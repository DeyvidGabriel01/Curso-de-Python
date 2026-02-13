# 📌 O QUE É UMA VARIÁVEL?
# Uma variável é um espaço na memória do computador usado para guardar um valor.
# Pensa nela como uma caixinha com nome onde você coloca um valor dentro.

# Exemplo:

idade = 18

#Aqui:

# idade → nome da variável
# = → recebe
# 18 → valor guardado

#👉 O sinal = não significa "igual".
# Ele significa "recebe".

# 🧠 Como o Python lê isso?
# Quando você escreve:

idade = 18

# O Python entende assim:

# "Crie uma variável chamada idade e coloque o valor 18 dentro dela."

# 📦 Tipos de valores (Tipos de dados)
# Uma variável pode guardar vários tipos de dados.

# 1️. INTEIRO (int)
# Números sem vírgula:

numero = 10
idade = 25

# 2️. FLOAT (decimal)
#Números com ponto:

altura = 1.75
peso = 70.5

# ⚠ Em Python usa ponto e não vírgula.

# 3️. STRING (str)
# Texto (sempre entre aspas):

nome = "João"
mensagem = "Olá mundo"


# Pode usar:

"texto"
'texto'

# 4️. BOOLEAN (bool)
# Valores lógicos:

ligado = True
desligado = False

# Só existem dois:

True
False

# 🔍 COMO DESCOBRIR O TIPO?
# Use type():

idade = 18
print(type(idade))

# 🔄 MUDANDO VALOR DA VARIAVEL
# Você pode mudar o valor quando quiser:

numero = 10
numero = 20

# Agora numero vale 20.

# ➕ OPERAÇÕES COM VARIÁVEIS
# Matemática
a = 10
b = 5

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b

# Com strings
nome = "Gabriel"
sobrenome = "Silva"

nome_completo = nome + " " + sobrenome

# 🎯 REGRAS PARA NOME DE VARIÁVEIS

# ✅ Pode:

# Letras
# Números (não no começo)
# Underscore _

idade2 = 20
nome_completo = "Ana"


# ❌ Não pode:

# Começar com número
# Ter espaço
# Usar palavras reservadas

# Errado:

# 2idade = 10
# nome completo = "João"
# if = 10

# 🏷 BOAS PRÁTICAS (MUITO IMPORTANTE)
# Use nomes claros:

# ❌ Ruim:

x = 10


# ✅ Melhor:

quantidade_de_vidas = 10

# 🔄 VARIÁVEIS RECEBEM RESULTADO INPUT ()
nome = input("Digite seu nome: ")

# ⚠ Importante:
# O input() sempre retorna string.
# Se quiser número:

idade = int(input("Digite sua idade: "))

# 🔁 VARIAVEIS E CONDIÇÕES (if)
idade = 18

if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# Aqui a variável está sendo usada para decisão.

# 🔄 VARIÁVEIS E LOOP
for numero in range(5):
    print(numero)

# numero é uma variável que muda a cada repetição.

# 🧠 VARIÁVEL É DIFERENTE DE VALOR
# Isso é MUITO importante:

a = 10
b = a


# Aqui:

# a vale 10
# b recebe o valor de a

# Se mudar a depois:

a = 20


# b continua valendo 10.

# 📚 MÚLTIPLAS VARIÁVEIS DE UMA VEZ
a, b, c = 1, 2, 3

# 🔁 TROCAR VALORES 
a = 10
b = 20

a, b = b, a


# Agora:

# a vale 20
# b vale 10

# 🔒 Variável constante (conceito)
# Python não tem constante de verdade, mas usamos letras maiúsculas:

PI = 3.14


# Isso significa:

"Não deveria mudar"

# Mas tecnicamente pode.

# 🧩 ESCOPO (IMPORTANTE PARA AVANÇAR)
# Variáveis podem existir em lugares diferentes.

# Variável global
x = 10

def teste():
    print(x)

# Variável local
def teste():
    y = 5
    print(y)# 


# y só existe dentro da fun#ção.

#⚠ Erros comuns com variáveis
# ❌ Usar antes de criar
print(x)


# Erro:

# NamEError

# ❌ Misturar tipos
numero = 10
texto = "5"

resultado = numero + texto  # ERRO


# Precisa converter:

resultado = numero + int(texto)

# 🏗 O QUE É UMA VARIÁVEL POR TRÁS DOS BASTIDORES?

# Tecnicamente:

# Python cria um objeto na memória
# A variável é só uma referência para esse objeto
# Mas isso é  nível intermediário.

# 🎯 Resumo final

# Variável é:

# Um nome que guarda um valor na memória.

# Ela pode:

# Guardar números
# Guardar textos
# Guardar valores lógicos
# Mudar de valor
# Ser usada em contas
# Ser usada em decisões
# Ser usada em loops  