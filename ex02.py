def verifica_fibonacci(numero):
    a, b = 0, 1

    while b < numero:
        a, b = b, a + b

    if b == numero:
        return True
    else:
        return False

# Solicita um número ao usuário
numero_informado = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

# Verifica se o número pertence à sequência de Fibonacci
if verifica_fibonacci(numero_informado):
    print(f"{numero_informado} pertence à sequência de Fibonacci.")
else:
    print(f"{numero_informado} não pertence à sequência de Fibonacci.")
