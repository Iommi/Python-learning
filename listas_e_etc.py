# ==================================================
# RESUMO — TIPOS DE DADOS SEQUENCIAIS E DICIONÁRIO
# ==================================================
#
# Tipos de dados sequenciais armazenam múltiplos valores
# em uma única variável.
#
# Principais tipos:
# - list  (lista)        -> mutável
# - tuple (tupla)        -> imutável
# - set   (conjunto)     -> não indexado, sem repetição
# - str   (string)       -> sequência de caracteres
# - dict  (dicionário)   -> pares chave:valor


# -----------------------------
# 1. LIST (lista)
# -----------------------------
# Lista é ordenada, indexada e mutável

nomes = ['Ana', 'Bruno', 'Carlos']

print(nomes)
print(nomes[0])          # acesso por índice
nomes.append('Daniel')   # adiciona elemento
print(nomes)

nomes[1] = 'Beatriz'     # altera elemento
print(nomes)

print(len(nomes))        # tamanho da lista


# -----------------------------
# 2. TUPLE (tupla)
# -----------------------------
# Tupla é ordenada, indexada e IMUTÁVEL

cores = ('vermelho', 'azul', 'verde')

print(cores)
print(cores[0])

# cores[1] = 'amarelo'   # ERRO: tupla não pode ser alterada


# -----------------------------
# 3. SET (conjunto)
# -----------------------------
# Set não é ordenado, não possui índice e não aceita repetição

numeros = {1, 2, 3, 3, 4}

print(numeros)           # valores repetidos são removidos

numeros.add(5)
print(numeros)

numeros.remove(2)
print(numeros)


# -----------------------------
# 4. STRING (str)
# -----------------------------
# String é uma sequência imutável de caracteres

texto = "Python"

print(texto)
print(texto[0])          # primeiro caractere
print(texto[-1])         # último caractere

# texto[0] = 'p'         # ERRO: string é imutável


# -----------------------------
# 5. DICT (dicionário)
# -----------------------------
# Dicionário armazena pares chave:valor
# As chaves são únicas e imutáveis

aluno = {
    'nome': 'Daniel',
    'idade': 22,
    'curso': 'ADS'
}

print(aluno)
print(aluno['nome'])     # acesso pelo nome da chave

aluno['idade'] = 23      # altera valor
print(aluno)

aluno['cidade'] = 'SP'   # adiciona novo par
print(aluno)

print(aluno.keys())      # chaves
print(aluno.values())    # valores
print(aluno.items())     # pares


# -----------------------------
# 6. Percorrendo estruturas
# -----------------------------

# Percorrendo lista
for nome in nomes:
    print(nome)

# Percorrendo string
for letra in texto:
    print(letra)

# Percorrendo dicionário
for chave, valor in aluno.items():
    print(chave, valor)


# -----------------------------
# 7. Comparação rápida
# -----------------------------
# list  -> ordenada, mutável, indexada
# tuple -> ordenada, imutável, indexada
# set   -> não ordenado, sem índice, sem repetição
# str   -> ordenada, imutável, indexada
# dict  -> chave:valor, mutável, chaves únicas


# -----------------------------
# RESUMO RÁPIDO (ESTILO PROVA)
# -----------------------------
# - Listas permitem alteração de valores
# - Tuplas e strings são imutáveis
# - Sets não aceitam valores duplicados
# - Dicionários usam pares chave:valor
# - Acesso em listas/tuplas/strings é por índice
# - Acesso em dicionários é pela chave