# ===============================
# RESUMO — LAÇO WHILE EM PYTHON
# ===============================
#
# O laço while é usado quando NÃO sabemos previamente
# quantas vezes o bloco de código será repetido.
#
# Sintaxe básica:
# while condicao:
#     bloco de código


# -----------------------------
# 1. While simples
# -----------------------------
contador = 1

while contador <= 5:
    print(contador)
    contador += 1
# Atenção: sem incremento gera loop infinito


# -----------------------------
# 2. While com condição lógica
# -----------------------------
senha = ""

while senha != "1234":
    senha = input("Digite a senha: ")

print("Acesso liberado")


# -----------------------------
# 3. While com break
# -----------------------------
contador = 0

while True:
    contador += 1
    print(contador)

    if contador == 3:
        break
# break encerra o laço


# -----------------------------
# 4. While com continue
# -----------------------------
contador = 0

while contador < 5:
    contador += 1

    if contador == 3:
        continue

    print(contador)
# continue pula a iteração atual


# -----------------------------
# 5. While com else
# -----------------------------
contador = 1

while contador <= 3:
    print(contador)
    contador += 1
else:
    print("Laço finalizado corretamente")


# -----------------------------
# 6. Loop infinito (cuidado)
# -----------------------------
# while True:
#     print("Loop infinito")


# -----------------------------
# 7. Boas práticas
# -----------------------------
# Sempre:
# - inicialize a variável de controle
# - atualize a variável dentro do laço
# - garanta uma condição de parada


# -----------------------------
# 8. While simulando for
# -----------------------------
i = 0
nomes = ['Ana', 'Bruno', 'Carlos']

while i < len(nomes):
    print(nomes[i])
    i += 1


# -----------------------------
# 9. Comparação for vs while
# -----------------------------
# Use FOR quando:
# - Você sabe quantas vezes vai repetir
# - Está percorrendo listas, strings, range
#
# Use WHILE quando:
# - Depende de uma condição
# - Não sabe o número de repetições


# -----------------------------
# RESUMO RÁPIDO (ESTILO PROVA)
# -----------------------------
# - while executa enquanto a condição for True
# - É necessário controlar a variável de repetição
# - break encerra o laço
# - continue pula a iteração
# - while pode ter else
# - Loops infinitos ocorrem se a condição nunca for falsa