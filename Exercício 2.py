#2) Escreva um programa que verifique, em uma string, a existência da letra ‘a’, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.
#IMPORTANTE: Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;

texto = input(str("digite algum texto: "))
text_list = texto.lower()
text_list = list(text_list)

if "a" in text_list:
    qtd_letra = 0
    i = 0
    while i < len(text_list):
        tam = text_list[i]
        if tam == "a":
            qtd_letra += 1
        i += 1
    print ("A palavra digitada possuía a letra 'a' um total de "+str(qtd_letra)+" vez(es)!")
else:
    print ("a string não possuia a letra 'a'")
    
#DONE