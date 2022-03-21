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

    varrerURL(url)
    

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

def varrerURL(url):

    #SITE :securityheaders.com 
    cmd('curl -skI ' + url + ' > saidaCurlCabecalho.csv')

   

 #securityheaders 
    
    
    cmd('python3 /home/securityheaders/securityheaders.py --flatten ' + url + ' > cabecalho.csv')

     # SHCHECK

    cmd('shcheck.py https:// ' + url + ' > shcheck') 
    cmd('shcheck.py https:// '+ url + ' -i > shcheckparamI')
    
    print("FIM DO SCRIPT")
    time.sleep(2)

if __name__ == '__main__':
     main()
