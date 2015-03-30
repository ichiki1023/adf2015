from bottle import request, route, run

@route('/')
def getYo():
  username = request.query['username']
  print username
  return ""

run(host='localhost', port=8080, debug=True)
