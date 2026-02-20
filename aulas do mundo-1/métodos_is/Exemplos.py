# 📌 O QUE SÃO MÉTODOS .IS?
# São métodos das strings (str) usados para verificar características do texto.

# Eles sempre:

# Retornam True ou False
# São usados para validação
# Não alteram a string
# Só funcionam em strings

# ⚠ MUITO IMPORTANTE
# Eles só existem para string.

# Se fizer isso:

# numero = 10
# numero.isdigit()

# Vai dar erro.
# Porque int não tem .isdigit().

# 🧠 ESTRUTURA GERAL
# texto.isalguma_coisa()

# Exemplo:

nome = "Gabriel"
print(nome.isalpha())

# Agora vamos um por um.


# 🔢 1️⃣ .ISDIGIT()
# Verifica se a string contém apenas números inteiros positivos.

print("123".isdigit())   # True
print("12a".isdigit())   # False
print("12.5".isdigit())  # False
print("-10".isdigit())   # False

# ⚠ Ele NÃO aceita:

# número negativo
# decimal
# espaço


# 🔢 2️⃣ .ISNUMERIC()
# Parecido com isdigit(), mas mais amplo.

print("123".isnumeric())  # True

# Aceita alguns caracteres numéricos especiais.


# 🔤 3️⃣ .ISALPHA()
# Verifica se contém apenas letras.

print("Gabriel".isalpha())   # True
print("Gabriel123".isalpha()) # False
print("Gabriel Silva".isalpha()) # False

# ⚠ Não aceita:

# números
# espaço


# 🔡 4️⃣ .ISALNUM()
# Verifica se contém apenas:

# Letras
# Números

print("Gabriel123".isalnum())  # True
print("Gabriel 123".isalnum()) # False (tem espaço)


# 🔠 5️⃣ .ISLOWER()
# Verifica se todas as letras estão minúsculas.

print("python".islower())   # True
print("Python".islower())   # False


# 🔠 6️⃣ .ISUPPER()
# Verifica se todas as letras estão maiúsculas.

print("PYTHON".isupper())   # True
print("Python".isupper())   # False


# 🅰 7️⃣ .ISTITLE()
# Verifica se está no formato "Título".

# Ou seja:
# Primeira letra de cada palavra maiúscula.

print("Python Programacao".istitle())  # True
print("Python programacao".istitle())  # False


# 🧪 8️⃣ .ISSPECE()
# Verifica se a string contém apenas espaços.

print("   ".isspace())   # True
print(" a ".isspace())   # False

# Muito útil para validar input() vazio.


# 📦 9️⃣ .ISIDENTIFIER()
# Verifica se a string pode ser usada como nome de variável.

print("nome".isidentifier())   # True
print("1nome".isidentifier())  # False
print("nome_1".isidentifier()) # True

# Isso é mais avançado, mas muito interessante.


# 🧠 DIFERENÇA IMPORTANTE: .ISDIGIT() vs .ISNUMERIC()
# Na prática, para iniciantes:

# Use .isdigit().

# Mas saiba:

#.isnumeric() é mais abrangente.


# 🔥 USO REAL COM INPUT()
# Isso aqui é MUITO importante para você:

numero = input("Digite um número: ")

if numero.isdigit():
    numero = int(numero)
    print("Número válido")
else:
    print("Digite apenas números!")

# Isso evita erro de ValueError.


# 🧠 LIMITAÇÃO IMPORTANTE
# Se o usuário digitar:

# -10

# .isdigit() retorna:

# False

# Porque o - não é número.


# 🧠 OUTRA LIMITAÇÃO
# Se digitar:

# 12.5

# Também retorna:

# False

# Porque o ponto não é dígito.


# 🧩 VALIDAÇÃO MAIS AVANÇADA (NÍVEL ACIMA)
# Para aceitar número negativo ou decimal, geralmente usamos:

try:
    numero = float(input("Digite um número: "))
    print("Número válido")
except:
    print("Número inválido")

# Mais profissional.


# 📊 RESUMO GERAL
# Método	        Verifica
# isdigit()	        Apenas números inteiros positivos
# isnumeric()	    Caracteres numéricos
# isalpha()	        Apenas letras
# isalnum()	        Letras e números
# islower()	        Tudo minúsculo
# isupper()	        Tudo maiúsculo
# istitle()	        Formato título
# isspace()	        Apenas espaços
# isidentifier()	Nome válido de variável


# 🧠 ALGO MUITO IMPORTANTE

# Todos os .is:

# Retornam True ou False
# Não modificam a string
# Funcionam só em string
