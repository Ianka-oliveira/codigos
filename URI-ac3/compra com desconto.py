print("Digite a valor do produto")
preco = float(input())

print("Digite a quantidade de produto")
qtd_prod = int(input())

total = preco*qtd_prod
desc_unidade = ((qtd_prod * 1) / 100) + 0.1
preco_desconto = total * desc_unidade

print("preco original: ", "%.2f" % total)
print("preco com desconto", "%.2f" % (total - preco_desconto))
