import grpc
import kinova_pb2
import kinova_pb2_grpc

import queue

from kinova_class import Kinova

class Kinova_pool:
  """Kinova pool Object that contains a queue of kinova ready for work

  This class is mainly used for load balancing and task scheduling. 
  User can get a kinova from the pool object and send it a Checkout or
  Checkin task then return the kinova to the pool (Since Checkout/Checkin
  for kinova is non-blocking you should return kinova right after sending
  the command)

  Typical usage example:

  mykinova_pool = Kinova_pool(2, ['localhost:50051', 'localhost:50052'])

  kinova = mykinova_pool.get_kinova()
  kinova.CheckOut()
  mykinova_pool.return_kinova(kinova)

  kinova = mykinova_pool.get_kinova()
  kinova.CheckOut()
  mykinova_pool.return_kinova(kinova)
  """
  def __init__(self, n = 1, addresses = ['localhost:50051']) -> None:
    """
      Initialize the kinova pool object, based on the number and addresses provided
    """
    self.q_ = queue.Queue()
    for i in range(n):
      self.q_.put(Kinova(address=addresses[i]))

  def get_kinova(self):
    """
      Get a kinova. If not already in use then set it's inuse state to true
    """
    kinova = self.q_.get()
    # We might need lock here the concurrency is relatively low 
    # so mutex won't have a big performance hit
    while True:
      kinova.inuse_lock_.acquire()
      if not kinova.inuse_:
        kinova.inuse_ = True
        kinova.inuse_lock_.release()
        return kinova
      kinova.inuse_lock_.release()
      # Give time for other to return kinova to prevent deadlock
      time.sleep(1)

  def return_kinova(self, kinova):
    """
      return a kinova. set it's inuse state to False
    """
    # We might need lock here the concurrency is relatively low 
    # so mutex won't have a big performance hit
    kinova.inuse_lock_.acquire()
    kinova.inuse_ = False
    kinova.inuse_lock_.release()
    self.q_.put(kinova)

if __name__ == "__main__":
  import time
  mykinova_pool = Kinova_pool(2, ['localhost:50053', 'localhost:50054'])

  print("first request comes in")
  kinova = mykinova_pool.get_kinova()
  kinova.CheckOut()
  mykinova_pool.return_kinova(kinova)

  time.sleep(4)
  print("second request comes in")
  kinova = mykinova_pool.get_kinova()
  kinova.CheckOut()
  mykinova_pool.return_kinova(kinova)

  while True:
    print("doing other stuff")
    time.sleep(1)