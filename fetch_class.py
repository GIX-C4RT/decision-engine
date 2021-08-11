import grpc
import fetch_pb2
import fetch_pb2_grpc

from threading import Lock

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

  def delivered(self, future):
    """
      Call back when the checkout process is done. 
      Depending on situation it might call Kinova CheckOut function for next step
    """
    print("Fetch " + self.address_ + " gets back")
    print("Check response value is it delivered? ", future.result().delivered)

  def CheckOut(self, kit_ID = -1, kit_location = -1, target_location = -1):
    """
      Check out instruction that will be send to the fetch
    """
    self.future_ = self.stub_.CheckOut.future(fetch_pb2.CheckOutRequest(kit_ID=kit_ID, kit_location=kit_location, target_location=target_location))
    self.future_.add_done_callback(self.delivered)

if __name__ == "__main__":
  myfetch = Fetch()
  myfetch.CheckOut()
  while True:
    pass