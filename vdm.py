# -*- coding:Utf-8 -*-
import urllib2 as get

vdm_start = 'class="fmllink">Aujourd'
vdm_end = '</a></p><div class="date">'

def get_quote():
        quote = get.urlopen('http://www.viedemerde.fr/aleatoire').read()
        quote = [a.split(vdm_end)[:-1] for a in quote.split(vdm_start)[1:]]
        for i, item in enumerate(quote):
                item = [a.split('>')[1] if '>' in a else a for a in item[0].split('</a><a')]
                quote[i] = 'Aujourd'+''.join(item)
        return quote

with open('vdm.txt', 'r') as f: vdm= f.read()
vdm = vdm.split('\n') if vdm else get_quote()
while not raw_input(''):
        print '\n',vdm.pop(0),'\n'
        if not vdm: vdm = get_quote()
