#!/bin/bash

echo '1. upgrade yum'
yum upgrade

echo '2. install wget'
yum install wget

echo '3. install shadowsocks'
wget --no-check-certificate https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks.sh
chmod +x shadowsocks.sh
./shadowsocks.sh 2>&1 | tee shadowsocks.log
