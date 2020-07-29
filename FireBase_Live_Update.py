from firebase import firebase
import random

#code to randomly update lat and long on firebase database to show realtime updates 
firebase=firebase.FirebaseApplication('https://fir-cdafa.firebaseio.com/',None)

key=[]
lat=[]
longg=[]
add='/fir-cdafa/location/'
result=firebase.get(add,'')
for i in result:
    key.append(i)
    for j in result[i]:
        if j=='lat':
            lat.append(result[i][j])
        if j=='long':
            longg.append(result[i][j])


while(1):

    add='/fir-cdafa/location/'
    result=firebase.get(add,'')
    
    for i in range(len(key)):
        tempadd=add+key[i]
        lat[i]=lat[i]+(random.randint(-9,9)*0.000001)
        longg[i]=longg[i]+(random.randint(-9,9)*0.000001)
        firebase.put(tempadd,'lat',lat[i])
        firebase.put(tempadd,'long',longg[i])
            
    print(1)

