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
    
    print("Vamos iniciar a rodar as ferramentas...")
    varrerVulnerabilidade(url)
    

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
    
  
    return process.communicate()[0]

def varrerVulnerabilidade(url):

# SUBFINDER
    print("Estamos no momento executando a ferramenta SUBFINDER... por favor, aguarde um momento!")

    cmd('subfinder -d ' + url + ' | anew  subfin.txt')

    print("SUBFINDER executada, vamos para a próxima")
    time.sleep(2)

# ASSETFINDER
    print("Estamos no momento executando a ferramenta ASSETFINDER... por favor, aguarde um momento!")
    cmd('assetfinder -subs-only ' + url + ' | anew assetf.txt')
    print("ASSETFINDER executada, vamos para a próxima")
    time.sleep(2)

#JUNTA TUDO NUM ARQUIVO SÓ

    cmd('cat assetf.txt  subfin.txt ' '| anew hosts.txt')

# VALIDANDO COM HTTPX
    cmd('cat hosts.txt | httpx -silent -threads 1000 | anew httpx.txt')

# PASSANDO NO GAUPLUS
    print("Estamos no momento executando a ferramenta GAUPLUS... por favor, aguarde um momento!")
    cmd('cat httpx.txt |gauplus | anew gaup.txt')   
    print("GAUPLUS executada, vamos para a próxima")
    time.sleep(2)

#ANALISANDO TODOS OS SUBDOMINIOS COM NUCLEI
    print("Estamos no momento executando a ferramenta NUCLEI... por favor, aguarde um momento!")
    cmd('cat gaup.txt | nuclei  -t /root/nuclei-templates/ -o resultnuclei')
    print("NUCLEI executada, vamos para a próxima")
    time.sleep(2)

# ANALISANDO TODOS OS SUBDOMINIOS COM JAELES
    print("Estamos no momento executando a ferramenta JAELES... por favor, aguarde um momento!")
    cmd('cat gaup.txt  | jaeles scan -c 100')
    print("JAELES executada, vamos para a próxima")
    time.sleep(2)

# ANALISANDO TODOS OS SUBDOMINIOS COM DALFOX
    print("Estamos no momento executando a ferramenta DALFOX... por favor, aguarde um momento!")
    cmd('cat gaup.txt  | dalfox pipe | anew dalfox')
    print("DALFOX executada, vamos para a próxima")
    time.sleep(2)

    print("FIM DO SCRIPT")
    time.sleep(2)

if __name__ == '__main__':
     main()