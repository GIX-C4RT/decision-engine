import grpc
import fetch_pb2
import fetch_pb2_grpc

import queue

from fetch_class import Fetch

class Fetch_pool:
  """Fetch pool Object that contains a queue of fetch ready for work

  This class is mainly used for load balancing and task scheduling. 
  Since a gRPC connection need
  to be remain connected this object will hold the connection until it is getting 
  destructed

  Typical usage example:

  myfetch = Fetch()
  myfetch2 = Fetch('localhost:50051')
  myfetch.CheckOut()
  """
  def __init__(self, n = 1, addresses = ['localhost:50051']) -> None:
    self.q_ = queue.Queue()
    for i in range(n):
      self.q_.put(Fetch(address=addresses[i]))

  def get_fetch(self):
    fetch = self.q_.get()
    # We might need lock here the concurrency is relatively low 
    # so mutex won't have a big performance hit
    fetch.inuse_lock_.acquire()
    fetch.inuse_ = True
    fetch.inuse_lock_.release()
    return fetch

  def return_fetch(self, fetch):
    # We might need lock here the concurrency is relatively low 
    # so mutex won't have a big performance hit
    fetch.inuse_lock_.acquire()
    fetch.inuse_ = False
    fetch.inuse_lock_.release()
    self.q_.put(fetch)

if __name__ == "__main__":
  import time
  myfetch_pool = Fetch_pool(2, ['localhost:50051', 'localhost:50052'])

  print("first request comes in")
  fetch = myfetch_pool.get_fetch()
  fetch.CheckOut()
  myfetch_pool.return_fetch(fetch)

  time.sleep(4)
  print("second request comes in")
  fetch = myfetch_pool.get_fetch()
  fetch.CheckOut()
  myfetch_pool.return_fetch(fetch)

  while True:
    print("doing other stuff")
    time.sleep(1)