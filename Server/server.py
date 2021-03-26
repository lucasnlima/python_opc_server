#socket_echo_server.py

import time
import pywintypes
import OpenOPC
import socket
import sys

pywintypes.datetime = pywintypes.TimeType
opc = OpenOPC.client()

def startOpcClient():
    opc.connect(opc.servers()[0],'localhost')
    print("Conectado ao servidor OPC: ")
    print(opc.properties('ArduinoSerial0.Ze.Int1'))
startOpcClient


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]
get_ip_address


#Interface Principal:
print("Gateway OPC:")
print(" IP: " +  get_ip_address())
print(" OPC Servers Dispniveis: " +"".join(str(x) for x in opc.servers()))
print("\n Digite <ENTER> para conectar ao servidor opc e iniciar o gateway ou <S> para sair:")
keyboard_in = ''
keyboard_in = input()
while True:
    if(keyboard_in == ""):
        startOpcClient()
        break
    elif(keyboard_in == ('s' or 'S')):
        print("Saindo...")
        break
    else:
        keyboard_in = input("Entrada invalida digite novamente:")


#Create a TCP/IP socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

#Bind the socket to the port
server_adress = (get_ip_address(),10000)
print('starting up on {} port {}'.format(*server_adress))
sock.bind(server_adress)

#Listen for incoming connections
sock.listen(1)

while True:
    #Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from',client_address)


        #Receive message to send arduino data
        while True:
            data = connection.recv(255)
            if data:
                TAG = opc.properties('ArduinoSerial0.Ze.Int1')
                name = str(TAG[0][2])
                valuea = str(TAG[2])
                message = name + valuea
                value = str.encode(message)
                print('Enviando estado atual do arduino...')       
                #while True:    
                connection.sendall(value)             
            else:
                print('no data from',client_address)
                break
    finally:
        #Clean up the connection
        connection.close()