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

    varrerScripNSE(url)
    

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

def varrerScripNSE(url):

#A01: 2021 - Controle de acesso quebrado na qual seria a CVE 2011-0049 (Path Traversal) = Explora uma vulnerabilidade de travessia de diretório existente no Majordomo2 para recuperar arquivos remotos.

    print("Estamos no momento executando a script http-majordomo2-dir-traversal.nse ... por favor, aguarde um momento!")
    cmd('nmap --script http-passwd --script http-majordomo2-dir-traversal.nse ' + url + ' > saidaPathTravessal')
    print("script http-majordomo2-dir-traversal.nse executada, vamos para a próxima")

    # SCRIPT nse-log4shell

    print("Estamos no momento executando a script nse-log4shell ... por favor, aguarde um momento!")
    cmd('nmap -sV -T4 -sS -Pn -v  --script http-log4shell.nse --script imap-log4shell.nse --script ssh-log4shell.nse --script ftp-log4shell.nse --script http-spider-log4shell.nse --script smtp-log4shell.nse   --script ftp-log4shell.nse ' + url + ' -oN log4shell.nse')
    print("script nse-log4shell executada, vamos para a próxima")

    # CVE-2015-1635/ms15-034 HTTP.sys no Microsoft Windows 7 SP1, Windows Server 2008 R2 SP1, Windows 8, Windows 8.1 e Windows Server 2012 Gold e R2 permite que invasores remotos executem código arbitrário por meio de solicitações HTTP criadas, também conhecido como "Vulnerabilidade de execução remota de código HTTP.sys. "

    print("Estamos no momento executando a script HTTP.sys ... por favor, aguarde um momento!")
    cmd('python3 /home/CVE-2015-1635_PoC.py https:// ' + url + ' > ResulCVE-2015-1635_HTTP.sys')
    print("script CVE-2015-1635_HTTP.sys executada, vamos para a próxima")


    #CVE-2017-7269 Existe uma vulnerabilidade no IIS quando o WebDAV manipula indevidamente objetos na memória, o que pode permitir que um invasor execute código arbitrário no sistema do usuário. Um invasor que explorar com êxito esta vulnerabilidade pode obter os mesmos direitos do usuário atual.

    print("Estamos no momento executando a script CVE-2017-7269/WebDAV ... por favor, aguarde um momento!")
    cmd('nmap --script http-iis-webdav-vuln -p80,8080,443 ' + url + ' -oN WebDAV')
    print("script CVE-2017-7269/WebDAV executada, vamos para a próxima")

    '''
    CVE-2015-4000 Uma falha foi encontrada na forma como o protocolo TLS compõe a troca Diffie-Hellman (para conjuntos de criptografia de grau de exportação e não exportação). Um invasor pode usar essa falha para fazer o downgrade de uma conexão DHE para usar tamanhos de chave de nível de exportação, que podem ser interrompidos por pré-computação suficiente. 
    Este script simula handshakes SSL / TLS usando ciphersuites que têm Diffie-Hellman efêmero como o algoritmo de troca de chave.

    Os parâmetros do grupo Diffie-Hellman MODP são extraídos e analisados ​​quanto à vulnerabilidade ao Logjam (CVE 2015-4000) e outras fraquezas.

    '''
    print("Estamos no momento executando a script ssl-dh-params ... por favor, aguarde um momento!")
    cmd('nmap --script ssl-dh-params ' + url + ' > saidaCVE-2015-4000SSL/TLS')
    print("script CVE-2015-4000/ssl-dh-params executada, vamos para a próxima")

    '''
    CVE-2014-0160 as implementações (1) TLS e (2) DTLS no OpenSSL 1.0.1 antes de 1.0.1g 
    não manipulam adequadamente os pacotes de extensão de pulsação, 
    o que permite que atacantes remotos obtenham informações confidenciais da memória do processo 
    por meio de pacotes criados que acionam uma sobre-leitura do buffer,
    conforme demonstrado pela leitura de chaves privadas, relacionadas a d1_both.c e t1_lib.c, 
    também conhecido como bug Heartbleed.

    '''
    print("Estamos no momento executando a script ssl-heartbleed ... por favor, aguarde um momento!")
    cmd('nmap -p 443 --script ssl-heartbleed ' + url + ' > saidaCVE-2014-0160ssl-heartbleed')
    print("script CVE-2014-0160ssl-heartbleed executada, vamos para a próxima")

    '''
    CVE-2020-0796  no Windows 10 e nos sistemas operacionais Windows Server, 
    a CVE-2020-0796 afeta o protocolo SMBv3 (Microsoft Server Message Block 3.1.1). 
    Segundo a Microsoft, um hacker pode explorar esta vulnerabilidade para executar códigos arbitrários no lado do servidor ou cliente SMB. 
    Para atacar o servidor, pode-se simplesmente enviar um pacote especialmente criado. Quanto ao cliente, os atacantes precisam configurar um servidor SMBv3 malicioso e convencer o usuário a se conectar.

    '''
    print("Estamos no momento executando a script CVE-2020-0796/SMBv3... por favor, aguarde um momento!")
    cmd('nmap -p445 --script cve-2020-0796 ' + url + ' > saidaCVE-2020-0796/SMBv3')
    print("script CVE-2020-0796/SMBv3 executada, vamos para a próxima")


    '''
    CVE-2021-26855 Vulnerabilidade de execução remota de código do Microsoft Exchange Server Este ID CVE é exclusivo de CVE-2021-26412,
    CVE-2021-26854, CVE-2021-26857, CVE-2021-26858, CVE-2021-27065, CVE-2021-27078.
    '''
    print("Estamos no momento executando a script http-vuln-cve2021-26855... por favor, aguarde um momento!")
    cmd('nmap -p 443,80 --script http-vuln-cve2021-26855 ' + url + ' > saidaCVE-2021-26855/MicrosoftExchangeServer')
    print("script http-vuln-cve2021-26855 executada, vamos para a próxima")

    '''
    "Esse script abaixo serve para enumerar endpoints de XSS,LFI,SQLI que esta nas seguintes CVES :
    Cross-site Scripting (XSS) = A sanitização de entrada inválida leva a Cross Site Scripting (XSS) refletido  pode levar a um sequestro de sessão do usuário, Os invasores podem roubar cookies e até assumir contas e realizar diferentes atividades maliciosas.
    Local File Inclusion (LFI) = Um invasor pode ler arquivos locais no servidor da Web aos quais normalmente não teria acesso, como o código-fonte do aplicativo ou arquivos de configuração contendo informações confidenciais sobre como o site está configurado.
    Sql Injection(SQLI) = Um invasor pode usar a injeção de SQL para contornar os mecanismos de autenticação e autorização de um aplicativo da Web 
    e recuperar o conteúdo de um banco de dados inteiro. O SQLi também pode ser usado para adicionar, modificar e excluir registros em um banco de dados, afetando a integridade dos dados. Nas circunstâncias certas, o SQLi também pode ser usado por um invasor para executar comandos do sistema operacional, 
    que podem então ser usados ​​para escalar um ataque ainda mais prejudicial.


    esta falhas sempre esta entre as 10 da owasp "

    '''
    print("Estamos no momento  enumerando xss,sqli,lfi... por favor, aguarde um momento!")
    
    cmd('subfinder -d ' + url + '> saidasubfin')
    cmd('assetfinder -subs-only ' + url + '> saidaAssetf')
    cmd('cat saidasubfin saidaAssetf | anew saidaEndpoints')
    cmd('cat saidaEndpoints | httpx -silent -threads 1000 | anew saida200Endpoints')
    cmd('cat saida200Endpoints | gauplus | httpx -silent -threads 1000 | anew saida200gauplus')
    cmd('cat saida200gauplus | gf xss | httpx -silent -threads 1000 | anew saidaXSS')
    cmd('cat saida200gauplus | gf lfi | httpx -silent -threads 1000 | anew saidaLFI ')
    cmd('cat saida200gauplus | gf sqli |  httpx -silent -threads 1000 | anew saidaSQLI ')
    cmd('rm -rf saidasubfin saidaAssetf saidaEndpoints')

    print("enumeração terminada, vamos para a próxima")

    print("Testando os Endpoints de xss,lfi,sqli")

    cmd('cat saidaXSS | dalfox pipe --skip-bav --mining-dict-word /home/XSS-OFJAAAH.txt |anew saidaDalfoxXSS ')
    cmd('cat saidaLFI | dalfox pipe --skip-bav --mining-dict-word /home/lfi.txt |anew saidaDalfoxLFI')
    cmd('cat saidaSQLI | dalfox pipe --skip-bav --mining-dict-word /home/SQL.txt |anew saidaDalfoxSQLI')





    print("FIM DO SCRIPT")
    time.sleep(2)

if __name__ == '__main__':
     main()
