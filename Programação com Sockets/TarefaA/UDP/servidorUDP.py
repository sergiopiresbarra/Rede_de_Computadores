# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
# ALUNO: SÉRGIO PIRES BARRA
# SCRIPT: Servidor de sockets UDP modificado para receber o comando 'data' do cliente e enviar resposta com a data e o horário do sistema (python 3)
#

# importacao das bibliotecas
from socket import * # sockets
import time

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 61000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))
while 1:
    message, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    message = message.decode('utf-8')
    if message == 'data':
        modifiedMessage = str(time.ctime())
        print ('Cliente %s enviou: %s, enviando: %s' % (clientAddress, message, modifiedMessage))
        serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress) 
        # envia a resposta para o cliente
    else:
        modifiedMessage = 'Erro! , Por favor envie apenas o comando data'
        print ('Cliente %s enviou: %s, enviando: %s' % (clientAddress, message, modifiedMessage))
        serverSocket.sendto(modifiedMessage.encode('utf-8'), clientAddress)

serverSocket.close() # encerra o socket do servidor