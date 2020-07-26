# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
# ALUNO: SÉRGIO PIRES BARRA
# SCRIPT: Servidor de sockets TCP modificado para receber um comando qualquer do cliente e executar esse comando localmente (python 3)
#

# importacao das bibliotecas
from socket import * # sockets
import os

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
while 1:
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  sentence = sentence.decode('utf-8')
  os.system(sentence)
  print ('Cliente %s enviou: %s.' % (addr, sentence))
  #connectionSocket.close() # encerra o socket com o cliente

serverSocket.close() # encerra o socket do servidor