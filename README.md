# python-quick-network-tool
python-quick-network-tool

Author: DJENGINEER

For when you need quick **HTTP** and **FTP** servers for file transfers. HTTP and FTP data transfers are not encrypted. Do not use if you require encryption.

The IP address in the second section may differ due to different number of network adapters or adapter names. If you are using for local network, then use your local network ip address, which may start with 192.168.\*\*\*.\*\*\*

![python quick network tool](https://github.com/djengineer/python-quick-network-tool/blob/main/screenshot.jpg?raw=true)



# Binaries
The tools are in the binaries folder. The windows binary may be flagged by anti-viruses as Trojan (AVG will do this). 

## v1.3 Binaries MD5 Checksum
py-quick-network-tool-ubuntu-64.bin: cef761af7a2b8784331632d670218a6e

py-quick-network-tool-win-64.exe: 75899def3fcd9eb78dc0903aa76d3840


# Running as script Windows or Linux

Uncomment "build_for" when building for windows or linux.
The difference is windows will use the https://pypi.org/project/hdpitkinter/ for proper scaling to avoid blur text. PSUTIL list sequence is also different when listing network interfaces

```python
# create Python3 virtual environment first.
pip install -r requirements.txt
python app.py

```

# Building from source
```python
pip install -r requirements.txt
pyinstaller -F --noconsole app.py -n py-quick-network-tool
pyinstaller -F --noconsole app.py --upx-dir=./upx-3.96-win64/upx.exe -n py-quick-network-tool
pyinstaller -F --noconsole app.py --upx-dir=./upx-3.96-amd64_linux/upx -n py-quick-network-tool

```

# Certificates
To generate your own certificate for HTTPS, use the following line.
```bash
# no passphrase
openssl req -nodes -new -x509  -keyout key.pem -out cert.pem
```

# DEV STATUS

Python script and binaries app.py works well in both windows and linux.




