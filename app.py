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
from tkinter import *
from hdpitkinter import HdpiTk
import psutil

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
	http_server_process = multiprocessing.Process(target=httpd,name='HTTPprocess')
	http_server_process.start()
	print("HTTPServer process started")

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
	ftp_server_process = multiprocessing.Process(target=ftpd,name='HTTPprocess')
	ftp_server_process.start()

def stop_ftp_button():
	global ftp_server_process
	ftp_server_process.terminate()
	print("FTPServer process terminated")


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

network_info = psutil.net_if_addrs()
network_list = []
interface_details = ""
for interface in network_info:
	temp_string = interface+" : "+network_info[interface][1][1] +"\n"
	interface_details = interface_details + temp_string
	network_list.append([interface,network_info[interface][1][1]])


IPAddr1=network_list[0][1]
#network_label = Entry(window, text=interface_details,  justify=RIGHT)

instruction_text = """
Accessing HTTP server in browser: http://%s:8000
Accessing FTP server:
Username: user123
Password: pass123
Port: 2121
Command in Linux: ftp %s 2121
""" % (IPAddr1,IPAddr1)


if __name__ == "__main__":
	################################
	##### Windows or Linux #########
	################################
	# change uncomment the appropriate build_for when building
	#build_for ="linux"
	build_for = "windows"
	if build_for == "linux":
		window = Tk()
	elif build_for == "windows":
		window = HdpiTk()
	window.title('Python Quick Network Tool - DJENGINEER')
	window.geometry("550x450")
	instruction_text_widget = Text(window, height=1, width=100)
	instruction_text_widget.tag_configure('tag-center', justify='center')
	instruction_text_widget.tag_configure('tag-right', justify='right')
	instruction_text_widget.tag_configure('tag-left', justify='left')
	instruction_text_widget.pack(fill='both', expand=True,padx=20, pady=20)
	instruction_text_widget.insert(END, interface_details,"tag-right")
	instruction_text_widget.insert(END, instruction_text)
	start_http = Button(window, text="start HTTP Server (port 8000)",command=start_http_button)
	stop_http = Button(window, text="stop HTTP Server",command=stop_http_button)
	start_ftp = Button(window, text="start FTP Server user123:pass123 port 2121",command=start_ftp_button)
	stop_ftp = Button(window, text="stop FTP server",command=stop_ftp_button)
	start_http.pack()
	stop_http.pack()
	start_ftp.pack()
	stop_ftp.pack()
	window.protocol("WM_DELETE_WINDOW", on_closing)
	window.mainloop()