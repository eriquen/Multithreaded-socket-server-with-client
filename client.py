from socket import *
import sys


server_port = int(raw_input("Port Number:"))
filename = raw_input("Search here:")
server_host = "127.0.0.1"
# server_port = 8080
host_port = "%s:%s" % (server_host, server_port)
print '\n\n'
try:
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_host, int(server_port)))
    header = {
        "first_header": "GET /%s HTTP/1.1" % (filename),
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Language": "en-us",
        "Host": host_port,
    }
    http_header = "\r\n".join("%s:%s" % (
        item, header[item]) for item in header)
    print http_header
    client_socket.send("%s\r\n\r\n" % (http_header))

    final = ""
    response_message = client_socket.recv(2048)
    print response_message
    while response_message:
        if "HTTP/1.1 404 Not Found\r\n\r\n" in response_message:
            final = "File Not Found !!!"
            break
    
        response_message = client_socket.recv(1024)
        final += response_message
        break

    client_socket.close()
    print "final:\n", final

except IOError:
    sys.exit(1)
