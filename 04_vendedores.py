total = float(input("Informe o valor total: "))

totaldesc = total - (total * 0.10)
comissao = totaldesc - (totaldesc * 0.05)

print("Total a pagar com 10% de desconto: ", totaldesc)
print("Valor da parcela 3x sem juros: ", round(total / 3, 2))
print("Comissão do vendedor: ", comissao)
