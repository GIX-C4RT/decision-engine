from fetch_pool import Fetch_pool
from kinova_pool import Kinova_pool
from kinova_class import KinovaConfig
from fetch_class import FetchConfig
import time

myfetch_pool = Fetch_pool(2, ['localhost:50051', 'localhost:50052'])
mykinova_pool = Kinova_pool(2, ['localhost:50053', 'localhost:50054'])
print("request 1 coming")
fetch = myfetch_pool.get_fetch()
kinova = mykinova_pool.get_kinova()
mykinovaconfig = KinovaConfig(operation="CheckOut", kit_ID=1, item_list=[2,4,6], call_back = lambda _:print("request 1 finished"))
kinova.LoadConfig(mykinovaconfig)
myfetchconfig = FetchConfig(operation="CheckOut", kit_ID=1, kit_location=1, target_location=1, call_back=kinova)
fetch.LoadConfig(myfetchconfig)
fetch()
myfetch_pool.return_fetch(fetch)
mykinova_pool.return_kinova(kinova)

time.sleep(1)
print("request 2 coming")
fetch = myfetch_pool.get_fetch()
kinova = mykinova_pool.get_kinova()
mykinovaconfig = KinovaConfig(operation="CheckOut", kit_ID=2, item_list=[1,3,5], call_back = lambda _:print("request 2 finished"))
kinova.LoadConfig(mykinovaconfig)
myfetchconfig = FetchConfig(operation="CheckOut", kit_ID=2, kit_location=2, target_location=2, call_back=kinova)
fetch.LoadConfig(myfetchconfig)
fetch()
myfetch_pool.return_fetch(fetch)
mykinova_pool.return_kinova(kinova)
while True:
  pass
# class DecisionEngine:

