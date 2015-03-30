# -*- coding: utf-8 -*-
from bottle import request, route, run

import serial
import time
com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)

def walk():
  #コマンドの組み合わせ
  # 前進
  com.write("#M1")
  time.sleep(5)
  # 停止
  com.write("#M0")

@route('/')
def getYo():
  username = request.query['username']
  print username
  walk()
  return ""

run(host='localhost', port=8080, debug=True)
