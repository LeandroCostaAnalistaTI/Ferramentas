#!/bin/bash

echo "=============================="
echo " INSTALAÇÃO DE FERRAMENTAS"
echo "=============================="
echo "=============================="

cd /home
# INSTALANDO PYTHON
apt update
apt-get install wget
apt-get install unzip
apt-get install python3
apt-get install python
apt-get install python2

#INSTALANDO PIP

apt-get install python3-pip

# INSTALANDO GO

apt update --fix-missing
apt install golang
#export GOPATH=$GOPATH/bin/gopath

# INSTALANDO SNAP

apt install snapd

# INSTALANDO GIT

dpkg --configure -a
apt --fix-broken install
apt install git


# INSTALANDO NMAP

apt install nmap

# INSTALANDO WHOIS

apt-get install whois

# INSTALANDO DIRB

apt install dirb

# INSTALANDO DIG

apt install dnsutils

# INSTALANDO METAGOOFIL
apt install metagoofil

# INSTALANDO  WAFW00F

apt-get update -y
apt-get install -y wafw00f

# INSTALANDO SUBFINDER

wget https://github.com/projectdiscovery/subfinder/releases/download/v2.4.9/subfinder_2.4.9_linux_amd64.zip
unzip subfinder_2.4.9_linux_amd64.zip
mv subfinder /usr/bin/

# INSTALANDO ASSETFINDER

go get -u github.com/tomnomnom/assetfinder
mv /root/go/bin/assetfinder  /usr/bin/

# INSTALANDO HTTPX
apt install unzip
wget https://github.com/projectdiscovery/httpx/releases/download/v1.1.3/httpx_1.1.3_linux_amd64.zip
unzip httpx_1.1.3_linux_amd64.zip
mv httpx /usr/bin/

# INSTALANDO GAUPLUS

GO111MODULE=on go get -u -v github.com/bp0lr/gauplus
mv /root/go/bin/gauplus  /usr/bin/

# INSTALANDO wget THEHARVESTER

apt-get install theharvester


# INSTALANDO NUCLEI

wget https://github.com/projectdiscovery/nuclei/releases/download/v2.5.3/nuclei_2.5.3_linux_amd64.zip
unzip nuclei_2.5.3_linux_amd64.zip
mv nuclei /usr/bin/
nuclei  -update-templates

# INSTALANDO JAELES

GO111MODULE=on go get github.com/jaeles-project/jaeles
mv /root/go/bin/jaeles  /usr/bin/
git clone --depth=1 https://github.com/jaeles-project/jaeles-signatures /tmp/jaeles-signatures/
jaeles config -a reload --signDir /tmp/jaeles-signatures

# INSTALANDO DALFOX

wget https://github.com/hahwul/dalfox/releases/download/v2.5.4/dalfox_2.5.4_linux_amd64.tar.gz
tar xvfz dalfox_2.5.4_linux_amd64.tar.gz
mv dalfox /usr/bin/

# INSTALANDO SUBLIST3R
cd /home
git clone https://github.com/aboul3la/Sublist3r.git
cd Sublist3r
pip install -r requirements.txt
apt-get install python-dnspython
pip install dnspython
apt-get install python-argparse
pip install argparse


# INSTALANDO DNSMAP

apt-get install dnsmap

# INSTALANDO DNSRECON

apt install dnsrecon

# INSTALANDO CTFR
cd /home
git clone https://github.com/UnaPibaGeek/ctfr.git
cd ctfr
pip3 install -r requirements.txt

# SSLYZE
pip install --upgrade setuptools pip
pip install --upgrade sslyze

# SCRIPT nse-log4shell
cd /home
git clone https://github.com/Diverto/nse-log4shell.git
cd nse-log4shell
mv http-log4shell.nse imap-log4shell.nse ssh-log4shell.nse ftp-log4shell.nse http-spider-log4shell.nse smtp-log4shell.nse /usr/share/nmap/scripts/
cd ..
rm -rf nse-log4shell


# INSTALANDO  URLCRAZY
apt install urlcrazy
apt install ruby
gem install bundler
gem install json colorize async async-dns async-http
apt-get install ruby-full

# Nikito

apt install nikto

# whatweb

apt install whatweb

# DNSTWIST

apt install dnstwist

# INSTALANDO AMASS
cd /home
wget https://github.com/OWASP/Amass/releases/download/v3.15.0/amass_linux_amd64.zip
unzip amass_linux_amd64.zip
mv amass_linux_amd64 amass
cd amass
mv amass /usr/bin/

#  enum4linux

 apt install enum4linux

 # Gobuste

 apt install gobuster

 # exploitdb

 apt install exploitdb

 # SHCHECK
 
apt install python3 python3-pip
pip3 install shcheck


 # wordlist
 cd /home
 mkdir wordlist
git clone https://github.com/danielmiessler/SecLists.git
wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Fuzzing/XSS/XSS-OFJAAAH.txt
wget https://raw.githubusercontent.com/drtychai/wordlists/master/intruder/lfi.txt
wget https://raw.githubusercontent.com/xmendez/wfuzz/master/wordlist/Injections/SQL.txt


#eyewitness
apt install eyewitness 

# SSLSCAN
apt-get install zlib1g
apt-get install libc6
apt-get install sslscan

#feroxbuster
apt install feroxbuster
apt install fonts-noto-color-emoji
apt install libc6

# INSTALANDO ANEW

go get -u github.com/tomnomnom/anew
mv /root/go/bin/anew  /usr/bin/

# INSTALANDO FINDOMAIN

wget https://github.com/findomain/findomain/releases/latest/download/findomain-linux
chmod +x findomain-linux
mv findomain-linux /usr/bin/findomain

# INSTALANDO XARGS

wget https://github.com/brentp/gargs/releases/download/v0.3.9/gargs_linux
chmod +x gargs_linux
mv gargs_linux /usr/bin/xargs

# INSTALANDO CENSYS

pip install censys-command-line

# INSTALANDO SECURITYHEADERS
cd /home
git clone https://github.com/koenbuyens/securityheaders.git
cd securityheaders
pip3 install -r requirements.txt

# INSTALANDO CURL

apt install curl

#INSTALANDO TESTSSL
apt-get install hexdump
apt-get install bsdmainutils
cd /home
git clone https://github.com/drwetter/testssl.sh

#Script nmap 
cd /home
wget https://gist.githubusercontent.com/Aquilao/adde703f52d7c89d2cdad01067f588b1/raw/cceaa5d69c7f5625489bc2fb37ee8b3b98a46baf/CVE-2015-1635_PoC.py
chmod +x CVE-2015-1635_PoC.py

wget https://raw.githubusercontent.com/psc4re/NSE-scripts/master/cve-2020-0796.nse
mv cve-2020-0796.nse /usr/share/nmap/scripts/

wget https://raw.githubusercontent.com/microsoft/CSS-Exchange/main/Security/src/http-vuln-cve2021-26855.nse
mv http-vuln-cve2021-26855.nse /usr/share/nmap/scripts/

wget https://raw.githubusercontent.com/s4n7h0/NSE/master/http-lfi.nse
mv http-lfi.nse /usr/share/nmap/scripts/

# Atualizar 

apt update
apt upgrade

echo "pra usar censys tem que instalar api do censys com o  camando "
echo "censys config"
echo "Digita API"
echo "============================================="
echo "============================================="

echo " TODAS FERRAMENTAS INSTALADAS COM SUCESSO "
