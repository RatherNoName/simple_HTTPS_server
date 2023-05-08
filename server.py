import http.server, ssl

#server_address = ('127.0.0.1', 4443) #localhost directly
server_address = ('', 4443) #this is local IP of computer
httpd = http.server.HTTPServer(server_address, http.server.SimpleHTTPRequestHandler)
#httpd.socket = ssl.wrap_socket(httpd.socket, #uncomment this to get https
#                               server_side=True,
#                               certfile='localhost.pem',
#                               ssl_version=ssl.PROTOCOL_TLS)
httpd.serve_forever()