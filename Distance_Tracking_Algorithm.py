import matplotlib.pyplot as plt
import math
import numpy as np
import time
import random
from firebase import firebase

#code for distance tracking algorithm
#read realtime data from firebase and using that calculate distance between people and show on a graph

lat1=39.099912
long1=-94.581213

firebase=firebase.FirebaseApplication('https://fir-cdafa.firebaseio.com/',None)

add='/fir-cdafa/location/'
result=firebase.get(add,'')
key=[]
lat=[]
longg=[]

for i in result:
    key.append(i) 
    for j in result[i]:
        if j=='lat':
            lat.append(result[i][j])
        if j=='long':
            longg.append(result[i][j])

plt.ion()
plt.figure()
plt.show()

while(1):

    plt.xlabel('X AXIS',fontsize=7)
    plt.ylabel('Y AXIS',fontsize=7)

    plt.plot(0,0,'bo')
    plt.annotate("You",(0,0))

    count=0

    for i in range(len(lat)):

        X=math.cos(math.radians(lat[i]))*math.sin(math.radians(longg[i]-long1))
        Y=math.cos(math.radians(lat1))*math.sin(math.radians(lat[i]))-math.sin(math.radians(lat1))*math.cos(math.radians(lat[i]))*math.cos(math.radians(longg[i]-long1))

        bangle=math.atan2(X,Y)
        bangle=math.degrees(bangle)
        bangle=(bangle+360)%360

        p=math.pi/180
        dist=0.5-math.cos((lat[i]-lat1)*p)/2+math.cos(lat1*p)*math.cos(lat[i]*p)*(1-math.cos((longg[i]-long1)*p))/2
        dist=12742*math.asin(math.sqrt(dist))
        dist=dist*3280.84


        if bangle==0 or bangle==360:
            if dist<=6:
                plt.plot(dist,0,'ro')
                count=count+1
            else:
                plt.plot(dist,0,'go')
            plt.annotate(str(dist),(dist,0))
        elif bangle==90:
            if dist<=6:
                plt.plot(0,dist,'ro')
                count=count+1
            else:
                plt.plot(0,dist,'go')
            plt.annotate(str(dist),(0,dist))
        elif bangle==180:
            if dist<=6:
                plt.plot(-dist,0,'ro')
                count=count+1 
            else:
                plt.plot(-dist,0,'go')
            plt.annotate(str(dist),(-dist,0))
        elif bangle==270:
            if dist<=6:
                plt.plot(0,-dist,'ro')
                count=count+1
            else:
                plt.plot(0,-dist,'go')
            plt.annotate(str(dist),(0,-dist))
        else:
            if(bangle>0 and bangle<90):
                angle=90-bangle
                y=math.sin(math.radians(angle))*dist
                x=math.cos(math.radians(angle))*dist 
                if dist<=6:
                    plt.plot(x,y,'ro')
                    count=count+1 
                else:
                    plt.plot(x,y,'go')
                plt.annotate(str(dist),(x,y))
            elif(bangle>90 and bangle<180):
                bangle=bangle-90
                angle=90-bangle 
                x=math.sin(math.radians(angle))*dist
                y=math.cos(math.radians(angle))*dist
                if dist<=6:
                    plt.plot(x,-y,'ro')
                    count=count+1 
                else:
                    plt.plot(x,-y,'go')
                plt.annotate(str(dist),(x,-y))
            elif(bangle>180 and bangle<270):
                bangle=bangle-180
                x=math.sin(math.radians(bangle))*dist
                y=math.cos(math.radians(bangle))*dist
                if dist<=6:  
                    plt.plot(-x,-y,'ro')
                    count=count+1
                else:
                    plt.plot(-x,-y,'go')
                plt.annotate(str(dist),(-x,-y))
            else:
                bangle=bangle-270
                y=math.sin(math.radians(bangle))*dist 
                x=math.cos(math.radians(bangle))*dist
                if dist<=6: 
                    plt.plot(-x,y,'ro')
                    count=count+1
                else:
                    plt.plot(-x,y,'go')
                plt.annotate(str(dist),(-x,y))

    plt.title("Restaurant Name!")
    if count==0:
        plt.figtext(0.5,0,"No people in radius!",wrap=True,horizontalalignment='center',color='green')
    else:
        plt.figtext(0.5,0.01,str(count)+" people in radius! Please Maintain Social Distancing!",wrap=True,horizontalalignment='center',color='red')
        
    plt.show()
    plt.pause(1)
    plt.clf()
    plt.cla()

    result=firebase.get(add,'')
    keycount=0
    for i in result:
        key[keycount]=result
        for j in result[i]:
            if j=='lat':
                lat[keycount]=result[i][j]
            if j=='long':
                longg[keycount]=result[i][j]
        keycount=keycount+1
