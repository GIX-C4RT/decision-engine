from fetch_pool import Fetch_pool
from kinova_pool import Kinova_pool
from kinova_class import KinovaConfig
import time

myfetch_pool = Fetch_pool(2, ['localhost:50051', 'localhost:50052'])
mykinova_pool = Kinova_pool(2, ['localhost:50053', 'localhost:50054'])
print("request 1 coming")
fetch = myfetch_pool.get_fetch()
kinova = mykinova_pool.get_kinova()
myconfig = KinovaConfig(operation="CheckOut", kit_ID=1, item_list=[2,4,6], call_back = lambda _:print("request 1 finished"))
kinova.LoadConfig(myconfig)
fetch.CheckOut(call_back = kinova)
myfetch_pool.return_fetch(fetch)
mykinova_pool.return_kinova(kinova)

time.sleep(5)
print("request 2 coming")
fetch = myfetch_pool.get_fetch()
kinova = mykinova_pool.get_kinova()
fetch.CheckOut(call_back = lambda _: kinova.CheckOut(kit_ID = 5, item_list = [3,5,7], call_back = lambda _:print("request 2 finished")))
myfetch_pool.return_fetch(fetch)
mykinova_pool.return_kinova(kinova)
while True:
  pass
# class DecisionEngine:

