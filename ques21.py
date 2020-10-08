import numpy
import matplotlib.pyplot as plt
wt=[]
for i in range(10**5):
        wt.append(numpy.random.gamma(16,0.75))
plt.hist(wt)
plt.xlabel("waiting times")
plt.ylabel("Frequencies of waititng time over 10^5 rounds")
plt.title("Frequency Distribution of waititng times of second patient")
plt.show()
