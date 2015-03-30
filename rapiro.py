import serial
import time
com = serial.Serial('/dev/ttyAMA0', 57600, timeout = 10)

#コマンドの組み合わせ
# 前進
com.write("#M1")
time.sleep(5)
# 停止
com.write("#M0")
