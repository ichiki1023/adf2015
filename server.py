# -*- coding: utf-8 -*-
from bottle import request, route, run

import serial
import time

userdict = {}

def newCom():
  return

def walk():
  com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)
  com.write("#M1")

def stop():
  com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)
  com.write("#M0")

def walkstop():
  com = serial.Serial('/dev/ttyAMA0', 57600) # , timeout = 1)
  com.write("#M1")
  time.sleep(1)
  com.write("#M0")

@route('/')
def getYo():
  username = request.query['username']
  print username
  
  if userdict.get(username) == None:
    userdict[username] = 1
  else:
    userdict[username] = userdict[username] + 1

  print username + ': ' + str(userdict[username])
  # print len(userdict)
  # print 'total: ' + str(

  walkstop()
  # if username == "AMUTAKE":
  #   print "walk"
  #   walkstop()
  # else:
  #   print "stop"
  #   stop()
  return ""

run(host='localhost', port=8080, debug=True)
