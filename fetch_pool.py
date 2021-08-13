import grpc
import fetch_pb2
import fetch_pb2_grpc

import queue

from fetch_class import Fetch, FetchConfig
import time

class Fetch_pool:
  """Fetch pool Object that contains a queue of fetch ready for work

  This class is mainly used for load balancing and task scheduling. 
  User can get a fetch from the pool object and send it a Checkout or
  Checkin task then return the fetch to the pool (Since Checkout/Checkin
  for fetch is non-blocking you should return fetch right after sending
  the command)

  Typical usage example:

  myfetch_pool = Fetch_pool(2, ['localhost:50051', 'localhost:50052'])

  print("first request comes in")
  fetch = myfetch_pool.get_fetch()
  fetch_checkout_config = FetchConfig(operation="CheckOut", kit_ID=1, kit_location=255, target_location=255)
  fetch_checkout_config.call_back_ = lambda : print("fetch1_done")
  fetch.LoadConfig(fetch_checkout_config)
  fetch()
  myfetch_pool.return_fetch(fetch)

  time.sleep(4)
  print("second request comes in")
  fetch = myfetch_pool.get_fetch()
  fetch_checkout_config = FetchConfig(operation="CheckOut", kit_ID=2, kit_location=128, target_location=128)
  fetch_checkout_config.call_back_ = lambda : print("fetch2_done")
  fetch.LoadConfig(fetch_checkout_config)
  fetch()
  myfetch_pool.return_fetch(fetch)
  """
  def __init__(self, n = 1, addresses = ['localhost:50051']) -> None:
    """
      Initialize the fetch pool object, based on the number and addresses provided
    """
    self.q_ = queue.Queue()
    for i in range(n):
      self.q_.put(Fetch(address=addresses[i]))

  def get_fetch(self):
    """
      Get a fetch. If not already in use then set it's inuse state to true
    """
    fetch = self.q_.get()
    # Useing lock to prevent if robot is checked out and inuse set to true but
    # at the same time the same robot is being returned by another request
    while True:
      fetch.inuse_lock_.acquire()
      if not fetch.inuse_:
        fetch.inuse_ = True
        fetch.inuse_lock_.release()
        return fetch
      fetch.inuse_lock_.release()
      # Give time for other to return fetch to prevent deadlock
      time.sleep(1)

  def return_fetch(self, fetch):
    """
      return a fetch. by putting it back to the queue
      unlocking is done in the callback see fetch_class.py MetaCallBack func
    """
    self.q_.put(fetch)

if __name__ == "__main__":
  # Make sure fetch_server.py is running first
  myfetch_pool = Fetch_pool(2, ['localhost:50051', 'localhost:50052'])

  print("first request comes in")
  fetch = myfetch_pool.get_fetch()
  fetch_checkout_config = FetchConfig(operation="CheckOut", kit_ID=1, kit_location=255, target_location=255)
  fetch_checkout_config.call_back_ = lambda : print("fetch1_done")
  fetch.LoadConfig(fetch_checkout_config)
  fetch()
  myfetch_pool.return_fetch(fetch)

  time.sleep(4)
  print("second request comes in")
  fetch = myfetch_pool.get_fetch()
  fetch_checkout_config = FetchConfig(operation="CheckOut", kit_ID=2, kit_location=128, target_location=128)
  fetch_checkout_config.call_back_ = lambda : print("fetch2_done")
  fetch.LoadConfig(fetch_checkout_config)
  fetch()
  myfetch_pool.return_fetch(fetch)

  while True:
    print("doing other stuff")
    time.sleep(1)