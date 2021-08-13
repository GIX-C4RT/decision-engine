# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc

import kinova_pb2
import kinova_pb2_grpc

import time
import random


class Greeter(kinova_pb2_grpc.KinovaServicer):

    def Kinova_CheckOut(self, request, context):
        for item in request.item_list:
          print("Grasping item ", item, "...")
          time.sleep(random.randint(1,3))
        print("CheckOut Done")
        return kinova_pb2.Kinova_CheckOutReply(item_ready=True)

    def Kinova_CheckIn(self, request, context):
        for item in request.item_list:
          print("Returning item ", item, "...")
          time.sleep(random.randint(1,3))
        print("CheckIn Done")
        return kinova_pb2.Kinova_CheckInReply(item_returned=True)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kinova_pb2_grpc.add_KinovaServicer_to_server(Greeter(), server)
    server.add_insecure_port('localhost:50053')
    server.start()

    server2 = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    kinova_pb2_grpc.add_KinovaServicer_to_server(Greeter(), server2)
    server2.add_insecure_port('localhost:50054')
    server2.start()

    server.wait_for_termination()
    server2.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
