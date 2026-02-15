# 📌 O QUE É F-STRING?

# f-string significa formatted string literal.
# É uma forma moderna (e melhor) de colocar variáveis dentro de textos.
# Ela surgiu no Python 3.6.

# 🧠 ESTRUTURA BÁSICA 
variavel = "Oi"
print(f"texto {variavel}")

# A letra f antes das aspas ativa o modo especial.

# 📦 EXEMPLO SIMPLES
nome = "Gabriel"
print(f"Olá, {nome}")

# Saída:

# Olá, Gabriel


# ❓ POR QUE USAR F-STRING?
# Antes dela, usávamos:

# ❌ FORMA ANTIGA 1 – CONCATENAÇÃO
print("Olá, " + nome)


# Problema:
# Não funciona direto com números
# Fica feio em textos grandes

# ❌ FORMA ANTIGA 2 – FORMAT()
print("Olá, {}".format(nome))

# Funciona, mas é menos prático.

# ✅ f-string é:
# Mais limpa
# Mais rápida
# Mais profissional
# Mais legível


# 🔢 USANDO NÚMERO
idade = 20
print(f"Você tem {idade} anos")

# Não precisa converter com str().


# ➕ FAZENDO CONTAS DENTRO DA F-STRING
# Você pode colocar expressões dentro das chaves:
a = 10
b = 5

print(f"Soma: {a + b}")

# Saída:
# Soma: 15

# Isso é muito poderoso.


# 🔄 USANDO FUNÇÕES DENTRO
nome = "gabriel"
print(f"Nome em maiúsculo: {nome.upper()}")


# 🎯 MÚLTIPLAS VARIÁVEIS
nome = "Ana"
idade = 25
altura = 1.70

print(f"Nome: {nome} | Idade: {idade} | Altura: {altura}")


# 🎨 FORMATANDO NÚMEROS (PARTE IMPORTANTE)
# Aqui começa o nível mais interessante.

# 🔹 CASAS DECIMAIS
pi = 3.14159265
print(f"{pi:.2f}")

# Saída:
# 3.14

# Explicação:
# : → começa formatação
# .2 → duas casas decimais
# f → float


# 🔹 MOSTRA PORCENTAGEM
valor = 0.25
print(f"{valor:.0%}")

# Saída:
# 25%


# 🔹 SEPARADOR DE MINHAR
numero = 1000000
print(f"{numero:,}")

# Saída:
# 1,000,000


# 🔹 ALINHAMENTO
# Alinhar à direita
print(f"{'Python':>10}")

# Alinhar à esquerda
print(f"{'Python':<10}")

# Centralizar
print(f"{'Python':^10}")


# 🔹 COMPLETAR COM CARACTERE
print(f"{'7':0>5}")

# Saída:
# 00007

# Muito usado para:
# Número de pedido
# Códigos
# IDs


# 🧪 USANDO DENTRO DE LOOP
for i in range(5):
    print(f"Número atual: {i}")


# 🧠 DEBUG MODERNO (MUITO USADO)
# Python permite isso:

x = 10
print(f"{x=}")

# Saída:
# x=10

# Excelente para testes.


# ⚠ ERROS COMUNS
# ❌ Esquecer o f
# print("Olá {nome}")


# Isso NÃO funciona.
# Tem que ser:

print(f"Olá {nome}")

# ❌ Usar variável que não existe
print(f"{idade}")

# Se idade não existir → erro.


# 🆚 F-STRING VS PRINT COM VÍRGULA
print("Nome:", nome)

# Funciona.

# Mas f-string é melhor quando:

# Texto é grande
# Tem várias variáveis
# Precisa formatar número

# 🔥 POR QUE PROFICIONAIS PREFEREM F-STRING?
# Porque ela:

# É mais rápida que .format()
# É mais legível
# Permite expressões
# Permite formatação avançada
# É padrão moderno


# 🏗 O QUE ACONTECE POR TRÁS?
# Quando você escreve:

f"Olá {nome}"


# O Python:

# 1. Avalia o que está dentro das { }
# 2. Converte para string automaticamente
# 3. Insere no texto final

# 🎯 RESUMO FINAL

# f-string serve para:
# Colocar variáveis dentro de texto
# Fazer contas dentro do texto
# Format ar números
# Organizar alinhamento
# Facilitar debug
# Escrever código mais limpo