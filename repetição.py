===============================
#RESUMO — LAÇO FOR EM PYTHON
===============================

#O laço for é usado para percorrer (iterar) elementos de uma sequência,
#como listas, strings, tuplas, conjuntos ou intervalos (range).

#Sintaxe básica:
#for variavel in sequencia:
#    bloco de código
#"""

# -----------------------------
# 1. For com lista
# -----------------------------
nomes = ['Laura', 'Lis', 'Guilherme', 'Enzo', 'Arthur']

for nome in nomes:
    print(nome)

# 'nome' recebe um elemento da lista a cada iteração


# -----------------------------
# 2. For com string
# -----------------------------
for letra in "Python":
    print(letra)

# Cada caractere da string é percorrido


# -----------------------------
# 3. For com range()
# -----------------------------
for i in range(5):
    print(i)
# Saída: 0 1 2 3 4

for i in range(1, 6):
    print(i)
# Saída: 1 2 3 4 5

for i in range(0, 10, 2):
    print(i)
# Saída: 0 2 4 6 8


# -----------------------------
# 4. For com índice (enumerate)
# -----------------------------
nomes = ['Ana', 'Bruno', 'Carlos']

for indice, nome in enumerate(nomes):
    print(indice, nome)

# enumerate() retorna índice + valor


# -----------------------------
# 5. For com condição (if)
# -----------------------------
numeros = [1, 2, 3, 4, 5]

for n in numeros:
    if n % 2 == 0:
        print(n, "é par")


# -----------------------------
# 6. break e continue
# -----------------------------
for n in range(1, 6):
    if n == 3:
        break
    print(n)
# Interrompe o laço

for n in range(1, 6):
    if n == 3:
        continue
    print(n)
# Pula a iteração atual


# -----------------------------
# 7. Boas práticas
# -----------------------------
# Use singular para o item e plural para a coleção

alunos = ['João', 'Maria']
for aluno in alunos:
    print(aluno)

# NÃO faça isso:
# for alunos in alunos:


# -----------------------------
# 8. For aninhado
# -----------------------------
for i in range(3):
    for j in range(2):
        print(i, j)


# -----------------------------
# 9. else no for
# -----------------------------
for n in range(3):
    print(n)
else:
    print("Laço finalizado sem break")


"""
#RESUMO RÁPIDO (ESTILO PROVA):

# O for percorre elementos de uma sequência
#- A variável do for recebe um valor por vez
#- range() gera números
#- enumerate() fornece índice e valor
#- break encerra o laço
#- continue pula a iteração
#- O nome da variável é definido pelo programador
#"""