# 📌 O QUE É TYPE()?
# type() é uma função embutida do Python que mostra o tipo de um valor ou variável.

# Exemplo:
print(type(10))

# Saída:
# <class 'int'>

# 🧠 O QUE ISSO SIGNIFICA?
# Quando você vê:

# <class 'int'>

# Significa que o valor pertence à classe int.
# Em Python:

# Tudo é objeto
# E todo objeto tem um tipo (classe)


# 📦 EXEMPLOS BÁSICOS
print(type(10))        # int
print(type(3.14))      # float
print(type("Olá"))     # str
print(type(True))      # bool


# 🔎 USANDO COM VARIÁVEIS
idade = 18
print(type(idade))


# ⚠ MUITO IMPORTANTE (LIGADO AO INPUT)
numero = input("Digite algo: ")
print(type(numero))

# Mesmo digitando 10, o resultado será:

# <class 'str'>

# Isso explica muitos erros de iniciante.


# 🧠 PYTHON É DINAMICAMENTE TIPADO
# Você não declara o tipo.
# O Python decide automaticamente:

x = 10
print(type(x))  # int

x = "Python"
print(type(x))  # str

# A mesma variável mudou de tipo.


# 🎯 PARA QUE TYPE() É USADO NA PRÁTICA?

# Principalmente para:
# Debug (descobrir erro)
# Entender por que uma operação falhou
# Aprender como o Python está interpretando o valor


# 🧩 COMPARANDO TIPOS 
# Você pode fazer:

x = 10

if type(x) == int:
    print("É inteiro")

# Mas ⚠ isso não é a melhor prática.


# 🚀 FORMA MAIS PROFISSIONAL: isinstance()
# Melhor do que:

type(x) == int

# É usar:

isinstance(x, int)

# Exemplo:

x = 10

print(isinstance(x, int))  # True

# Por quê?
# Porque isinstance() funciona melhor com herança (nível mais avançado).


# 🧠 TYPE() COM COLEÇÕES
# Mesmo que você ainda não esteja estudando isso profundamente, veja:

print(type([1,2,3]))   # list
print(type((1,2,3)))   # tuple
print(type({1,2,3}))   # set
print(type({"a":1}))   # dict

# Tudo tem tipo.


# 🔥 USANDO TYPE() DENTRO DE F-STRING
x = 5
print(f"O tipo é {type(x)}")


#  ⚠ CUIDADO IMPORTANTE
# Isso aqui:

print(type(10) == int)

# Retorna:

# True

# Mas isso aqui:

print(type(True))

# Mostra:

# <class 'bool'>

# E aqui vem algo interessante:

print(isinstance(True, int))

# Isso retorna:

# True

# 🤯 Por quê?
# Porque bool é uma subclasse de int.

# Em Python:

# True vale 1
# False vale 0

# Isso é algo que pouca gente explica.


# 🧠 TYPE() COM DOIS ARGUMENTOS (MODO AVANÇADO)
# type() também pode ser usado para criar classes dinamicamente:

MinhaClasse = type("MinhaClasse", (), {})

# Mas isso é programação avançada (metaprogramação).
# Para seu nível atual, não precisa focar nisso.


# 🏗 RESUMO COMPLETO

# type():

# Mostra o tipo de um valor
# Retorna a classe do objeto
# Ajuda a debugar
# Mostra como o Python está interpretando algo
# Não converte tipo (só informa)


# 📌 DIFERENÇA IMPORTANTE
# Função	    | Faz o quê?
# type()	    | Mostra o tipo
# int()	        | Converte para inteiro
# str()	        | Converte para string
# float()	    | Converte para decimal
# isinstance()	| Verifica tipo (forma melhor)


