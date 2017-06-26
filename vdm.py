# -*- coding:Utf-8 -*-

import urllib2
from HTMLParser import HTMLParser

def lire():
    fichier = open("vdm.txt", "r+")
    vdm = fichier.readlines()
    taille = len(vdm)

    try:
        print "\n", vdm[taille-1]
        size =  sum(len(mot) for mot in vdm) - len(vdm[taille-1])
        fichier.truncate(size)

    except:
        data = urllib2.urlopen("http://www.viedemerde.fr/aleatoire")
        htmlSource = data.read()
        parser = MyHTMLParser()
        parser.feed(htmlSource)
        ecrire()
        lire()

    fichier.close()

def ecrire():
    fichier = open("vdm.txt", "a+")

    i = 0
    while i < len(vdm):
        if "VDM" in vdm[i]: vdm[i] += '\n'
        fichier.write(vdm[i])
        i+=1

    fichier.close()

class MyHTMLParser(HTMLParser):
    flag = False

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            for name, value in attrs:
                if name == "class" and value == "fmllink":
                    self.flag = True

    def handle_endtag(self, tag):
        if tag == "a":
            self.flag = False

    def handle_data(self, data):
        if self.flag and data !=".":
            vdm.append(data)

vdm = []

try:
    lire()
except:
    ecrire()
