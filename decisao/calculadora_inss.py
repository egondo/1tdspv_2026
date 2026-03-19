#Faixa de Salário (R$) 	Alíquota
#Até 1.621,00	7,5%
#De 1.621,01 até 2.902,84	9%
#De 2.902,85 até 4.354,27	12%
#De 4.354,28 até 8.475,55	14%

salario = float(input("Salário: "))
if salario <= 1621:
    inss = salario * 7.5 / 100
else:
    inss = 1621 * 0.075 #(7.5%)
    if salario <= 2902.84:
        inss = inss + (salario - 1621) * 0.09
    else:
        inss = inss + (2902.84 - 1621) * 0.09    
        if salario <= 4354.27:
            inss = inss + (salario - 2902.84) * 0.12
        else:
            inss = inss + (4354.27 - 2902.84) * 0.12
            if salario <= 8475.55:
                inss = inss + (salario - 4354.27) * 0.14
            else:
                inss = inss + (8475.55 - 4354.27) * 0.14

print(f"Desconto INSS é {inss}")
