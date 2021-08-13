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

import fetch_pb2
import fetch_pb2_grpc

import time
import random


class Greeter(fetch_pb2_grpc.FetchServicer):
    def Fetch_CheckOut(self, request, context):
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
        print("Kit ID = ", request.kit_ID, " kit_location = ", request.kit_location, " target_location = ", request.target_location)
        print("Kit ID = ", request.kit_ID, " retriving packing...")
        time.sleep(random.randint(1,3))
        print("Kit ID = ", request.kit_ID, " handing over...")
        time.sleep(random.randint(1,3))
        print("Kit ID = ", request.kit_ID, " Returned")
        return fetch_pb2.Fetch_CheckInReply(returned=True)


def serve():
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
