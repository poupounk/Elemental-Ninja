#!/usr/bin/python3
# -*- coding: utf-8 -*-
# auteur Pascal VINCENT
"""
Ce programme crée un serveur web simple
"""
import http.server  
 
# L'adresse IP du serveur
monIP = "127.0.0.1"
port = 8888
monAdresse = (monIP, port)

# On crée le gestionnaire
handler = http.server.SimpleHTTPRequestHandler
# et le serveur
monServeur = http.server.HTTPServer(monAdresse, handler)

print(f"Le serveur est actif à l'adresse {monIP}:{port}")

# On le laisse tourner en continu
monServeur.serve_forever()