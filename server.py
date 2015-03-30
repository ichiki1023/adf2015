# -*- coding: utf-8 -*-
from bottle import request, route, run

from collections import deque
import serial
import time

import Queue

import threading

userdict = {}
total = 0


import cgi,urllib

def yoAll(apitokenvalue):
  reqdata = {}
  reqdata['api_token'] = apitokenvalue # YoのAPI_token
  params = urllib.urlencode(reqdata)
  urllib.urlopen("http://api.justyo.co/yoall/",params)




@route('/')
def getYo():
  global total
  username = request.query['username']
  print username

  if userdict.get(username) == None:
    userdict[username] = 1
  else:
    userdict[username] = userdict[username] + 1

  print username + ': ' + str(userdict[username])
  # print len(userdict)
  # print 'total: ' + str(
  total += 1
  if total == 1:
    com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 0)
    com.write("#M1")

  if total == 50:
    yoAll("3e54a635-8751-4c7f-a668-c307d6e0636c")
    com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 0)
    com.write("#M5")

  if username == "AMUTAKE":
    com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 0)
    com.write("#M0")
    

  # walkstop()
  # if username == "AMUTAKE":
  #   print "walk"
  #   walkstop()
  # else:
  #   print "stop"
  #   stop()
  return ""

run(host='localhost', port=8080, debug=True)
