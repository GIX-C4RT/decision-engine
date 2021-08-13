import grpc
import kinova_pb2
import kinova_pb2_grpc

from threading import Lock
from typing import Any

class KinovaConfig:
  """An reuseable configuration object for potential mass deployment with low code interface

     Can change to XML or JSON format for easy editing
  """
  def __init__(self, operation = None, kit_ID = None, item_list = None, call_back = None) -> None:
    """
      Initialize the config object
    """
    self.operation_ = operation
    self.kit_ID_ = kit_ID
    self.item_list_ = item_list
    self.call_back_ = call_back

class Kinova:
  """Kinova Object that contains the gRPC connection to a kinova at a certain ip.

  This class is mainly used for the Kinova_pool class. Since a gRPC connection need
  to be remain connected this object will hold the connection until it is getting 
  destructed

  Typical usage example:

  kinova_checkout_config = KinovaConfig(operation="CheckOut", kit_ID=1, item_list=[1,2,3])
  kinova_checkout_config.call_back_ = lambda : print("CheckOut Success")
  kinova = Kinova('localhost:50053')
  kinova.LoadConfig(kinova_checkout_config)
  kinova()
  """
  def __init__(self, address = 'localhost:50051') -> None:
    """
      Initialize the kinova object, initialize the gRPC channel with address and stub
      Also sets inuse to False and create a lock for modify it concurrently
    """
    self.inuse_ = False
    self.inuse_lock_ = Lock()
    self.address_ = address
    self.channel_ = grpc.insecure_channel(self.address_)
    self.stub_ = kinova_pb2_grpc.KinovaStub(self.channel_)
    print("Initialize Kinova at " + self.address_)

  def __del__(self):
    """
      Destructor of the kinova object which will close the gRPC channel 
    """
    print("deleting Kinova at " + self.address_)
    self.channel_.close()

  def __call__(self, *args: Any, **kwds: Any) -> Any:
    """
      Main call that will init the RPC 
      Also sets the call back to meta call back

      TODO: should use dict based condition for extendbility
    """
    if self.operation_ == "CheckOut":
      self.future_ = self.stub_.Kinova_CheckOut.future(kinova_pb2.Kinova_CheckOutRequest(kit_ID = self.kit_ID_, item_list = self.item_list_))
      self.future_.add_done_callback(self.MetaCallBack_)
    elif self.operation_ == "CheckIn":
      self.future_ = self.stub_.Kinova_CheckIn.future(kinova_pb2.Kinova_CheckInRequest(kit_ID = self.kit_ID_, item_list = self.item_list_))
      self.future_.add_done_callback(self.MetaCallBack_)

  def MetaCallBack_(self, future):
    """
      This will be called after the async RPC routing finished which means this kinova
      object is no longer in used. So if we can get the lock (There might be some one
      wants to get this object from the pool but that function have a time.sleep(1) in
      the loop that check the lock [it will acquire the lock check the inuse state then
      release the lock] so no deadlock will happen. Here the acquire will block until 
      it gets the lock)we can set it to free state and invoke the actual call back

      TODO: NEED TO CHECK IF RPC CALL SUCCESS
    """
    self.inuse_lock_.acquire()
    self.inuse_ = False
    self.inuse_lock_.release()
    if self.call_back_:
      self.call_back_()

  def LoadConfig(self, config: KinovaConfig):
    """
      Simple helper for loading config object
    """
    self.operation_ = config.operation_
    self.kit_ID_ = config.kit_ID_
    self.item_list_ = config.item_list_
    self.call_back_ = config.call_back_

if __name__ == "__main__":
  # Make sure kinova_server.py is running first
  kinova_checkout_config = KinovaConfig(operation="CheckOut", kit_ID=1, item_list=[1,2,3])
  kinova_checkout_config.call_back_ = lambda : print("CheckOut Success")
  kinova = Kinova('localhost:50053')
  kinova.LoadConfig(kinova_checkout_config)
  kinova()
  while True:
    pass