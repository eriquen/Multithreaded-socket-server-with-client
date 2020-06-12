from socket import *
import threading
import datetime

class ClientThread(threading.Thread):
    def __init__(self, connect, address):
        threading.Thread.__init__(self)
        self.connectionSocket = connect
        self.addr = address

    def run(self):
        while True:
            try:
                message = connectionSocket.recv(2048)

                if not message:
                    break
                print("message: ")
                print(message)
                filename = message.split()[1]
                f = open(filename[1:])
                outputdata = f.read()
             
                now = datetime.datetime.now()
              
                first_header = "HTTP/1.1 200 OK"

                header_info = {
                    "Content-Length": len(outputdata),
                    "Keep-Alive": "timeout=%d,max=%d" % (10, 100),
                    "Connection": "Keep-Alive",
                    "Content-Type": "text/html"
                }

                following_header = "\r\n".join("%s: %s" % (
                    item, header_info[item]) for item in header_info)
                print "%s\r\n%s\r\n\r\n" % (first_header, following_header)
                self.connectionSocket.send(
                    "%s\r\n%s\r\n\r\n" % (first_header, following_header))
                self.connectionSocket.send("%s\r\n" % (outputdata))
                self.connectionSocket.close()
                print "Data sent, socket closed"

            except IOError:
      
                self.connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n")
                self.connectionSocket.close()

            break
     


serverSocket = socket(AF_INET, SOCK_STREAM)

serverPort = int(raw_input("Enter Port Number : "))
serverSocket.bind(('', serverPort))
serverSocket.listen(5)
threads = []
    
while True:
      
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print("addr:\n", addr)
      
    client_thread = ClientThread(connectionSocket, addr)
    client_thread.start()
    threads.append(client_thread)
	
serverSocket.close()
