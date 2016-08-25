## Hrishi Hiraskar
## 25 August 2016
import gevent
import gevent.monkey
import time
from gevent.pywsgi import WSGIServer
gevent.monkey.patch_all()

from flask import Flask, request, Response, render_template

app = Flask(__name__)

def event_stream():
    for count in range(32):
		#start sending timestamp
		if count < 31:
		    yield 'event: timestamp\ndata: %s\n\n' % int(round(time.time() * 1000))
			#wait for 2 secs
		    gevent.sleep(2)
		else:
			#stop sending data
			yield 'event: DONE\ndata: NA\n\n'
		
@app.route('/SendTime')
def sse_request():
	#set response method to event-stream
    return Response(
            event_stream(),
            mimetype='text/event-stream')

@app.route('/')
def page():
    return render_template('SendTime.html')

if __name__ == '__main__':
	#set server address 127.0.0.1:8080/
    http_server = WSGIServer(('127.0.0.1', 8001), app)
    http_server.serve_forever()

