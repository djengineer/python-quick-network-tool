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
The tools are in the binaries folder. The windows binary may be flagged by anti-viruses as Trojan (AVG will do this). From V1.2.2, the binaries are properly packed with UPX. Windows may give a warning when running an unknown .exe file. 

## v1.2.4 Binaries MD5 Checksum

py-quick-network-tool-ubuntu-64-v1-2-4.bin: 4c189899b24bb86ec5b4d4af1e9ca856
py-quick-network-tool-win-64-v1-2-4.exe: f2fc04441ca82bd06ad55a51e2f94a8c

## v1.2.3 Binaries MD5 Checksum

py-quick-network-tool-ubuntu-64-v1-2-3.bin: 1deef0e2afb77f27a9f782df7e20e287
py-quick-network-tool-win-64-v1-2-3.exe: 4c3dce6e998d4d4c142989b142f12a06

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

Use py-quick-network-tool.spec where possible. Ensure certificates folder are added correctly

```python
pip install -r requirements.txt

pyinstaller py-quick-network-tool.spec --upx-dir="./upx-3.96-win64/"
pyinstaller py-quick-network-tool.spec --upx-dir="./upx-3.96-amd64_linux/"

# running these will change the spec files
pyinstaller -F --noconsole --add-data './certificates':'/certificates' app.py -n py-quick-network-tool
pyinstaller -F --noconsole --add-data './certificates':'/certificates' app.py --upx-dir="./upx-3.96-win64/" -n py-quick-network-tool
pyinstaller -F --noconsole --add-data './certificates':'/certificates' app.py --upx-dir="./upx-3.96-amd64_linux/" -n py-quick-network-tool

```

### To compile the FTP Commandline py file
```python
pip install -r requirements.txt

pyinstaller py-ftp-cmdline.spec --upx-dir="./upx-3.96-win64/"
pyinstaller py-ftp-cmdline.spec --upx-dir="./upx-3.96-amd64_linux/"

# running these will change the spec files
pyinstaller -F --noconsole --add-data './certificates':'/certificates' ftp_cmdline.py --upx-dir="./upx-3.96-win64/" -n py-ftp-cmdline
pyinstaller -F --noconsole --add-data './certificates':'/certificates' ftp_cmdline.py --upx-dir="./upx-3.96-amd64_linux/" -n py-ftp-cmdline

```

# Building notes

[Linux] Current binary(v1.2.4) is compiled with GLIBC 2.35. New Ubuntu releases(2023) features GLIBC 2.36 and above.

If spec file is corrupted or accidentally replaced, we need to add certificate files into the build in the spec file
```
block_cipher = None

added_files = [
    ('./certificates', '/certificates'),
    ]

a = Analysis(
    ['app.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    ...,
    ...
```
## If using pyenv for python, we need to share resources with OS
For ubuntu:
```
env PYTHON_CONFIGURE_OPTS="--enable-shared" pyenv install 3.10.6
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
cat cert.pem key.pem > keycert_ftp.pem
# change the name to the appropriate ftp cert name in the codes
```

We can use the `gen_new_cert.sh` instead to do it for us automatically.
This will run the above 2 commands to update the FTP and HTTPS certificates.

# Compatibility

- Python 3.10.6
- Does not work with Python >= 3.11.0
- V1.2.4 Linux binary compiled with GLIBC 2.35. You can check your version with `ldd --version`

# Deploying on Cloud

For fast FTP to use in a cloud environment, use the ftp_cmdline.py script/binary.
Set up the venv, and `pip install -r requirements.txt` as usual.

In the FTP script, and app.py, FTP has `handler.passive_ports = range(60000, 65535)`
We can simply reduce it to `handler.passive_ports = range(60000, 60001)` and open a TCP port `60000` inbound rule in Security Group settings.

We could just open from 60000 to 65535, but it is bad security to open so many unused ports.





