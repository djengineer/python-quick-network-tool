#!/bin/bash
openssl req -nodes -new -x509  -keyout ./certificates/key.pem -out ./certificates/cert.pem
cat ./certificates/cert.pem ./certificates/key.pem > ./certificates/keycert_ftp.pem