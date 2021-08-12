from fetch_pool import Fetch_pool
from kinova_pool import Kinova_pool

myfetch_pool = Fetch_pool(2, ['localhost:50051', 'localhost:50052'])
mykinova_pool = Kinova_pool(2, ['localhost:50053', 'localhost:50054'])
fetch = myfetch_pool.get_fetch()
kinova = Kinova_pool.get_kinova()
fetch.Checkout(lambda: kinova.CheckOut(kit_ID = 5, item_list = [3,2,1], call_back = lambda:print("finished")))
# class DecisionEngine:

