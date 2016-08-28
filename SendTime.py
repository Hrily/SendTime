## Hrishi Hiraskar
## 25 August 2016

import gevent
import time
from gevent import monkey
from gevent.pywsgi import WSGIServer
from flask import Flask, request, Response, render_template

monkey.patch_all()

app = Flask(__name__)

def event_stream():
	for count in range(31):
		# Start sending timestamp
		yield 'event: timestamp\ndata: %s\n\n' % int(round(time.time() * 1000))
		# Wait for 2 secs
		gevent.sleep(2)
		if count==30:
			# Stop sending data
			yield 'event: DONE\ndata: NA\n\n'
		
@app.route('/SendTime')
def sse_request():
	# Set response method to event-stream
	return Response(event_stream(), mimetype='text/event-stream')

@app.route('/')
def page():
	return render_template('index.html')

if __name__ == '__main__':
	# Set server address 127.0.0.1:8080/
	http_server = WSGIServer(('127.0.0.1', 8001), app)
	http_server.serve_forever()

