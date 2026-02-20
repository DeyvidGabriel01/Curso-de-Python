# 📌 O QUE SÃO TIPOS PRIMITIVOS?
# Tipos primitivos são os tipos básicos de dados que o Python usa para representar informações simples.

# Eles são a base de tudo.

# Em Python, os principais tipos primitivos são:

# int
# float
# str
# bool


# 🔢 1️⃣ INT (INTEIRO)
# Representa números inteiros (sem parte decimal).

# Exemplos:

idade = 18
ano = 2025
saldo = -50

# Características:

# Pode ser positivo ou negativo
# Pode ser muito grande (Python suporta inteiros grandes)

# Operações comuns:

a = 10
b = 3

print(a + b)  # soma
print(a - b)  # subtração
print(a * b)  # multiplicação
print(a // b) # divisão inteira
print(a % b)  # resto
print(a ** b) # potência


# 🔢 2️⃣ FLOAT (DECIMAL)
# Representa números com casas decimais.

# Exemplos:

altura = 1.75
preco = 19.99
temperatura = -3.5

# ⚠ Usa ponto, não vírgula.

numero = 2.5
print(type(numero))

# Operações funcionam normalmente:

a = 5.0
b = 2

print(a / b)

# 🔤 3️⃣ STR (String)
# Representa texto.

# Exemplos:

nome = "Gabriel"
cidade = 'São Paulo'

# Características:

# Sempre entre aspas simples ou duplas
# Pode conter letras, números e símbolos

# Operações com string
# Concatenar
nome = "Ana"
sobrenome = "Silva"

print(nome + " " + sobrenome)

# Repetir texto
print("Python " * 3)

# Tamanho da string
nome = "Gabriel"
print(len(nome))


# 🔘 4️⃣ BOOL (BOOLEANO)
# Representa valores lógicos.

# Só existem dois:

True
False

# Exemplos:

ligado = True
ativo = False

# Muito usado em condições:

idade = 18
print(idade >= 18)

# Isso retorna:

True

# 🧠 Comparações geram boolean
print(10 > 5)   # True
print(3 == 4)   # False
print(7 != 2)   # True


# Operadores importantes:

# == igual
# != diferente
# > maior
# < menor
# >= maior ou igual
# <= menor ou igual


# 🔄 CONVERSÃO DE TIPOS (CASTING)
# Muito importante.

# Converter para inteiro
numero = int("10")

# Converter para float
numero = float("3.14")

# Converter para string
idade = 20
texto = str(idade)

# Converter para bool
print(bool(1))   # True
print(bool(0))   # False
print(bool(""))  # False
print(bool("A")) # True

#Regras gerais:

# 0 → False
# "" → False
# vazio → False
# resto → True


# ⚠ MISTURA DE TIPOS
# Isso dá erro:

# print("Idade: " + 18)

# Porque:
#String + int → incompatíve

# Forma correta:

print("Idade:", 18)

# Ou:

print(f"Idade: {18}")


# 🧩 TIPOS E INPUT()
# Lembra disso (muito importante):

idade = input("Digite sua idade: ")

# Mesmo digitando 18, o tipo será:

# str

# Por isso usamos:

idade = int(input("Digite sua idade: "))


# 🧠 COMO O PYTHON TRATA TIPOS ?
# Python é dinamicamente tipado.

# Isso significa:

# Você não precisa declarar o tipo
# O tipo é definido automaticamente

# Exemplo:

x = 10      # int
x = "Oi"    # agora virou string


# Isso é permitido.

# 🧠 Checando tipo
print(type(10))        # int
print(type(3.5))       # float
print(type("Oi"))      # str
print(type(True))      # bool

# 🏗 Resumo estrutural
# Tipo  |  Guarda |  Exemplo
# int   | inteiro |   10
# float | decimal |  3.14
# str   |  texto  | "Python"
# bool  | lógico  |  True


