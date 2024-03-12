def inverter_string(s):
    tamanho = len(s)
    string_invertida = [''] * tamanho

    for i in range(tamanho):
        string_invertida[i] = s[tamanho - 1 - i]

    return ''.join(string_invertida)

# Exemplo de utilização
entrada_usuario = input("Digite uma string: ")
resultado = inverter_string(entrada_usuario)

print("String original:", entrada_usuario)
print("String invertida:", resultado)