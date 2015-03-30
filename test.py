# coding:utf-8
import cgi,urllib

def yoAll(apitokenvalue):
  	reqdata = {}
	reqdata['api_token'] = apitokenvalue#YoのAPI_token
	params = urllib.urlencode(reqdata)
	urllib.urlopen("http://api.justyo.co/yoall/",params)

yoAll("923474be-cde0-4ab1-a84f-171b4e78e821")
