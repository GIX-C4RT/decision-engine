"""Example implementation of gRPC server that will run on the fetch. Currently just a mockup"""
from concurrent import futures
import logging

import grpc

import fetch_pb2
import fetch_pb2_grpc

import time
import random

class Greeter(fetch_pb2_grpc.FetchServicer):
  """ Example class that defines the Fetch service

      This class provides an example on how to implement gRPC server on fetch
  """
  def Fetch_CheckOut(self, request, context):
    """
      Fetch_CheckOut call that should perform the checkout sequence.
      Can be blocking
    """
    print("Kit ID = ", request.kit_ID, " kit_location = ", request.kit_location, " target_location = ", request.target_location)
    print("Kit ID = ", request.kit_ID, " Navigating...")
    time.sleep(random.randint(1,3))
    print("Kit ID = ", request.kit_ID, " Docking...")
    time.sleep(random.randint(1,3))
    print("Kit ID = ", request.kit_ID, " Grasping...")
    time.sleep(random.randint(1,3))
    print("Kit ID = ", request.kit_ID, " Delivering")
    time.sleep(random.randint(4,8))
    print("Kit ID = ", request.kit_ID, " Checked Out")
    return fetch_pb2.Fetch_CheckOutReply(delivered=True)

  def Fetch_CheckIn(self, request, context):
    """
      Fetch_CheckIn call that should perform the checkin sequence.
      Can be blocking
    """
    print("Kit ID = ", request.kit_ID, " kit_location = ", request.kit_location, " target_location = ", request.target_location)
    print("Kit ID = ", request.kit_ID, " retriving packing...")
    time.sleep(random.randint(1,3))
    print("Kit ID = ", request.kit_ID, " handing over...")
    time.sleep(random.randint(1,3))
    print("Kit ID = ", request.kit_ID, " Returned")
    return fetch_pb2.Fetch_CheckInReply(returned=True)

def serve():
  """
    Example init function for starting the service
  """
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  fetch_pb2_grpc.add_FetchServicer_to_server(Greeter(), server)
  server.add_insecure_port('localhost:50051')
  server.start()

  server2 = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  fetch_pb2_grpc.add_FetchServicer_to_server(Greeter(), server2)
  server2.add_insecure_port('localhost:50052')
  server2.start()

  server.wait_for_termination()
  server2.wait_for_termination()

if __name__ == '__main__':
  logging.basicConfig()
  serve()
