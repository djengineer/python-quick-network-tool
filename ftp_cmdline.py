import threading
import socket 
import multiprocessing
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.handlers import TLS_FTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.servers import ThreadedFTPServer
import psutil
import threading
import ssl
import sys, os

ftp_username=""
ftp_pass=""

global application_path

if getattr(sys, 'frozen', False):
	# If the application is run as a bundle, the PyInstaller bootloader
	# extends the sys module by a flag frozen=True and sets the app 
	# path into variable _MEIPASS'.
	#application_path = sys._MEIPASS
	application_path = os.path.dirname(sys.executable)
else:
	application_path = os.path.dirname(os.path.abspath(__file__))

global certdir
if hasattr(sys, "_MEIPASS"):
	# this is for pyinstaller's bundled file
    base_dir = os.path.abspath(os.path.dirname(__file__))
else:
	# if this is not for bundled file, just for the script
    base_dir = './'

def ftpd():
    authorizer = DummyAuthorizer()
    authorizer.add_user(ftp_username, ftp_pass, '.', perm='elradfmwMT')
    handler = FTPHandler
    #handler = TLS_FTPHandler
    #handler.certfile = 'keycert.pem'
    handler.authorizer = authorizer
    server = ThreadedFTPServer(('0.0.0.0', 8021), handler)
    server.serve_forever()

def ftpsd():
    authorizer = DummyAuthorizer()
    authorizer.add_user(ftp_username, ftp_pass, '.', perm='elradfmwMT')
    handler = TLS_FTPHandler
    handler.certfile = base_dir + '/certificates/keycert_ftp.pem'
    handler.authorizer = authorizer
    # requires SSL for both control and data channel
    handler.tls_control_required = True
    handler.tls_data_required = True
    server = ThreadedFTPServer(('0.0.0.0', 8021), handler)
    server.serve_forever()

if __name__ == "__main__":
    ftpsd()