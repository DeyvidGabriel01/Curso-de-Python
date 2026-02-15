# 📌 O QUE É INPUT()?

# input() é uma função usada para receber dados do usuário pelo teclado.

# Ou seja:

# Enquanto o print() mostra algo
# o input() recebe algo

# 🧠 ESTRUTURA BÁSICA
input("Mensagem")

# Exemplo:

nome = input("Digite seu nome: ")


# O que acontece:

# 1. O Python mostra: Digite seu nome:
# 2. O programa pausa
# 3. O usuário digita algo
# 4. O valor digitado é guardado na variável


# 🔑 MUITO IMPORTANTE
# 👉 O input() sempre retorna STRING
# Mesmo se o usuário digitar um número.

# Exemplo:

idade = input("Digite sua idade: ")

# Se a pessoa digitar:

18

# O Python guarda:

"18"

# Não é número. É texto.


# 🔢 CONVERTENDO PARA NÚMERO
# Se quiser número, precisa converter.

# Para inteiro:
idade = int(input("Digite sua idade: "))

# Para decimal:
altura = float(input("Digite sua altura: "))


# ⚠ ERRO COMUM
# Se fizer isso:

numero = input("Digite um número: ")
print(numero + 10)

# Vai dar erro.
# Porque é string + número.
# Forma correta:

numero = int(input("Digite um número: "))
print(numero + 10)


# 🔄 INPUT + PRINT
# Exemplo completo:

nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")

# 🧩 INPUT DENTRO DE CONDIÇÃO (IF)
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Aqui o input() influencia a decisão.


# 🔁 INPUT DENTRO DE LOOP 
# Exemplo:

while True:
    numero = int(input("Digite um número (0 para sair): "))
    
    if numero == 0:
        break

# Aqui o programa continua pedindo até digitar 0.

# GUARDANDO VÁRIOS IMPUTS
nome = input("Nome: ")
idade = int(input("Idade: "))
cidade = input("Cidade: ")


# 🧠 O QUE ACONTECE POR TRÁS?
# Quando você usa:

input("Digite algo: ")

# O Python:
# 1. Mostra a mensagem
# 2. Espera o usuário digitar
# 3. Captura o texto digitado
# 4. Retorna como string


# 🔍 INPUT SEM MENSAGEM 
#  Você pode fazer:

valor = input()

# Mas não é recomendado, porque o usuário não sabe o que deve digitar.


# 🎯 INPUT0 + SPRIT()
# Muito usado quando o usuário digita vários valores na mesma linha.

# Exemplo:

# Usuário digita:

# 10 20

# Código:

a, b = input("Digite dois números: ").split()


# Isso separa pelo espaço.
# Se quiser números:

a, b = map(int, input("Digite dois números: ").split())

# Isso já converte para inteiro.


# ⚠ ERRO COMUNS COM INPUT
# ❌ Esquecer de converter
numero = input()
print(numero + 5)  # ERRO

# ❌ Digitar letra quando espera número
idade = int(input("Idade: "))

# Se digitar:

# abc

# Vai dar erro:

# ValueError


# 🛡 TRATANDO ERRO (NÍVEL INTERMEDIÁRIO)
try:
    idade = int(input("Digite sua idade: "))
except:
    print("Digite apenas números!")

# Isso evita o programa quebrar.


# 🔥 DIFERENÇA ENTRE INPUT E VARIÁVEL NORMAL
# Sem input:
idade = 18

# Com input:
idade = int(input("Digite sua idade: "))

# Aqui o valor só é decidido quando o usuário digita.

# 🧠 RESUMO DEFINIDO

# input() serve para:
# Receber dados do usuário
# Pausar o programa
# Sempre retorna string
# Precisa converter se quiser número
# Pode ser usado com if, for, while
#Pode dividir dados com split()