from tkinter import *

import threading
import http.server
import socket 
from http.server import HTTPServer, SimpleHTTPRequestHandler, BaseHTTPRequestHandler
import http.server
import http.server
import os

import multiprocessing

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.servers import ThreadedFTPServer

import threading
web_dir = os.path.join(os.path.dirname(__file__), './')
os.chdir(web_dir)
class ThreadedHttpd (threading.Thread):
	def __init__(self, threadID, name, ):
		threading.Thread.__init__(self)
		self.threadID = threadID
		self.name = name
		self.start_status = False
	def run(self,server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
		server_address = ('', 8000)
		httpd = server_class(server_address, handler_class)
		httpd.serve_forever()
		
	def start_server(self):
		self.server_process = multiprocessing.Process(target=self.run())
		self.server_process.start()
	def shutdown(self):
		self.server_process.terminate()



def ftp_server_start():
    authorizer = DummyAuthorizer()
    authorizer.add_user('user', '12345', '.')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = ThreadedFTPServer(('', 2121), handler)
    server.serve_forever()



http_server = ThreadedHttpd(1, "Thread-1")

window = Tk()
label = Label(window, text="I am a label widget")
start_http = Button(window, text="start Http port 8080",command=lambda:http_server.start_server())
stop_http = Button(window, text="stop http server",command=lambda:http_server.shutdown())


#start_ftp = Button(window, text="start FTP server",command=ftp_server_start)
#stop_ftp = Button(window, text="stop fto server",command=ftp_server_shutdown)


label.pack()
start_http.pack()
stop_http.pack()

if __name__ == "__main__":
	window.mainloop()