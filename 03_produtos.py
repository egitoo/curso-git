cod = str(input("Informe o código: "))
nome = str(input("Informe o nome: "))
qtde = int(input("Informe a quantidade: "))
vlr_unit = float(input("Informe o valor unitário: "))
vlr_total = qtde * vlr_unit

print("Código: %s\nNome: %s\nQuantidade: %d\nValor unitário: %.2f\nValor total: %.2f" % (cod, nome, qtde, vlr_unit, vlr_total))