# main.py
# Bortoletti, Luis Alexandre
#
# teste para gerar log de aplicações
#
#================================================


import Logar
lista = [1,2,3,4,5,6,7,8,9]

# instanciar o Log
logar = Logar.Logar( "arquivo1")

#escrever mensagem no Log
logar.escrever("inicio")
for a in lista:
    #escrever mensagem no Log
    logar.escrever( f"linha {a}" )

#escrever mensagem no Log
logar.escrever(  "Fim" )