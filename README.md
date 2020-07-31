# SafeShop_Distance_Tracking_Algorithm
### Repository for Distance Tracking Algorithm 

In this pandemic season and lockdown, people are required to follow certain rules and regulations to reduce and prevent further spread of the virus. The goal of this algorithm is to check if people are maintaining proper social distancing or not in public places.

#### Overview:

Let's say user has ordered something for nearby restaurant and he has been allocated a pick up. The user approaches the restaurant at the given time. When the user is within 10-15 feet of the restaurant, his GPS will start and his location (latitude and longitude) will be sent to Google FireBase Real-Time Database. 
(Same thing will be done for all the users who are within 10-15 feet range of the restaurant)

Now the distance and angle between the every person will be calculated using the locations from FireBase and every user will get a live realtime graph displaying distance and relative angle between him and every other other user in the range of restaurant.
If the user is within 6 feet range of any person, he will notified that there are people nearby in his range.
This algorithm will work continuously until as long as user is insiderr the 10-15 feet range of restaurant.

The repostiory contains the code which will be used to send live location updates to FireBase and code for making a graph after reading data from FireBase.
Currently, the graph is generated using random data and the codes are in Python.
We will be converting the code to JAVA and integrating the code with the Mobile App in future.

#### Tools and Technologies:
1. Python 3.x (matplotlib,firebase)
2. Google FireBase
3. We will be using JAVA in future

#### Images:

<p align="center">
  <img width="300" heigth="300" src="Images_for_readme/output2.png">
</p>
  
<p align="center">
  <img width="300" heigth="300" src="Images_for_readme/output2.png">
</p>
  
<p align="center">
  <img width="300" heigth="300" src="Images_for_readme/output2.png">
</p>
