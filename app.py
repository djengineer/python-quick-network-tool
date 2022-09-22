from tkinter import *

import http.server
from http.server import BaseHTTPRequestHandler, HTTPServer
from http.server import HTTPServer, SimpleHTTPRequestHandler

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.servers import ThreadedFTPServer

import threading


def http_server_start(port):
	httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
	httpd.serve_forever()

def http_server_shutdown():
	httpd.shutdown()

def http_server_start(port):
	httpd = HTTPServer(('localhost', port), SimpleHTTPRequestHandler)
	httpd.serve_forever()

def http_server_shutdown():
	httpd.shutdown()

def ftp_server_start():
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', '.')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = ThreadedFTPServer(('', 2121), handler)
    server.serve_forever()

def ftp_server_shudtown():


window = Tk()
label = Label(window, text="I am a label widget")
start_http = Button(window, text="start Http port 8080",command=http_server_start)
stop_http = Button(window, text="stop http server",command=http_server_shutdown)


start_ftp = Button(window, text="start FTP server",command=ftp_server_start)
stop_ftp = Button(window, text="stop fto server",command=ftp_server_shutdown)


label.pack()
button.pack()
button2.pack()

if __name__ == "__main__":
	window.mainloop()