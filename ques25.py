import numpy
import matplotlib.pyplot as plt
numpy.random.seed(1000)
mu=3.0
for z in range(2):
        if z==0:
                Arr=[0,0]
                c=len(Arr)
                i=12
                while c<30:
                        Arr.append(i)
                        i=i+12
                        c=c+1
        else:
                iat=[]
                i=5.95
                while i<28:
                        iat.append(i)
                        i=i+2
                Arr=[0]
                for j in range(4):
                        Arr.append(Arr[j]+iat[j])
                c=len(Arr)
                i=Arr[len(Arr)-1]+12
                k=0
                while c<30:
                        Arr.append(i)
                        i=i+12
                        c=c+1
                        k=k+1

        print len(Arr)
        avg_wt=[]
        avg_id=[]
        print "Arrivals=",Arr
        for k in range(10**5):
                Wt=[0.0 for i in range(len(Arr))]
                id=[0.0 for i in range(len(Arr))]
                cst=0.0
                for  i in range(len(Arr)):
                        s=numpy.random.gamma(16,0.75)
                        if cst>Arr[i]:
                                Wt[i]=cst-Arr[i]
                                cst=cst+s
                        if cst<Arr[i]:
                                id[i]=Arr[i]-cst
                                cst=Arr[i]+s
                        if i==0:
                                cst=s
                avg_wt.append(sum(Wt))
                avg_id.append(sum(id))
        if z==0:
                print "we have the following from bailey welch rule:"
        else:
                print "modified rule gives us:"
        print "the average total waiting time of all 30 patients is ",sum(avg_wt)/len(avg_wt),"minutes"
        print "the average idle time of a practitioner in a day is ",sum(avg_id)/len(avg_id)," minutes"

