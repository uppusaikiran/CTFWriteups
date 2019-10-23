#!/usr/bin/python3

from websocket import create_connection
import string

def isNeedle(s="Gundremmingen C"):
        #ws.send(s)
        o = ws.recv()
        a = o[0]
        print a 
        print o
        #if o == "not found":
        #        return False
        o2 = ws.recv()
        #if "CAMP15_silverneedle" not in o or "CAMP15_silverneedle" not in o2:
        #        print("Golden Needle?: {0}".format(s))
        #        exit()
        print o2
        return True

ws = create_connection("ws://31.22.123.49:1909/ws")

def tryCombinations(b=""):
        for c in string.printable:
                print("trying {0}".format(b+c))
                if isNeedle(b + c):
                        tryCombinations(b+c)


tryCombinations()
