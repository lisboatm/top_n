# Problema: Classificação de Colocação em Categorias "Top N"

Neste problema, o objetivo é identificar a categoria "Top N" mais baixa em que uma colocação \( K \) pertence, de acordo com categorias amplamente usadas para classificar colocação, como "Top 1", "Top 3", "Top 5", "Top 10", etc.

## Descrição do Problema

Dada uma posição \( K \) de um participante em um ranking (com \( 1 \leq K \leq 100 \)), determine a menor categoria que contém essa colocação. As categorias disponíveis são:
- **Top 1**: \( K = 1 \)
- **Top 3**: \( 1 \leq K \leq 3 \)
- **Top 5**: \( 1 \leq K \leq 5 \)
- **Top 10**: \( 1 \leq K \leq 10 \)
- **Top 25**: \( 1 \leq K \leq 25 \)
- **Top 50**: \( 1 \leq K \leq 50 \)
- **Top 100**: \( 1 \leq K \leq 100 \)

Para cada valor de \( K \), você deve imprimir "Top N", onde \( N \) é a menor categoria aplicável para a colocação fornecida.

### Entrada
- Um valor inteiro \( K \), representando a colocação no ranking, onde \( 1 \leq K \leq 100 \).

### Saída
- Uma linha contendo o texto “Top N”, onde \( N \) corresponde ao menor número que caracteriza a categoria da colocação \( K \).

### Exemplo de Entrada e Saída

| Entrada | Saída     |
|---------|-----------|
| 7       | Top 10    |
| 25      | Top 25    |
| 26      | Top 50    |

## Solução

Para resolver este problema, verificamos em qual faixa de categoria o número \( K \) se encontra e imprimimos a categoria correspondente. A abordagem ideal é usar uma sequência de condicionais para determinar a menor categoria possível.

### Passo a Passo da Solução

1. Ler a entrada \( K \).
2. Verificar a categoria de \( K \) da menor para a maior (começando do "Top 1" até "Top 100").
3. Imprimir o resultado na primeira categoria aplicável.

### Exemplo de Código em Python

```python
# Leitura da entrada
k = int(input())

# Verificação e impressão da categoria aplicável
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
```

### Explicação do Código
- O código verifica o valor de \( K \) usando uma série de condicionais (`if-elif`) que avaliam de menor a maior categoria.
- A primeira condição atendida imprime a saída e interrompe a verificação, assegurando a menor categoria aplicável para \( K \).

### Complexidade
- A solução tem complexidade constante **O(1)**, pois o número de verificações é fixo.

## Observações
- A implementação é eficiente e cobre todos os casos para \( 1 \leq K \leq 100 \).
- Esta abordagem é útil em competições de programação devido à sua simplicidade e clareza.
