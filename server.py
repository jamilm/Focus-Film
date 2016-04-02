import argparse
import math
import time
import threading
import os
import numpy as np

from pythonosc import dispatcher
from pythonosc import osc_server

def initArrays():
  global alphaArray, betaArray, deltaArray, thetaArray, concentrationArray
  global timesCalled, lastSubmit
  timesCalled = 0
  alphaArray = []
  betaArray = []
  thetaArray = []
  deltaArray = []
  concentrationArray = []
  lastSubmit = time.time()
  serverRunning = False

def getAverage(*nums):
  total = 0
  nums = list(nums)
  for i in range(len(nums[0])):
    if i>0:
      total += float(nums[0][i])
  total = total/4
  return total

def arrayAverage(array):
  total = 0
  for i in array:
    total += i
  return total/(len(array))

def alphaData(*data):
  print(np.array(data))

def betaData(*data):
    print(data)

def deltaData(*data):
    print(data)

def thetaData(*data):
    print(data)

def concentrationData(*data):
    print(data)
    
def submitData():
  global lastSubmit, alphaArray, betaArray, deltaArray, thetaArray, concentrationArray
  if time.time() - lastSubmit > 3:
    lastSubmit = time.time()
    avgArray = [arrayAverage(alphaArray), arrayAverage(betaArray), arrayAverage(deltaArray), arrayAverage(thetaArray), arrayAverage(concentrationArray)]
    print(avgArray)
    alphaArray = []
    betaArray = []
    thetaArray = []
    deltaArray = []
    concentrationData = []

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
  dispatcher.map("/muse/elements/gamma_absolute", concentrationData)
  	
  server = osc_server.ThreadingOSCUDPServer((args.ip, args.port), dispatcher)
  print("Serving on {}".format(server.server_address))
  server_thread = threading.Thread(target=server.serve_forever)
  server_thread.start()


initArrays()
runMuseServer()


