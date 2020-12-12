# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 11:10:59 2020

@author: bfp2
"""

def divide(entrada, sufixo):
    with open('imteste.inc','r') as f:
        for linha in f:
            if linha.strip() == '': # Identifica linhas que começam com ** ou linhas em branco
                continue
            elif linha.strip().startswith('POR'):
                fw = open('POR_'+sufixo+'.inc','w')
            elif linha.strip().startswith('NETGROSS'):
                fw = open('NTG_'+sufixo+'.inc','w')
            elif linha.strip().startswith('PERMI'):
                fw = open('PERMI_'+sufixo+'.inc','w')
            elif linha.strip().startswith('PERMJ'):
                fw = open('PERMJ_'+sufixo+'.inc','w')
            elif linha.strip().startswith('PERMK'):
                fw = open('PERMK_'+sufixo+'.inc','w')
            fw.write(linha)

def lerarquivo(arq):
    propriedades = ['POR ALL','NETGROSS ALL','PERMI ALL','PERMJ ALL','PERMK ALL']
    lista = []
    with open(arq,'r') as f:
        for linha in f:
            if linha.strip() == "" or linha.strip() in propriedades:
                continue
            linhalista = linha.split();
            for item in linhalista:
                itens = item.split("*")
                if len(itens) == 1:
                    lista.append(float(item))
                else:
                    print(itens[0], itens[1])
                    for i in range(0,int(itens[0])):
                        lista.append(float(itens[1]))
    return lista
            


divide('imteste.inc', 'teste')

sufixos = list(range(0,10))
for suf in sufixos:
    divide('im'+str(suf)+'.inc',str(suf))

lista = lerarquivo('NTG_0.inc')
print(lista)
    
