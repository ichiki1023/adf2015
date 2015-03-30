# -*- coding: utf-8 -*-
from bottle import request, route, run

from collections import deque
import serial
import time

import Queue

import threading

class WalkThread(threading.Thread):

  def __init__(self, q):
    super(WalkThread, self).__init__()
    self.queue = q

  def run(self):
    while True:
      n = self.queue.qsize()
      if n != 0:
        print n
        walkstop(n)
        while not self.queue.empty():
          self.queue.get()

def walkstop(sec):
  com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 1)
  com.write("#M1")
  time.sleep(sec)
  com.write("#M0")

def walk(sec):
  com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)
  com.write("#M1")
  time.sleep(sec)

def stop():
  com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)
  com.write("#M0")


queue = Queue.Queue()
thread = WalkThread(queue)
thread.start()

userdict = {}



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
  queue.put(username)

  # walkstop()
  # if username == "AMUTAKE":
  #   print "walk"
  #   walkstop()
  # else:
  #   print "stop"
  #   stop()
  return ""

run(host='localhost', port=8080, debug=True)
