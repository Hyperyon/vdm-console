# -*- coding:Utf-8 -*-
import urllib2 as get
dir = 'the_path_of_the_life'

def get_data():
        req = get.build_opener()
        req.addheaders = [('User-Agent', 'Mozilla/5.0')]
        data = req.open('http://www.viedemerde.fr/aleatoire').read()
        return data

def get_quote(data): #parsing html
        quote = data.split("Aujourd'hui, ")[1:]
        for i, item in enumerate(quote):
            item = item.split('VDM\n')[0]
            quote[i] = "Aujourd'hui, "+''.join(item)+'VDM\n'
            quote[i] = unicode(quote[i], 'Utf-8').encode('cp1252') #thanks Windows
        return quote

def save_quote(quotes):
    with open(dir+'vdm.txt', 'a+') as f:
        for quote in quotes:
            f.write(quote)

def read_quote():
    quotes = ''
    with open(dir+'vdm.txt', 'r') as f:
        quotes = f.readlines()
        f.close()
    with open(dir+'vdm.txt', "w"):pass #erase content file

    print quotes[0]

    if len(quotes) == 1: #last quote so we need to get more
        save_quote(get_quote(get_data()))
    else:
        save_quote(quotes[1:])

read_quote()
