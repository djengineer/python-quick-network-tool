import pytest
import time
import os
import requests
from app import start_http_button,start_https_button,stop_http_button,start_ftp_button,start_ftps_button,stop_ftp_button
import ftplib
from ftplib import FTP,FTP_TLS

# create 100mb file for test
size = 100000000
with open("./BigTestFile.txt", "wb") as f:
    f.write(b" " * size)
with open("./SmallTestFile.txt", "wb") as f:
    f.write(b" " * 1000)
print("Temp files created for testing.")


url = 'http://127.0.0.1:8000'
https_url = 'https://127.0.0.1:8000'

class TestClassHTTP:
	"""
	HTTP status code tests
	"""
	def test_http(self):
		start_http_button()
		x = requests.get(url)
		stop_http_button()
		assert x.status_code == 200
	def test_https(self):
		start_https_button()
		x = requests.get(https_url, verify=False)
		stop_http_button()
		assert x.status_code == 200
	def test_small_file(self):
		start_http_button()
		x = requests.get(url+"/SmallTestFile.txt")
		stop_http_button()
		assert x.status_code == 200
	def test_big_file(self):
		start_http_button()
		x = requests.get(url+"/BigTestFile.txt")
		stop_http_button()
		assert x.status_code == 200

class TestClassFTP:
	def test_login(self):
		start_ftp_button()
		time.sleep(3)
		ftp = FTP()  # connect to host, default port
		ftp.connect('127.0.0.1',8021)
		result = ftp.login("user123","pass123")
		stop_ftp_button()
		assert result == "230 Login successful."
	def test_ftps_login(self):
		start_ftps_button()
		time.sleep(3)
		ftps = FTP_TLS()  # connect to host, default port
		ftps.connect('127.0.0.1',8021)
		result = ftps.login("user123","pass123")
		stop_ftp_button()
		assert result == "230 Login successful."
class TestClassTeardown:
	def test_teardown(self):		
		print("REMOVING FILES AND STOPPING SERVERS")
		os.remove("./BigTestFile.txt")
		os.remove("./SmallTestFile.txt")
		stop_http_button()
		stop_ftp_button()