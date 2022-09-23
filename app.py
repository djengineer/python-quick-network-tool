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

from tkinter import messagebox

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
window.geometry("400x200")

hostname=socket.gethostname()   
IPAddr=socket.gethostbyname(hostname + ".local") 
print("Your Computer Name is:"+hostname)   
print("Your Computer IP Address is:"+IPAddr)   
ip_label = Label(window, text="Your IP Address is: %s"%IPAddr)

instruction_text = """
Accessing HTTP server in browser: http://%s:8000

"""

instruction_label = Label(window, text="Accessing HTTP server in browser: http://%s:8000\n")

start_http = Button(window, text="start HTTP Server (port 8000)",command=lambda:start_http_button())
stop_http = Button(window, text="stop HTTP Server",command=lambda:stop_http_button())

start_ftp = Button(window, text="start FTP Server user123:pass123 port 2121",command=lambda:start_ftp_button())
stop_ftp = Button(window, text="stop FTP server",command=lambda:stop_ftp_button())


def on_closing():
	global http_server_process
	global ftp_server_process
	if messagebox.askokcancel("Quit", "Do you want to close all services and quit?"):
		try:
			http_server_process.terminate()
		except NameError:
			# if no server process, skip. NameError if server process not started
			pass

		try:
			ftp_server_process.terminate()
		except NameError:
			# if no server process, skip. NameError if server process not started
			pass
		window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)

#start_ftp = Button(window, text="start FTP server",command=ftp_server_start)
#stop_ftp = Button(window, text="stop fto server",command=ftp_server_shutdown)

ip_label.pack()
instruction_label.pack()
start_http.pack()
stop_http.pack()
start_ftp.pack()
stop_ftp.pack()

if __name__ == "__main__":
	window.mainloop()