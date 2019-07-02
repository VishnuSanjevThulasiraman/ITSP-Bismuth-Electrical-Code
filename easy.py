import math
from math import cos,sin,radians
val = 0

def value(a,b,c) :
    f=abs(a-b)
    g=abs(b-c)
    h=abs(a-c)
    if f<g :
        if f<h :
            return (a+b)/2
        else :
            return (a+c)/2
    else :
        if g<h :
            return (b+c)/2
        else :
            return (a+c)/2


final_array = [[0]*360 for i in range(151)]
arr = [[0]*1080 for i in range(151)]
for h in range(0,151,2) :
    for i in range(1080) :
         arr[h][i] = val;

for x in range(0,151,2) :
    arr1 = [[0] for i in range(360)]
    arr2 = [[0] for i in range(360)]
    arr3 = [[0] for i in range(360)]
    var = 0
    for i in range(360) :
        arr1[i] = arr[x][var]
        var = var + 3
    var = 1
    for i in range(60,360) :
        arr2[i] = arr[x][var]
        var = var + 3
    for i in range(0,60) :
        arr2[i] = arr[x][var]
        var = var + 3
    var = 2
    for i in range(120,360) :
        arr3[i] = arr[x][var]
        var = var + 3
    for i in range(0,120) :
        arr3[i] = arr[x][var]
        var = var +3

    for i in range(360) :
        final_array[x][i] = 20-value(arr1[i],arr2[i],arr3[i])

output = open(r"/Users/tsanjevvishnu/Desktop/points1.txt","w")
   
for h in range(0,151,2) :
    for a in range(360) :
        x = float(0)
        y = float(0)
        z = float(0)
        r = float(0)
        z=h
        r=final_array[h][a]
        x=r*cos(radians(a))
        y=r*sin(radians(a))
        str = "{}   {}  {}"
        output.write(str.format(x,y,z))
        output.write("\n")

output.close()
    


    

    
