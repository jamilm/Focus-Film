import numpy as np
from sklearn.svm import SVC
trainx = np.loadtxt(open("conFort.csv","rb"),delimiter=",")

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
trues = np.ones((332,1))
trainx = np.concatenate((l, a, b, d, g,t),axis=1)
#trainx = np.array(trainx)


trainx1 = np.loadtxt(open("reParse.csv","rb"),delimiter=",")

l = []
a = []
b = []
d = []
g = []
t = []

for i in range(0,356):
    l.append(trainx1[i*6])
    a.append(trainx1[i*6 + 1])
    b.append(trainx1[i*6+2])
    d.append(trainx1[i*6+3])
    g.append(trainx1[i*6+4])
    t.append(trainx1[i*6+5])
falses = np.zeros((356,1))
l = np.array(l)
a = np.array(a)
b = np.array(b)
d = np.array(d)
g = np.array(g)
t = np.array(t)

trainx1 = np.concatenate((l, a, b, d, g, t),axis=1)
#trainx = np.array(trainx)


X = np.concatenate((trainx, trainx1))
Y = np.concatenate((trues, falses))
