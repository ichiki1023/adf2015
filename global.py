# coding:utf-8
import cgi,urllib

total = 0

def check():
	global total
	total += 1#total++は出来なかったです

check()
print total
