# python-quick-network-tool
python-quick-network-tool

Author: DJENGINEER

For when you need quick **HTTP** and **FTP** servers for file transfers. HTTP and FTP data transfers are not encrypted. Do not use if you require encryption.

HTTPS and SFTP is available from V1.2.2. Do not use on production servers.

The IP address in the second section may differ due to different number of network adapters or adapter names. If you are using for local network, then use your local network ip address, which may start with 192.168.\*\*\*.\*\*\*

### Regarding HTTPS and SFTP
If you run HTTPS server instead of HTTP, specify **https://** when accessing the url like this **https://[ip_address]:8000**.

If you run TLS/SSL enabled HTTP and FTP, your browser and FTP client may show a certificate warning. You may accept the warning and proceed with the connection.

![python quick network tool](https://github.com/djengineer/python-quick-network-tool/blob/main/screenshot%20v1.2.3.jpg?raw=true)



# Binaries
The tools are in the binaries folder. The windows binary may be flagged by anti-viruses as Trojan (AVG will do this). From V1.2.2, the binaries are properly packed with UPX. Windows may give a warning running an unknown .exe file. 

## v1.2.3 Binaries MD5 Checksum

py-quick-network-tool-ubuntu-64-v-1-2-3.bin: f7a03549cbe79fb7759f031303002ca7
py-quick-network-tool-win-64-v-1-2-3.exe: 9366aa5b7bfd7c5765c2ce41d759543a

## v1.2.2 Binaries MD5 Checksum
py-quick-network-tool-ubuntu-64-v-1-2-2.bin: 92d5c2d69462696fc6ce5738d858528e

py-quick-network-tool-win-64-v-1-2-2.exe: 968ee1b952db4664c55479d3357f6150


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
pyinstaller -F --noconsole app.py --upx-dir="./upx-3.96-win64/" -n py-quick-network-tool
pyinstaller -F --noconsole app.py --upx-dir="./upx-3.96-amd64_linux/" -n py-quick-network-tool

```

# Certificates
## HTTPS
To generate your own certificate for HTTPS, use the following line.
```bash
# no passphrase
openssl req -nodes -new -x509  -keyout key.pem -out cert.pem
```
## Certificate for pyftpd 
https://pyftpdlib.readthedocs.io/en/latest/tutorial.html#ftps-ftp-over-tls-ssl-server

We use the demo certificate referenced in the documentation. https://github.com/giampaolo/pyftpdlib/blob/master/demo/keycert.pem

If you want to create a new certificate, use the following commands.

```bash
# combining both private key and certificate into one pem file
openssl req -nodes -new -x509  -keyout key.pem -out cert.pem
cat cert.pem key.pem > server.includesprivatekey.pem
# change the name to the appropriate ftp cert name in the codes
```

# DEV STATUS

Python script and binaries app.py works well in both windows and linux.




