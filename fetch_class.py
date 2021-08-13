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
      self.operation_ = operation
      self.kit_ID_ = kit_ID
      self.kit_location_ = kit_location
      self.target_location_ = target_location
      self.call_back_ = call_back

class Fetch:
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
    self.stub_ = fetch_pb2_grpc.FetchStub(self.channel_)
    print("Initialize Fetch at " + self.address_)

  def __del__(self):
    """
      Destructor of the fetch object which will close the gRPC channel 
    """
    print("deleting Fetch at " + self.address_)
    self.channel_.close()

  def __call__(self, *args: Any, **kwds: Any) -> Any:
    if self.operation_ == "CheckOut":
      self.future_ = self.stub_.Fetch_CheckOut.future(fetch_pb2.Fetch_CheckOutRequest(kit_ID=self.kit_ID_, kit_location=self.kit_location_, target_location=self.target_location_))
      self.future_.add_done_callback(self.meta_call_back)
    elif self.operation_ == "CheckIn":
      self.future_ = self.stub_.Fetch_CheckIn.future(fetch_pb2.Fetch_CheckInRequest(kit_ID=self.kit_ID_, kit_location=self.kit_location_, target_location=self.target_location_))
      self.future_.add_done_callback(self.meta_call_back)

  def meta_call_back(self, future):
      self.inuse_lock_.acquire()
      self.inuse_ = False
      self.inuse_lock_.release()
      self.call_back_()

  def LoadConfig(self, config: FetchConfig):
    self.operation_ = config.operation_
    self.kit_ID_ = config.kit_ID_
    self.kit_location_ = config.kit_location_
    self.target_location_ = config.target_location_
    self.call_back_ = config.call_back_

  # def CheckOutComplete(self, future):
  #   """
  #     Call back when the checkout process is done. 
  #     Depending on situation it might call Kinova CheckOut function for next step
  #   """
  #   print("Fetch " + self.address_ + " gets back")
  #   print("Check response value is it delivered? ", future.result().delivered)

  # def CheckOut(self, kit_ID = -1, kit_location = -1, target_location = -1, call_back=None):
  #   """
  #     Check out instruction that will be send to the fetch
  #   """
  #   self.future_ = self.stub_.Fetch_CheckOut.future(fetch_pb2.Fetch_CheckOutRequest(kit_ID=kit_ID, kit_location=kit_location, target_location=target_location))
  #   if call_back:
  #     self.future_.add_done_callback(call_back)

if __name__ == "__main__":
  myfetch = Fetch()
  myfetch.CheckOut()
  while True:
    pass