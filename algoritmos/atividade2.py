#Entrada de dados e conversao para numero

preco = float(input("Preço:"))
descontopercentual = float(input("Desconto em %:"))

desconto = preco * descontopercentual / 100
preco_final = preco - desconto
print(preco_final)

