# 📌 O QUE É PRINT()?
# print() é uma função usada para mostrar algo na tela.

# Exemplo básico:

print("Olá mundo")

# Isso faz o programa exibir o texto no terminal.

# 🧠 O QUE É UMA FUNÇÃO?
# Uma função é algo que executa uma ação.

#No caso:
#print() → mostra algo na tela

# 📦 Estrutura do print
# print(valor)

# Você coloca dentro dos parênteses o que quer mostrar.
# Pode ser:

# Texto
# Número
# Variável
# Conta matemática
# Resultado de uma função


# 🧾 PRINT COM TEXTO (string)
print("Python é incrível")

# ⚠ Texto sempre entre aspas.


# 🔢 PRINT COM NÚMERO
print(10)
print(3.14)

# Não precisa de aspas.


# 📦 PRINT COM VARIÁVEL
nome = "Gabriel"
print(nome)

# Aqui ele mostra o valor guardado na variável.


# ➕ PRINT COM CONTA
print(10 + 5)

# Saída:
15

# Você pode fazer:

a = 10
b = 5
print(a + b)


# 🧩 MOSTRAR TEXTO + VARIÁVEL
# ⚠ Aqui muita gente erra.

# ❌ Errado:
# idade = 18
# print("Sua idade é " + idade)  # ERRO

# Erro porque está misturando string com inteiro.


# ✅ FORMA 1 – CONVERTENDO
idade = 18
print("Sua idade é " + str(idade))

# ✅ FORMA 2 – VÍGULA (mais simples)
idade = 18
print("Sua idade é", idade)

# O print automaticamente separa com espaço.

# ✅ FORMA 3 – F-STRING (FORMA PROFISSIONAL)

# A melhor forma:

idade = 18
print(f"Sua idade é {idade}")


# Isso é chamado de f-string.
# Muito usada profissionalmente.

# 🔄 VÁRIOS VALORES NO PRINT
nome = "Ana"
idade = 20

print(nome, idade)

# Saída:
# Ana 20


# ⚙ PARÂMETROS ESPECIAIS DO PRINT
# O print() tem configurações extras.

# Estrutura:
valor1 = "Olá"
valor2 = "Deyvid"
print(valor1, valor2, sep=" ", end="\n")

# Vamos entender isso.


#🔹 SEP (SEPARADOR)
# Define o que fica entre os valores.

# Padrão:

sep=" "
# (um espaço)

# Exemplo:

print("A", "B", "C", sep="-")

# Saída:
# A-B-C


# 🔹 END (FINAL DA LINHA)
# Por padrão:

end="\n"

# Isso significa que ele pula linha automaticamente.

# Exemplo:

print("Olá")
print("Mundo")

# Saída:
# Olá
# Mundo

# Se mudar o end:

print("Olá", end=" ")
print("Mundo")

# Saída:
# Olá Mundo


# 🧪 PRINT DENTRO DE LOOP (MUITO IMPORTANTE)

for i in range(5):
    print(i)

# Ele imprime a cada repetição.

# Se usar end:

for i in range(5):
    print(i, end=" ")

# Saída:
# 0 1 2 3 4


# 🔍 PRINT PARA DEPURAÇÃO (DEBUG)
# Programadores usam muito print() para testar código.

# Exemplo:

numero = 10
print("Valor de numero:", numero)

# Serve para verificar valores enquanto o programa rod


# 🔡 CARACTERES ESPECIAIS NO PRINT
# Quebra de linha manual

print("Olá\nMundo")

# Saída:
# Olá
# Mundo

# Tabulação
print("Nome:\tGabriel")

# Aspas dentro do texto
print("Ele disse: \"Olá\"")

# Ou:

print('Ele disse: "Olá"')

# 🧠 O QUE ACONTECE POR TRÁS
# Quando você usa:

print("Olá")

# O Python:
# Converte o valor para string (se precisar)
# Envia para a saída padrão (terminal)
# Aplica o separador
# Aplica o final de linha

# ⚠ ERROS COMUNS COM PRINT
# ❌ Esquecer parênteses
# print "Olá"  # ERRO

# Python 3 exige parênteses.


# ❌ Esquecer aspas
# print(Olá)  # ERRO

# Texto precisa de aspas.


# ❌ Misturar tipos sem converter
# print("Idade: " + 18)  # ERRO


# 🆚 DIFERENÇA ENTRE MOSTRAR E GUARDAR
# Isso é MUITO importante:

print(10 + 5)

# Isso apenas mostra o resultado.
# Não guarda.
# Se quiser guardar:

resultado = 10 + 5
print(resultado)

# 📌 Print vazio
print()

# Isso só pula uma linha.

# 🏁 Resumo geral

# print() serve para:
# Mostrar texto
# Mostrar números
# Mostrar variáveis
# Mostrar resultados
# Ajudar a testar código
# Controlar formatação com sep e end
# Usar f-string para formatação profissional