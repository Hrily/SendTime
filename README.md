# SendTime - Python 
Python Server that sends client the server time every two second for a minute, using Server Sent Events


###Server does following process:
  + On request from client, start sending server time to client
  + Repeat this for every two seconds 
  + After one minute, stop sending the time
  + The client which sent the request only should recieve the time, not all clients

	Server Side : Python 

	Client Side : JavaScript

To run server, goto the SendTime directory and type:
 
 `python SendTime.py`
 
Then goto [127.0.0.1:8001](127.0.0.1:8001) in browser
