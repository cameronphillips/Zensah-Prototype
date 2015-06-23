import socket
import sys
import time
import datetime
import random 

#define json format
Org      = "Zensah"
Disp     = "Dummy X"                     # will be the label for the curve on the chart
GUID     = "nnnnnnnn-nnnn-nnnn-nnnn-nnnnnnnnnnnn"  # ensures all the data from this sensor appears on the same chart. You can use the Tools/Create GUID in Visual Studio to create
Locn     = "here"
Measure  = "measure"
Units    = "units"

#Communication takes place via a socket to the Mono C# gateway service
HOST = '127.0.0.1'   
PORT = 5000
CONNECT_RETRY_INTERVAL = 2
EXCEPTION_THRESHOLD    = 3
SEND_INTERVAL          = 1

while 1:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created.")

    while 1:
        try:
            s.connect((HOST, PORT));
            break;
        except socket.error as msg:
            print("Socket connection failed. Error Code : " + str(msg[0]) + " Message " + msg[1])
            time.sleep(CONNECT_RETRY_INTERVAL)
     
    print ("Socket connection succeeded.")

    exceptions_count = 0
    while 1:
        timeStr = datetime.datetime.utcnow().isoformat()


        ##Insert code to retrieve data from device##
        #Currently using dummy data#
        #dummy = random.randint(0, 100)
        #print str(dummy)

        dummy = "blah"

        try:
            JSONdata = "{\"value\":"+dummy+",\"guid\":\""+GUID+"\",\"organization\":\""+Org+"\",\"displayname\":\""+Disp +"\",\"unitofmeasure\":\""+Units+"\",\"measurename\":\""+Measure+"\",\"location\":\""+Locn+"\",\"timecreated\":\""+timeStr+"\"}"            
            print(sys.getsizeof(JSONdata))
            s.send("<" + JSONdata + ">");                  # sends to gateway over socket interface
            print(JSONdata)
        except Exception as msg:
            exceptions_count += 1
            print(msg[0])
            # if we get too many exceptions, we assume the server is dead
            # we will ignore the casual exception

            if exceptions_count > EXCEPTION_THRESHOLD:
                break 
            else:
                continue

        print("sleeping for" + str(SEND_INTERVAL))
        time.sleep(SEND_INTERVAL)
    
    # will never get here, unless server dies         
    try: 
        s.close()
    except Exception as msg:
        # eat all exception and go back to connect loop 
        print(msg[0])