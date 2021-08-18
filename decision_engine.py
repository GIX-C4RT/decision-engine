from typing import List
from fetch_pool import Fetch_pool
from kinova_pool import Kinova_pool
from kinova_class import KinovaConfig
from fetch_class import FetchConfig
import time

import grpc
from concurrent import futures

import webapp_pb2
import webapp_pb2_grpc

class DecisionEngine:
  """ Main Decision Engine Class, Core of the system

  This class provides the implementation of decision engine it can handle predefined 
  operation and potentially support customizable low code environment for client to 
  build customized pipline

  TODO: Adding low code customizable pipline config interface 

  Typical usage example:
  
  myengine = DecisionEngine()
  myengine.init_fetch_pool(n = 2, ip_list = ['localhost:50051', 'localhost:50052'])
  myengine.init_kinova_pool(n = 2, ip_list = ['localhost:50053', 'localhost:50054'])

  fetch_checkout_config = FetchConfig(operation="CheckOut", kit_ID=1, kit_location=255, target_location=255)
  kinova_checkout_config = KinovaConfig(operation="CheckOut", kit_ID=1, item_list=[2,4,6])

  fetch_checkin_config1 = FetchConfig(operation="CheckIn", kit_ID=2, kit_location=128, target_location=128)
  kinova_checkin_config1 = KinovaConfig(operation="CheckIn", kit_ID=2, item_list=[1,3,5])

  fetch_checkin_config2 = FetchConfig(operation="CheckIn", kit_ID=3, kit_location=64, target_location=64)
  kinova_checkin_config2 = KinovaConfig(operation="CheckIn", kit_ID=3, item_list=[7,8,9])

  myengine.op_CheckIn(fetch_checkin_config1, kinova_checkin_config1)
  myengine.op_CheckIn(fetch_checkin_config2, kinova_checkin_config2)
  myengine.op_CheckOut(fetch_checkout_config, kinova_checkout_config)
  myengine.op_CheckOut(fetch_checkout_config, kinova_checkout_config)
  myengine.op_CheckOut(fetch_checkout_config, kinova_checkout_config)
  """
  def __init__(self) -> None:
    """
      Init function
    """
    pass

  def init_fetch_pool(self, n : int, ip_list : List):
    """
      Init the fetch_pool object
    """
    self.fetch_pool_ = Fetch_pool(n, ip_list)
  
  def init_kinova_pool(self, n : int, ip_list : List):
    """
      Init the kinova_pool object
    """
    self.kinova_pool_ = Kinova_pool(n, ip_list)

  def op_CheckOut(self, fetch_config : FetchConfig, kinova_config : KinovaConfig):
    """ 
      predefined operation
    """
    fetch = self.fetch_pool_.get_fetch()
    kinova = self.kinova_pool_.get_kinova() 

    # Sequence of initialization is important because fetch would become a call back of kinova
    fetch_config.call_back_ = lambda:print("CheckOut finished")
    fetch.LoadConfig(fetch_config)
    
    kinova_config.call_back_ = fetch
    kinova.LoadConfig(kinova_config)
    ###########################################################################################

    kinova()

    self.fetch_pool_.return_fetch(fetch)
    self.kinova_pool_.return_kinova(kinova)

  def op_CheckIn(self, fetch_config : FetchConfig, kinova_config : KinovaConfig):
    """ 
      predefined operation
    """
    fetch = self.fetch_pool_.get_fetch()
    kinova = self.kinova_pool_.get_kinova()

    # Sequence of initialization is important because kinova would become a call back of fetch
    kinova_config.call_back_ = lambda:print("CheckIn finished")
    kinova.LoadConfig(kinova_config)

    fetch_config.call_back_ = kinova
    fetch.LoadConfig(fetch_config)
    ###########################################################################################

    fetch()

    self.fetch_pool_.return_fetch(fetch)
    self.kinova_pool_.return_kinova(kinova)

if __name__ == "__main__":
  class Greeter(webapp_pb2_grpc.WebAppServicer):
      """ Example class that defines the Fetch service

          This class provides an example on how to implement gRPC server on fetch
      """
      def __init__(self, engine):
        self.myengine_ = engine

      def WebApp_CheckOut(self, request, context):
        print(request.user_ID)
        print(request.item_ID)
        self.myengine_.op_CheckOut(fetch_checkout_config, kinova_checkout_config)
        return webapp_pb2.WebApp_CheckOutReply(ack = True)
        

      def WebApp_CheckIn(self, request, context):
        print(request.user_ID)
        print(request.item_ID)
        return webapp_pb2.WebApp_CheckInReply(ack = True)

  # Make sure fetch_server.py and kinova_server.py is running first
  myengine = DecisionEngine()
  myengine.init_fetch_pool(n = 2, ip_list = ['localhost:50051', 'localhost:50052'])
  myengine.init_kinova_pool(n = 2, ip_list = ['localhost:50053', 'localhost:50054'])

  fetch_checkout_config = FetchConfig(operation="CheckOut", kit_ID=1, kit_location=255, target_location=255)
  kinova_checkout_config = KinovaConfig(operation="CheckOut", kit_ID=1, item_list=[2,4,6])

  fetch_checkin_config1 = FetchConfig(operation="CheckIn", kit_ID=2, kit_location=128, target_location=128)
  kinova_checkin_config1 = KinovaConfig(operation="CheckIn", kit_ID=2, item_list=[1,3,5])

  fetch_checkin_config2 = FetchConfig(operation="CheckIn", kit_ID=3, kit_location=64, target_location=64)
  kinova_checkin_config2 = KinovaConfig(operation="CheckIn", kit_ID=3, item_list=[7,8,9])

  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  webapp_pb2_grpc.add_WebAppServicer_to_server(Greeter(myengine), server)
  server.add_insecure_port('10.155.234.132:50051')
  server.start()

  # myengine.op_CheckIn(fetch_checkin_config1, kinova_checkin_config1)
  # myengine.op_CheckIn(fetch_checkin_config2, kinova_checkin_config2)
  # myengine.op_CheckOut(fetch_checkout_config, kinova_checkout_config)
  # myengine.op_CheckOut(fetch_checkout_config, kinova_checkout_config)
  # myengine.op_CheckOut(fetch_checkout_config, kinova_checkout_config)

  while True:
    time.sleep(1)
    print("doing something else ... ")


