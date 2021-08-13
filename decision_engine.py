from typing import List
from fetch_pool import Fetch_pool
from kinova_pool import Kinova_pool
from kinova_class import KinovaConfig
from fetch_class import FetchConfig
import time

class DecisionEngine:
  def __init__(self) -> None:
      pass

  def init_fetch_pool(self, n : int, ip_list : List):
    self.fetch_pool_ = Fetch_pool(n, ip_list)
  
  def init_kinova_pool(self, n : int, ip_list : List):
    self.kinova_pool_ = Kinova_pool(n, ip_list)

  def op_CheckOut(self, fetch_config : FetchConfig, kinova_config : KinovaConfig):
    """ predefined operation
    """
    fetch = self.fetch_pool_.get_fetch()
    kinova = self.kinova_pool_.get_kinova() 

    fetch_config.call_back_ = lambda _:print("CheckOut finished")
    kinova_config.call_back_ = fetch

    fetch.LoadConfig(fetch_config)
    kinova.LoadConfig(kinova_config)

    kinova()

    self.fetch_pool_.return_fetch(fetch)
    self.kinova_pool_.return_kinova(kinova)

  def op_CheckIn(self, fetch_config : FetchConfig, kinova_config : KinovaConfig):
    """ predefined operation
    """
    fetch = self.fetch_pool_.get_fetch()
    kinova = self.kinova_pool_.get_kinova()

    fetch_config.call_back_ = kinova
    kinova_config.call_back_ = lambda _:print("CheckIn finished")

    kinova.LoadConfig(kinova_config)
    fetch.LoadConfig(fetch_config)

    fetch()

    self.fetch_pool_.return_fetch(fetch)
    self.kinova_pool_.return_kinova(kinova)

if __name__ == "__main__":
  myengine = DecisionEngine()
  myengine.init_fetch_pool(n = 2, ip_list = ['localhost:50051', 'localhost:50052'])
  myengine.init_kinova_pool(n = 2, ip_list = ['localhost:50053', 'localhost:50054'])

  fetch_checkout_config = FetchConfig(operation="CheckOut", kit_ID=1, kit_location=1, target_location=1)
  kinova_checkout_config = KinovaConfig(operation="CheckOut", kit_ID=1, item_list=[2,4,6])

  fetch_checkout_config = FetchConfig(operation="CheckIn", kit_ID=2, kit_location=2, target_location=2)
  kinova_checkout_config = KinovaConfig(operation="CheckIn", kit_ID=2, item_list=[1,3,5])

  myengine.op_CheckIn(fetch_checkout_config, kinova_checkout_config)
  myengine.op_CheckOut(fetch_checkout_config, kinova_checkout_config)


