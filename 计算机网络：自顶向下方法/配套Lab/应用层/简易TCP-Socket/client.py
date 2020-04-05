#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 10:14:51 2020

@author: IMAC
"""

import socket
s=socket.socket()

port= 12345
s.connect(('127.0.0.1',port))

print(s.recv(1024))

s.close()
