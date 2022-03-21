#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import time, sys, os
from subprocess import PIPE, Popen
from pathlib import Path

def main():
    issu()

    folder = input("Vamos criar uma pasta para salvar os arquivos, digite um nome pra ela: ")
    #cria a pasta
    os.mkdir(folder)    
    # acessa a pasta
    os.chdir(folder)

    # informa o host: site.com | 127.0.0.1
    url = input("digita a url: ")

    varrerSSL(url)
    

#verifica se está com super usuário
def issu():
    if os.geteuid() != 0:
        for i in range(3):
            print("\033[93m              Este programa precisa ser executado em modo ROOT!!\n\n")
            time.sleep(0.5)
        print("\033[93m                      Exemplo: sudo python3 planoBasico.py")
        time.sleep(2)
        os.system('clear')
        sys.exit(0)
    else:
        pass

#processos | pega a saída
def cmd(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    for line in process.stdout:
        print(str(line))

    return process.communicate()[0]

# CTFR
def varrerSSL(url):
  
    cmd('python2 /home/ctfr/ctfr.py -d ' + url + ' > saidaCtfr.csv')
    

    # SSLYZE
    cmd('sslyze ' + url + ' :443 > saidaSSL.csv')

    # SSLSCAN

    cmd('sslscan ' + url + ' >sslscan')
    cmd('sslscan --show-certificate 443 ' + url + ' >sslscanCertifi')
    # NMAP SCRIPT PRA SSL
    
    cmd('nmap --script ssl-enum-ciphers -p 443 ' + url + ' > nmapsslscan')

    # O testssl.sh é uma ferramenta que permite avaliar de forma detalhada a criptografia TLS/SSL além de reportar a validade do certificado e suas vulnerabilidades.

    cmd('. /home/testssl.sh/testssl.sh --ssl-native ' + url + ' > testSSL')

    
    print("FIM DO SCRIPT")
    time.sleep(2)

#processos | pega a saída
def cmd(command):
    process = Popen(
        args=command,
        stdout=PIPE,
        shell=True
    )
    for line in process.stdout:
        print(str(line))

    return process.communicate()[0] 
    
if __name__ == '__main__':
     main()
