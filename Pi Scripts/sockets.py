import socket
import sys
import time
import datetime
import random

#define json format
Org      = "My organization"
Disp     = "Bluetooth example"                     # will be the label for the curve on the chart
GUID     = "nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn"  # ensures all the data from this sensor appears on the same chart. You can use the Tools/Create GUID in Visual Studio to create
Locn     = "here"
Measure  = "measure"
Units    = "units"


HOST = '127.0.0.1'   
PORT = 5000
CONNECT_RETRY_INTERVAL = 2

def connectSockets(gatewaySock):
  while gatewaySock == None:
      print "Connecting TCP"
      try:
          gatewaySock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
          gatewaySock.connect((HOST, PORT));
          print ("Connection to gateway succeeded")
      except socket.error as msg:
          gatewaySock = None
          print("Socket connection failed. Error Code : " + str(msg[0]) + " Message " + msg[1])
          time.sleep(CONNECT_RETRY_INTERVAL)
  return gatewaySock

###

s = None
s = connectSockets(s)

while True:
  timeStr = datetime.datetime.utcnow().isoformat()
  JSONdata = "{\"value\":"+ str(random.randrange(0, 100)) +",\"guid\":\""+GUID+"\",\"organization\":\""+Org+"\",\"displayname\":\""+Disp +"\",\"unitofmeasure\":\""+Units+"\",\"measurename\":\""+Measure+"\",\"location\":\""+Locn+"\",\"timecreated\":\""+timeStr+"\"}"
  wasExceptionOccured = 0
  try:
      # send to gateway over socket interface
      bytesNeedToBeSent = len(JSONdata)
      bytesSent = 0
      while(bytesSent < bytesNeedToBeSent):
        #send data 
        bytesSent = bytesSent + s.send("<" + JSONdata + ">")
      print(JSONdata) 
      # TODO check if all bytes sent. Sent again if necessary.
  except Exception as msg:
      print(msg[0])
      try: 
          s.close()
      except Exception as msg:
          print(msg[0])
      wasExceptionOccured = 1
      
  if (wasExceptionOccured == 1):
      # something went wrong, reconnect gateway socket
      s = None
      print "gateway socket exception occured"
      s = connectSockets(s)
              
  time.sleep(1)
        
# will never get here, unless server dies         
try: 
    s.close()
except Exception as msg:
# eat all exception and go back to connect loop 
    print(msg[0])
try: 
    bt.close()
except Exception as msg:
    # eat all exception and go back to connect loop 
    print(msg[0])