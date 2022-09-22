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
global http_server_process
global ftp_server_process

def httpd(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler):
	server_address = ('', 8000)
	httpd = server_class(server_address, handler_class)
	httpd.serve_forever()

def start_http_button():
	global http_server_process
	print(1)
	http_server_process = multiprocessing.Process(target=httpd)
	print(2)
	http_server_process.start()
	print(3)

def stop_http_button():
	global http_server_process
	http_server_process.terminate()
	print("HTTPServer process terminated")



def ftpd():
    authorizer = DummyAuthorizer()
    authorizer.add_user('user123', 'pass123', '.')
    handler = FTPHandler
    handler.authorizer = authorizer
    server = ThreadedFTPServer(('', 2121), handler)
    server.serve_forever()


def start_ftp_button():
	global ftp_server_process
	print(1)
	ftp_server_process = multiprocessing.Process(target=ftpd)
	print(2)
	ftp_server_process.start()
	print(3)

def stop_ftp_button():
	global ftp_server_process
	ftp_server_process.terminate()
	print("FTPServer process terminated")




window = Tk()
label = Label(window, text="I am a label widget")
start_http = Button(window, text="start Http port 8080",command=lambda:start_http_button())
stop_http = Button(window, text="stop http server",command=lambda:stop_http_button())

start_ftp = Button(window, text="start ftp server user123:pass123 port 2121",command=lambda:start_ftp_button())
stop_ftp = Button(window, text="stop http server",command=lambda:stop_ftp_button())


#start_ftp = Button(window, text="start FTP server",command=ftp_server_start)
#stop_ftp = Button(window, text="stop fto server",command=ftp_server_shutdown)


label.pack()
start_http.pack()
stop_http.pack()
start_ftp.pack()
stop_ftp.pack()

if __name__ == "__main__":
	window.mainloop()