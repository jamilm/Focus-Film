import numpy as np
from sklearn.svm import SVC
import warnings
#from sklearn.neighbors import KNeighborsClassifier
import win32com.client as comclt
warnings.filterwarnings("ignore")
trainx = np.loadtxt(open("conFort.csv","rb"),delimiter=",")
wsh= comclt.Dispatch("WScript.Shell")
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

clf = SVC()
clf.fit(X, np.ravel(Y)) 









import argparse
import time
import threading

from pythonosc import dispatcher
from pythonosc import osc_server

def initArrays():
  global a1, a2, a3, a4
  global b1, b2, b3, b4
  global d1, d2, d3, d4
  global t1, t2, t3, t4
  global g1, g2, g3, g4
  global l1, l2, l3, l4
  global c
  global count
  global timesCalled, lastSubmit
  count = 0
  timesCalled = 0
  a1 = []
  a2 = []
  a3 = []
  a4 = []
  b1 = []
  b2 = []
  b3 = []
  b4 = []
  d1 = []
  d2 = []
  d3 = []
  d4 = []
  g1 = []
  g2 = []
  g3 = []
  g4 = []
  t1 = []
  t2 = []
  t3 = []
  t4 = []
  l1 = []
  l2 = []
  l3 = []
  l4 = []
  c = []
  lastSubmit = time.time()
  serverRunning = False

def alphaData(*data):
  global a1, a2, a3, a4
  data = np.array(data)
  a1.append(data[1])
  a2.append(data[2])
  a3.append(data[3])
  a4.append(data[4])
  submitData()

def betaData(*data):
  global b1, b2, b3, b4
  data = np.array(data)
  b1.append(data[1])
  b2.append(data[2])
  b3.append(data[3])
  b4.append(data[4])
  submitData()

def deltaData(*data):
  global d1, d2, d3, d4
  data = np.array(data)
  d1.append(data[1])
  d2.append(data[2])
  d3.append(data[3])
  d4.append(data[4])
  submitData()

def thetaData(*data):
  global t1, t2, t3, t4
  data = np.array(data)
  t1.append(data[1])
  t2.append(data[2])
  t3.append(data[3])
  t4.append(data[4])
  submitData()

def gammaData(*data):
  global g1, g2, g3, g4
  data = np.array(data)
  g1.append(data[1])
  g2.append(data[2])
  g3.append(data[3])
  g4.append(data[4])
  submitData()


def lowData(*data):
  global l1, l2, l3, l4
  data = np.array(data)
  l1.append(data[1])
  l2.append(data[2])
  l3.append(data[3])
  l4.append(data[4])
  submitData()

def cData(*data):
  global c
  data = np.array(data)
  c.append(data[1])
  submitData()


def submitData():
  global lastSubmit
  global a1, a2, a3, a4
  global b1, b2, b3, b4
  global d1, d2, d3, d4
  global t1, t2, t3, t4
  global g1, g2, g3, g4
  global l1, l2, l3, l4
  global c
  global count
  if time.time() - lastSubmit > 1:
    lastSubmit = time.time()
    alpha = [np.mean(np.array(a1).astype(np.float)), np.mean(np.array(a2).astype(np.float)), np.mean(np.array(a3).astype(np.float)), np.mean(np.array(a4).astype(np.float))]
    beta = [np.mean(np.array(b1).astype(np.float)), np.mean(np.array(b2).astype(np.float)), np.mean(np.array(b3).astype(np.float)), np.mean(np.array(b4).astype(np.float))]
    delta = [np.mean(np.array(d1).astype(np.float)), np.mean(np.array(d2).astype(np.float)), np.mean(np.array(d3).astype(np.float)), np.mean(np.array(d4).astype(np.float))]
    theta = [np.mean(np.array(t1).astype(np.float)), np.mean(np.array(t2).astype(np.float)), np.mean(np.array(t3).astype(np.float)), np.mean(np.array(t4).astype(np.float))]
    gamma = [np.mean(np.array(g1).astype(np.float)), np.mean(np.array(g2).astype(np.float)), np.mean(np.array(g3).astype(np.float)), np.mean(np.array(g4).astype(np.float))]
    low = [np.mean(np.array(l1).astype(np.float)), np.mean(np.array(l2).astype(np.float)), np.mean(np.array(l3).astype(np.float)), np.mean(np.array(l4).astype(np.float))]
    xtest = np.concatenate((alpha, beta, delta, theta, gamma, low))
    x = clf.predict(xtest)[0]
    print(x)
    if (x > 0.5 and count < 10):
        while (count < 10):
            wsh.SendKeys("d")
            count = count + 1
    if (x < 0.5 and count > 0):
        wsh.SendKeys("s")
        count = count - 1
    #print("Channel 1-4")
    #print("Alpha:", alpha)
    #print("Beta:", beta)
    #print("Delta:", delta)
    #print("Theta:", theta)
    #print("Gamma:", gamma)
    #print("Low Freq:", low)
    #print()
    #print("")
    a1 = []
    a2 = []
    a3 = []
    a4 = []
    b1 = []
    b2 = []
    b3 = []
    b4 = []
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    g1 = []
    g2 = []
    g3 = []
    g4 = []
    t1 = []
    t2 = []
    t3 = []
    t4 = []
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    c = []

def endServer():
  global server
  server.shutdown()

def runMuseServer():
  global dispatcher, Dispatcher, server
  parser = argparse.ArgumentParser()
  parser.add_argument("--ip",
      default="localhost", help="The ip to listen on")
  parser.add_argument("--port",
      type=int, default=1337, help="The port to listen on")
  args = parser.parse_args()

  dispatcher = dispatcher.Dispatcher()
  dispatcher.map("/muse/elements/alpha_absolute", alphaData)
  dispatcher.map("/muse/elements/beta_absolute", betaData)
  dispatcher.map("/muse/elements/delta_absolute", deltaData)
  dispatcher.map("/muse/elements/theta_absolute", thetaData)
  dispatcher.map("/muse/elements/gamma_absolute", gammaData)
  dispatcher.map("/muse/elements/low_freqs_absolute", lowData)
  dispatcher.map("/muse/elements/experimental/concentration", cData)
  	
  server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server_thread = threading.Thread(target=server.serve_forever)
  server_thread.start()


initArrays()
runMuseServer()

