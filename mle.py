import numpy as np

trainx = np.loadtxt(open("conFort.csv","rb"),delimiter=",",skiprows=1)
print(trainx.shape)

l = []
a = []
b = []
d = []
g = []
t = []

for i in range(332):
    l.append(trainx[i*6])
    a.append(trainx[i*6 + 1])
    b.append(trainx[i*6+2])
    d.append(trainx[i*6+3])
    g.append(trainx[i*6+4])
    t.append(trainx[i*6+5])
l = np.array(l)
a = np.array(a)
b = np.array(b)
d = np.array(d)
g = np.array(g)
t = np.array(t)
trainx = np.concatenate((t, l, a, b, d, g),axis=1)
#trainx = np.array(trainx)
print(trainx)
