import grpc
import kinova_pb2
import kinova_pb2_grpc

from threading import Lock
from typing import Any

class KinovaConfig:
  """An reuseable configuration object for potential mass deployment with low code interface
  """
  def __init__(self, operation = None, kit_ID = None, item_list = None, call_back = None) -> None:
      self.operation_ = operation
      self.kit_ID_ = kit_ID
      self.item_list_ = item_list
      self.call_back_ = call_back

class Kinova:
  """Fetch Object that contains the gRPC connection to a fetch at a certain ip.

  This class is mainly used for the Fetch_pool class. Since a gRPC connection need
  to be remain connected this object will hold the connection until it is getting 
  destructed

  Typical usage example:

  myfetch = Fetch()
  myfetch2 = Fetch('localhost:50051')
  myfetch.CheckOut()
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
    self.stub_ = kinova_pb2_grpc.KinovaStub(self.channel_)
    print("Initialize Kinova at " + self.address_)

  def __del__(self):
    """
      Destructor of the fetch object which will close the gRPC channel 
    """
    print("deleting Kinova at " + self.address_)
    self.channel_.close()

  def __call__(self, *args: Any, **kwds: Any) -> Any:
      # should change to dictionary based condition for future extension
      if self.operation_ == "CheckOut":
        self.future_ = self.stub_.Kinova_CheckOut.future(kinova_pb2.Kinova_CheckOutRequest(kit_ID = self.kit_ID_, item_list = self.item_list_))
        self.future_.add_done_callback(self.call_back_)
      elif self.operation_ == "CheckIn":
        self.future_ = self.stub_.Kinova_CheckIn.future(kinova_pb2.Kinova_CheckInRequest(kit_ID = self.kit_ID_, item_list = self.item_list_))
        self.future_.add_done_callback(self.call_back_)

  def LoadConfig(self, config: KinovaConfig):
    self.operation_ = config.operation_
    self.kit_ID_ = config.kit_ID_
    self.item_list_ = config.item_list_
    self.call_back_ = config.call_back_
  # def operation_complete(self, future):
  #   """
  #     Call back when the checkout process is done. 
  #     Depending on situation it might call Kinova CheckOut function for next step
  #   """
  #   print("Kinova " + self.address_ + " completes operation")
  #   print("Check response value is it delivered? ", future.result().item_ready)

  # def CheckOut(self, kit_ID = -1, item_list = [1,2,3], call_back = None):
  #   """
  #     Check out instruction that will be send to the fetch
  #   """
  #   self.future_ = self.stub_.Kinova_CheckOut.future(kinova_pb2.Kinova_CheckOutRequest(kit_ID = kit_ID, item_list = item_list))
  #   if call_back:
  #     self.future_.add_done_callback(call_back)

if __name__ == "__main__":
  myfetch = Kinova()
  myfetch.CheckOut(call_back=lambda x: print("Sorting finished"))
  while True:
    pass