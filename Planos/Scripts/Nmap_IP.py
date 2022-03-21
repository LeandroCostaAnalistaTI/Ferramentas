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
    ip = input("digita o ip: ")
    
    print("Vamos iniciar a rodar as ferramentas...")
    varrerNmap(ip)
    

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

def varrerNmap(ip):

#nmap


    print("Estamos no momento executando a ferramenta nmap... por favor, aguarde um momento!")
    
    # Encontrar erros HTTP
    cmd('nmap -p80,443 --script=http-errors ' + ip + ' -oN detecErroHttp')
    # Encontrar Servidores Compartilhados e Novos
    cmd('nmap -p80,443 --script=dns-brute ' + ip + ' -oN ServidoresCompartilhados')
    # SCRIPT nse-log4shell
    cmd('nmap -sV -T4 -sS -Pn -v  --script http-log4shell.nse --script imap-log4shell.nse --script ssh-log4shell.nse --script ftp-log4shell.nse --script http-spider-log4shell.nse --script smtp-log4shell.nse   --script ftp-log4shell.nse ' + ip + ' -oN log4shell.nse')

    cmd('nmap -n -p21,22,23,25,53,80,110,111,135,139,143,443,445,993,1723,3306,3389,5900,8080 --open ' + ip + ' -oA scandiscovery')
    cmd('nmap -sS -Pn -p21,22,23,25,53,80,110,111,135,139,143,443,445,993,1723,3306,3389,5900,8080 -v --script=vuln ' + ip + ' -oN reconVuln')
    cmd('nmap -Pn -sV -n -p$(cat scandiscovery.nmap | grep "tcp" | grep -v ports | cut -d'/' -f1 | sed "N;s/\n/,/g")' + ip + ' -oA scandetailed')
    
    print("nmap executada !!")
    time.sleep(2)

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