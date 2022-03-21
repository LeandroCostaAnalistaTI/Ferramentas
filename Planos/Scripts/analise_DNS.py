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

    varrerDNS(url)
    

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

def varrerDNS(url):

    cmd('dnsmap ' + url + ' > saidasdnsmap')
    cmd('dig NS ' + url + ' > saidadigNS')
    cmd('dig MX ' + url + ' > saidadigTX')
    cmd('host ' + url + ' > saidaHost')
    cmd('host -t mx ' + url + ' > saidaHostMX')
    cmd('host -t ns ' + url + ' > saidaHostNS')
    cmd('dnsrecon -d ' + url + ' > saidadnsrecon')

    print("FIM DO SCRIPT")
    time.sleep(2)
    
if __name__ == '__main__':
     main()

