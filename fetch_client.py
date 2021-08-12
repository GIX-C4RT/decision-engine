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
"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function
import logging

import grpc

import fetch_pb2
import fetch_pb2_grpc

import time

def delivered(future):
      print("Call back triggered when delivered")
      print("Check response value is it delivered? ", future.result().delivered)

def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    
    channel = grpc.insecure_channel('localhost:50051')
    stub = fetch_pb2_grpc.FetchStub(channel)
    # print(stub.CheckOut(kit_ID=1, kit_location=1, target_location=1))
    print("Sending Fetch for delivering")
    future = stub.CheckOut.future(fetch_pb2.CheckOutRequest(kit_ID=1, kit_location=1, target_location=1))
    future.add_done_callback(CheckOutComplete)
    print("Request Send")
    while True:
      print("doing something else")
      time.sleep(1)
    channel.close()


if __name__ == '__main__':
    logging.basicConfig()
    run()
