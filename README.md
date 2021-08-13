# Decision Engine
This repo includes the core code of our decision engine

# Summary
## Feature
- Capable of handle large amount of robots (over 1000)
- Allow concurrent access
- Full async based scheduling
- Potentially support low / no code pipeline building (Under development)

## Scheduling / Concurrency
This Decision Engine will allow as many fetch and kinova farm as we want and since everything is async. Our decision engine won't be blocked by a large amount of concurrent request. It can handle as many request as the min(fetch, kinova) the client has at sametime. All the scheduling is being done under the hood that is not senseble for the user.  

# Build protobuf support file
A makefile is provided for using GNU make to generate the following file (Those are automatically generated based on .proto file and should not be modify by hand in anyway)
```
fetch_pb2_grpc.py
fetch_pb2.py
kinova_pb2_grpc.py
kinova_pb2.py
```
To execute the generation, run the following command in terminal
```
make
```
**IMPORTANT NOTE**  
If protobuf is modified and files are re-generated python won't automatically update cache to using the new file. So to make sure you are using the correct file please run 
```
rm -rf __pycache__
```
in the current directory

# Run the Decision Engine
## Running on real robot
Currently all example code are provided assuming running `decision engine`, `fetch server` and `kinova server` on the same local machine. In real life please run `fetch server` on fetch, `kinova server` on the computer that connects to kinova arms and `decision engine` on your main server. After that please set appropriate firewall setting and port setting in the code.

## Running on local machine (simulated)
Please execute the following command in seperate terminal. 
```
python fetch_server.py
```
```
python kinova_server.py
```
```
python decision_engine.py
```
Note here fetch_server by default launching two server (mock up for running on two fetch robot) at `localhost:50051` and `localhost:50052`. kinova_server by default launching two server (mock up for running on two set of kinova arms) at `localhost:50053` and `localhost:50054`. This is also the ip that `decision engine` assumes. Feel free to change to adapt to your local network environment.

## **[Video Demo Link](https://youtu.be/4LqepKzcOeQ)**

### Expacted output  

`fetch server` terminal
```
Kit ID =  2  kit_location =  128  target_location =  128
Kit ID =  3  kit_location =  64  target_location =  64
Kit ID =  2  retriving packing...
Kit ID =  3  retriving packing...
Kit ID =  2  handing over...
Kit ID =  3  handing over...
Kit ID =  3  Returned
Kit ID =  2  Returned
Kit ID =  1  kit_location =  255  target_location =  255
Kit ID =  1  Navigating...
Kit ID =  1  Docking...
Kit ID =  1  Grasping...
Kit ID =  1  kit_location =  255  target_location =  255
Kit ID =  1  Navigating...
Kit ID =  1  Docking...
Kit ID =  1  Delivering
Kit ID =  1  Grasping...
Kit ID =  1  Delivering
Kit ID =  1  Checked Out
Kit ID =  1  Checked Out
Kit ID =  1  kit_location =  255  target_location =  255
Kit ID =  1  Navigating...
Kit ID =  1  Docking...
Kit ID =  1  Grasping...
Kit ID =  1  Delivering
Kit ID =  1  Checked Out
```

`kinova server` terminal

```
Grasping item  1 ...
Grasping item  2 ...
Grasping item  3 ...
CheckOut Done
Grasping item  1 ...
Grasping item  2 ...
Grasping item  3 ...
Grasping item  1 ...
CheckOut Done
Grasping item  2 ...
Grasping item  3 ...
CheckOut Done
Returning item  7 ...
Returning item  1 ...
Returning item  3 ...
Returning item  8 ...
Returning item  9 ...
Returning item  5 ...
CheckIn Done
CheckIn Done
Grasping item  2 ...
Grasping item  2 ...
Grasping item  4 ...
Grasping item  6 ...
Grasping item  4 ...
CheckOut Done
Grasping item  6 ...
CheckOut Done
Grasping item  2 ...
Grasping item  4 ...
Grasping item  6 ...
CheckOut Done
```

`decision engine` terminal

```
Initialize Fetch at localhost:50051
Initialize Fetch at localhost:50052
Initialize Kinova at localhost:50053
Initialize Kinova at localhost:50054
CheckIn finished
CheckIn finished
CheckOut finished
CheckOut finished
doing something else ...
...
doing something else ... 
doing something else ... 
CheckOut finished
doing something else ... 
...
doing something else ...
```

# List of class
## **DecisionEngine**
**Main Decision Engine Class, Core of the system**

This class provides the implementation of decision engine it can handle predefined 
operation and potentially support customizable low code environment for client to 
build customized pipline

TODO: Adding low code customizable pipline config interface 

## **Fetch**
**Fetch Object that contains the gRPC connection to a fetch at a certain ip.**

This class is mainly used for the Fetch_pool class. Since a gRPC connection need
to be remain connected this object will hold the connection until it is getting 
destructed  

## **FetchConfig**
**An reuseable configuration object for potential mass deployment with low code interface**

Can change to XML or JSON format for easy editing  

## **Fetch_pool**
**Fetch pool Object that contains a queue of fetch ready for work**

This class is mainly used for load balancing and task scheduling. 
User can get a fetch from the pool object and send it a Checkout or
Checkin task then return the fetch to the pool (Since Checkout/Checkin
for fetch is non-blocking you should return fetch right after sending
the command)

## **Kinova**
**Kinova Object that contains the gRPC connection to a kinova at a certain ip.**

This class is mainly used for the Kinova_pool class. Since a gRPC connection need
to be remain connected this object will hold the connection until it is getting 
destructed

## **KinovaConfig**
**An reuseable configuration object for potential mass deployment with low code interface**

Can change to XML or JSON format for easy editing

## **Kinova_pool**
**Kinova pool Object that contains a queue of kinova ready for work**

This class is mainly used for load balancing and task scheduling. 
User can get a kinova from the pool object and send it a Checkout or
Checkin task then return the kinova to the pool (Since Checkout/Checkin
for kinova is non-blocking you should return kinova right after sending
the command)