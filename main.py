# Leitura do valor de entrada
k = int(input())

# Verificação das faixas de categorias e impressão do resultado
if k == 1:
    print("Top 1")
elif k <= 3:
    print("Top 3")
elif k <= 5:
    print("Top 5")
elif k <= 10:
    print("Top 10")
elif k <= 25:
    print("Top 25")
elif k <= 50:
    print("Top 50")
else:
    print("Top 100")
