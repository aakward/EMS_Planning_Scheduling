import math
from pulp import *
import numpy as np
import matplotlib.pyplot as plt


def main():
    l=input("Enter the length of the rectangular region: ")
    w=input("Enter the width of the rectangualr region: ")
    k=input("Enter the value of k: ")
    N=input("Enter the no. of EMS locations: ")
    loc=[]
    for i in range(N):
        a=input("Enter a location: ")
        loc.append(a)
    d1=float(l)/k
    d2=float(w)/k
    coord=[]
    for j in range(k+1):
        temp=[]
        for i in range(k+1):
            itemp=[]
            itemp.append(i*d1)
            itemp.append(j*d2)
            temp.append(itemp)
        coord.append(temp)

    pixels=[]                #would store the mid-point of each pixels
    for i in range(k):
        temp1=[]
        for j in range(k):
            iitemp=[]
            iitemp.append((coord[i][j][0]+coord[i][j+1][0])/2)
            iitemp.append((coord[i][j][1]+coord[i+1][j][1])/2)
            temp1.append(iitemp)

        pixels.append(temp1)
    map=[[0 for i in range(k)] for j in range(k)]
    for i in range(k):
        for j in range(k):
            arr=[]
            for l in range(N):
                x=abs(pixels[i][j][0]-loc[l][0])+abs(pixels[i][j][1]-loc[l][1])
                arr.append(x)
            minm=10000000000000000000
            p=0
            for m in range(len(arr)):
                if(arr[m]<=minm):
                    minm=arr[m]
                    p=m+1
            map[i][j]=p

    A=map
    A=np.matrix(A)
    cmap = plt.get_cmap('RdBu', np.max(A)-np.min(A)+1)
    mat = plt.matshow(A,cmap=cmap,vmin = np.min(A)-.5, vmax = np.max(A)+.5)
    #tell the colorbar to tick at integers
    plt.colorbar(mat, ticks=np.arange(np.min(A),np.max(A)+1))
    plt.title("Coverage of each EMS across the region")
    plt.show()
#printing the map in matrix form

    for i in range(k):
        temp=[]
        for j in range(k):
            temp.append(map[i][j])
        print temp
        print ""


    #finding avg time and proportion
    time=0.0
    prop=[0.0 for i in range(N)]
    for i in range(k):
        for j in range(k):
            for l in range(N):
                if(map[i][j]==l+1):
                    time=time+abs(loc[l][0]-pixels[i][j][0])+abs(loc[l][1]-pixels[i][j][1])
                    prop[l]=prop[l]+1.0
    for i in range(N):
        prop[i]=prop[i]/(k**2)
    time=time/(float)(k**2)
    print "Average time to service a call: ",time
    print "Proportion of Population served by each location: ",prop


    #computing distances b/w EMS locations and pixels
    distance=[]
    for l in range(N):
        temp=[]
        for i in range(k):
            for j in range(k):
                x=abs(loc[l][0]-pixels[i][j][0])+abs(loc[l][1]-pixels[i][j][1])
                temp.append(x)
        distance.append(temp)

    #solving the Optimisation Problem
    EMS=[0,1,2,3]
    xx=k**2
    value=[i for i in range(0,xx)]


    prob=LpProblem("Problem1",LpMinimize)
    x=LpVariable.dicts("x",(EMS,value), 0, 1, LpBinary)
    prob+= lpSum([[distance[i][j]*x[i][j] for j in range(xx)] for i in range(N)])
    for i in range(N):
        prob+= lpSum([x[i][j] for j in range(xx)])>=1
        prob+= lpSum([x[i][j] for j in range(xx)])<=((xx/N)+1)
    for j in range(xx):
        prob+= lpSum([x[i][j] for i in range(N)])<=1
        prob+= lpSum([x[i][j] for i in range(N)])>=1
    prob.solve(PULP_CBC_CMD(maxSeconds=500))
    print "Status: ",LpStatus[prob.status]
    for v in prob.variables():
        print "{}={}".format(v.name, v.varValue)
    final=[[0 for i in range(50)] for j in range(50)]
    for v in prob.variables():
        if(v.varValue==1):
                x=str(v.name)
                i=int(x[2])
                j=int(x[4:])
                h=int(math.floor(j/50))
                m=int(j%50)
                final[h][m]=i+1
    final1=final
    final1=np.matrix(final)
    cmap = plt.get_cmap('RdBu', np.max(final1)-np.min(final1)+1)
    mat = plt.matshow(final1,cmap=cmap,vmin = np.min(final1)-.5, vmax = np.max(final1)+.5)

    #tell the colorbar to tick at integers
    plt.colorbar(mat, ticks=np.arange(np.min(final1),np.max(final1)+1))
    plt.title("Modified distribution of coverage of EMS across the city")
    plt.show()

#finding new avg time and proportion

    ntime=0.0
    nprop=[0.0 for i in range(N)]
    for i in range(len(final)):
        for j in range(len(final[0])):
            for m in range(N):
                if(final[i][j]==(m+1)):
                    ntime=ntime+abs(loc[m][0]-pixels[i][j][0])+abs(loc[m][1]-pixels[i][j][1])
                    nprop[m]=nprop[m]+1.0

    for i in range(N):
        nprop[i]=nprop[i]/(float)(k**2)
    ntime=ntime/(float)(k**2)
    print "New Average time to service a call: ",ntime
    print "New Proportion of Population served by each location: ",nprop




main()
