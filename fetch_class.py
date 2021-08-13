import grpc
import fetch_pb2
import fetch_pb2_grpc

from threading import Lock
from typing import Any

class FetchConfig:
  """An reuseable configuration object for potential mass deployment with low code interface

     Can change to XML or JSON format for easy editing
  """
  def __init__(self, operation = None, kit_ID = None, kit_location = None, target_location = None, call_back = None) -> None:
    """
      Initialize the config object
    """
    # Operation, currently support 'CheckOut' and 'CheckIn'
    self.operation_ = operation
    # kit_ID, the ID of the kit that fetch need to pickup or retrive
    self.kit_ID_ = kit_ID
    # kit_location, current location of the kit
    self.kit_location_ = kit_location
    # target_location, target location the kit need to go to
    self.target_location_ = target_location
    # call_back, call back function that will invoke after the call made to Fetch() functor
    self.call_back_ = call_back

class Fetch:
  """Fetch Object that contains the gRPC connection to a fetch at a certain ip.

  This class is mainly used for the Fetch_pool class. Since a gRPC connection need
  to be remain connected this object will hold the connection until it is getting 
  destructed

  Typical usage example:

  fetch_checkout_config = FetchConfig(operation="CheckOut", kit_ID=1, kit_location=255, target_location=255)
  fetch = Fetch()
  fetch.LoadConfig(fetch_checkout_config)
  fetch()
  """
  def __init__(self, address = 'localhost:50051') -> None:
    """
      Initialize the fetch object, initialize the gRPC channel with address and stub
      Also sets inuse to False and create a lock for modify it concurrently
    """
    self.inuse_ = False
    self.inuse_lock_ = Lock()
    self.address_ = address
    self.channel_ = grpc.insecure_channel(self.address_)
    self.stub_ = fetch_pb2_grpc.FetchStub(self.channel_)
    print("Initialize Fetch at " + self.address_)

  def __del__(self):
    """
      Destructor of the fetch object which will close the gRPC channel 
    """
    print("deleting Fetch at " + self.address_)
    self.channel_.close()

  def __call__(self, *args: Any, **kwds: Any) -> Any:
    """
      Main call that will init the RPC 
      Also sets the call back to meta call back

      TODO: should use dict based condition for extendbility
    """
    if self.operation_ == "CheckOut":
      self.future_ = self.stub_.Fetch_CheckOut.future(fetch_pb2.Fetch_CheckOutRequest(kit_ID=self.kit_ID_, kit_location=self.kit_location_, target_location=self.target_location_))
      self.future_.add_done_callback(self.MetaCallBack_)
    elif self.operation_ == "CheckIn":
      self.future_ = self.stub_.Fetch_CheckIn.future(fetch_pb2.Fetch_CheckInRequest(kit_ID=self.kit_ID_, kit_location=self.kit_location_, target_location=self.target_location_))
      self.future_.add_done_callback(self.MetaCallBack_)

  def MetaCallBack_(self, future):
    """
      This will be called after the async RPC routing finished which means this fetch
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

  def LoadConfig(self, config: FetchConfig):
    """
      Simple helper for loading config object
    """
    self.operation_ = config.operation_
    self.kit_ID_ = config.kit_ID_
    self.kit_location_ = config.kit_location_
    self.target_location_ = config.target_location_
    self.call_back_ = config.call_back_

if __name__ == "__main__":
  # Make sure fetch_server.py is running first
  fetch_checkout_config = FetchConfig(operation="CheckOut", kit_ID=1, kit_location=255, target_location=255)
  fetch_checkout_config.call_back_ = lambda : print("CheckOut Success")
  fetch = Fetch()
  fetch.LoadConfig(fetch_checkout_config)
  fetch()
  while True:
    pass