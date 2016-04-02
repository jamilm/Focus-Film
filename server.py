import argparse
import math
import time
import threading
import os
import numpy as np

from pythonosc import dispatcher
from pythonosc import osc_server

def initArrays():
  global a1, a2, a3, a4
  global b1, b2, b3, b4
  global d1, d2, d3, d4
  global t1, t2, t3, t4
  global g1, g2, g3, g4
  global l1, l2, l3, l4
  
  global timesCalled, lastSubmit
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

def submitData():
  global lastSubmit
  global a1, a2, a3, a4
  global b1, b2, b3, b4
  global d1, d2, d3, d4
  global t1, t2, t3, t4
  global g1, g2, g3, g4
  global l1, l2, l3, l4
  
  if time.time() - lastSubmit > 1:
    lastSubmit = time.time()
    print("Channel 1-4")
    print("Alpha:", np.mean(np.array(a1).astype(np.float)), np.mean(np.array(a2).astype(np.float)), np.mean(np.array(a3).astype(np.float)), np.mean(np.array(a4).astype(np.float)))
    print("Beta:", np.mean(np.array(b1).astype(np.float)), np.mean(np.array(b2).astype(np.float)), np.mean(np.array(b3).astype(np.float)), np.mean(np.array(b4).astype(np.float)))
    print("Delta:", np.mean(np.array(d1).astype(np.float)), np.mean(np.array(d2).astype(np.float)), np.mean(np.array(d3).astype(np.float)), np.mean(np.array(d4).astype(np.float)))
    print("Theta:", np.mean(np.array(t1).astype(np.float)), np.mean(np.array(t2).astype(np.float)), np.mean(np.array(t3).astype(np.float)), np.mean(np.array(t4).astype(np.float)))
    print("Gamma:", np.mean(np.array(g1).astype(np.float)), np.mean(np.array(g2).astype(np.float)), np.mean(np.array(g3).astype(np.float)), np.mean(np.array(g4).astype(np.float)))
    print("Low Freq:", np.mean(np.array(l1).astype(np.float)), np.mean(np.array(l2).astype(np.float)), np.mean(np.array(l3).astype(np.float)), np.mean(np.array(l4).astype(np.float)))
    print("")
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
  	
  server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server_thread = threading.Thread(target=server.serve_forever)
  server_thread.start()


initArrays()
runMuseServer()


