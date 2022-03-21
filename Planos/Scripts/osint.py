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
    varrerOsint(url)
    

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

def varrerOsint(url):
 
    # wafwoof
    print("Estamos no momento executando a ferramenta wafw00f... por favor, aguarde um momento!")
    cmd('wafw00f ' + url + ' > saidawafwoof')
    print("wafw00f executada, vamos para a próxima")
    # deixa esperar uns segundinhos só para ficar mais legal
    time.sleep(2)

    # whois
    print("Estamos no momento executando a ferramenta whois... por favor, aguarde um momento!")
    cmd('whois ' + url + ' > whois.csv ')
    print("whois executada, vamos para a próxima")
    # deixa esperar uns segundinhos só para ficar mais legal
    time.sleep(2)

    #censys
    print("Estamos no momento executando a ferramenta censys... por favor, aguarde um momento!")
    cmd('censys search ' + url + ' > censys.csv')
    cmd('censys search --index-type hosts ' + url + ' > censys.csv')
    cmd('censys search --index-type certs ' + url + ' > censys.csv')
    cmd('censys search --index-type ipv4 ' + url + ' > censys.csv')
    print("censys executada, vamos para a próxima")
    time.sleep(2)

    

    # METAGOOFIL
    print("Estamos no momento executando a ferramenta metagoofil... por favor, aguarde um momento!")
    cmd('metagoofil -d' + url + ' -t pdf,doc,xls,ppt,odp,ods,docx,xlsx,pptx -l 200 -n 10 -o saidaMetagoofil')
    print("metagoofil executada, vamos para a próxima")
    time.sleep(2)
    
    #theHarvester 
    print("Estamos no momento executando a ferramenta theHarvester... por favor, aguarde um momento!")
    cmd('theHarvester -d ' + url + ' -b all > saidatheharvester')
    print("theHarvester executada, vamos para a próxima")    
    time.sleep(2) 

     # enum4linux
    print("Estamos no momento executando a ferramenta enum4linux... por favor, aguarde um momento!")
    cmd('enum4linux ' + url + ' > enum4.txt')
    print("enum4linux executada, vamos para a próxima")    
    time.sleep(2)

   # Nikto
    print("Estamos no momento executando a ferramenta Nikto... por favor, aguarde um momento!")
    cmd('nikto -host ' + url + ' > nikto.txt')
    print("nikto executada, vamos para a próxima")    
    time.sleep(2)

    # whatweb
    print("Estamos no momento executando a ferramenta whatweb... por favor, aguarde um momento!")
    cmd('whatweb ' + url + ' > whatwe.txt')
    print("whatweb executada, vamos para a próxima")    
    time.sleep(2)
   

    # AMASS
    print("Estamos no momento executando a ferramenta Amass... por favor, aguarde um momento!")
    cmd('amass enum -d ' + url + ' > saidaamass')   
    print("Amass executada, vamos para a próxima")    
    time.sleep(2) 

    # eyewitness
    print("Estamos no momento executando a ferramenta eyewitness... por favor, aguarde um momento!")
    cmd('eyewitness --single ' + url  + ' -f ./out')  
    print("eyewitness executada, vamos para a próxima")
    time.sleep(2)

    # feroxbuster
    print("Estamos no momento executando a ferramenta feroxbuster... por favor, aguarde um momento!")
    cmd('feroxbuster --url https:// ' + url + ' --depth 2  -s 200,201,302,207,500,501  -w /home/wordlist/SecLists/Discovery/Web-Content/raft-medium-directories.txt > feroxbus.txt')
    cmd('feroxbuster --url https:// ' + url + ' --depth 2   -x pdf -x js,html -x php txt json,docx -w /home/wordlist/SecLists/Discovery/Web-Content/raft-medium-directories.txt > ferox.txt')
    print("feroxbuster executada, vamos para a próxima")
    time.sleep(2)
 
    #nmap


    print("Estamos no momento executando a ferramenta nmap... por favor, aguarde um momento!")
    
    # Encontrar erros HTTP
    cmd('nmap -p80,443 --script=http-errors ' + url + ' -oN detecErroHttp')
    # Encontrar Servidores Compartilhados e Novos
    cmd('nmap -p80,443 --script=dns-brute ' + url + ' -oN ServidoresCompartilhados')
    # SCRIPT nse-log4shell
    cmd('nmap -sV -T4 -sS -Pn -v  --script http-log4shell.nse --script imap-log4shell.nse --script ssh-log4shell.nse --script ftp-log4shell.nse --script http-spider-log4shell.nse --script smtp-log4shell.nse   --script ftp-log4shell.nse ' + url + ' -oN log4shell.nse')

    cmd('nmap -n -p21,22,23,25,53,80,110,111,135,139,143,443,445,993,1723,3306,3389,5900,8080 --open ' + url + ' -oA scandiscovery')
    cmd('nmap -sS -Pn -p21,22,23,25,53,80,110,111,135,139,143,443,445,993,1723,3306,3389,5900,8080 -v --script=vuln ' + url + ' -oN reconVuln')
    cmd('nmap -Pn -sV -n -p$(cat scandiscovery.nmap | grep "tcp" | grep -v ports | cut -d'/' -f1 | sed "N;s/\n/,/g")' + url + ' -oA scandetailed')
    
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