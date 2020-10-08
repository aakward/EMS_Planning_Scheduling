import numpy
numpy.random.seed(1000)
Arr=[0,0]
for i in range(12,348,12):
        Arr.append(i)
avg_wt=[]
avg_id=[]

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
print "the average total waiting time of all 30 patients is ",sum(avg_wt)/len(avg_wt),"minutes"
print "the average idle time of a practitioner in a day is ",sum(avg_id)/len(avg_id)," minutes"
