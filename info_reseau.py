#!/usr/bin/python3
# -*- coding: utf-8 -*-
# auteur Pascal VINCENT
'''
pour connaitre mon adresse IP, je crée un socket vers une destination quelconque
et je lis les informations envoyées qui contiennent mon adresse et le port que j'ai utilisé
'''
import socket

hoteDest = "localhost"
portDestination = 800
destination = (hoteDest,portDestination)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# on se connecte n'importe où
s.connect(destination)

# on lit le début du message envoyé
ip = s.getsockname()[0]

print(f"mon adresse IP = {ip}")