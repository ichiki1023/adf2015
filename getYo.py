import cgi,sys,os,urllib

#Yo！をしたユーザ名を保持
yo_list = []

form = cgi.FieldStorage()

#form.has_key("name").

username = form["username"].value

#まだYoをされていないなら
if username not in yo_list:
	#グローバル変数に格納

	if len(yo_list) >= 30:
		#目標達成(終了)
		yoAll("923474be-cde0-4ab1-a84f-171b4e78e821")
		#rapiro.py


def yoAll(apitokenvalue):
  url = "http://api.justyo.co/yoall/"
  reqdata[] = {}
  reqdata{'api_token'] = apitokenvalue
  params = urllib.urlencode(reqdata)
  urllib.urlopen("http://api.justyo.co/yoall",params)

