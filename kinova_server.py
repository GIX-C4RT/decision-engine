"""Example implementation of gRPC server that will run on the kinova. Currently just a mockup"""

from concurrent import futures
import logging

import grpc

import kinova_pb2
import kinova_pb2_grpc

import time
import random


class Greeter(kinova_pb2_grpc.DeweyKinovaServicer):
  """ Example class that defines the Fetch service

      This class provides an example on how to implement gRPC server on fetch
  """
  def Kinova_CheckOut(self, request, context):
    """
      Kinova_CheckOut call that should perform the checkout sequence.
      Can be blocking
    """
    for item in request.item_list:
      print("Grasping item ", item, "...")
      time.sleep(random.randint(1,3))
    print("CheckOut Done")
    return kinova_pb2.Kinova_CheckOutReply(item_ready=True)

  def Kinova_CheckIn(self, request, context):
    """
      Kinova_CheckIn call that should perform the checkin sequence.
      Can be blocking
    """
    for item in request.item_list:
      print("Returning item ", item, "...")
      time.sleep(random.randint(1,3))
    print("CheckIn Done")
    return kinova_pb2.Kinova_CheckInReply(item_returned=True)


def serve():
  """
    Example init function for starting the service
  """
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  kinova_pb2_grpc.add_DeweyKinovaServicer_to_server(Greeter(), server)
  server.add_insecure_port('localhost:50053')
  server.start()

  server2 = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  kinova_pb2_grpc.add_DeweyKinovaServicer_to_server(Greeter(), server2)
  server2.add_insecure_port('localhost:50054')
  server2.start()

  server.wait_for_termination()
  server2.wait_for_termination()


if __name__ == '__main__':
  logging.basicConfig()
  serve()
