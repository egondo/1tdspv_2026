palavra = input("Palavra: ")

resultado = ''

i = 0
while i < len(palavra):
    #print(palavra[i] + ' ')
    resultado = resultado + palavra[i]
    resultado = resultado + " "
    i = i + 1
    
print(resultado)