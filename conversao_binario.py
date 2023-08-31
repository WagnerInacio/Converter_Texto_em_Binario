"""
Código para converter binário em textos

"""

def binary_to_text(binary_string):
    binary_values = binary_string.split()  # Divide a sequência em valores binários separados por espaços
    text_result = ''.join(chr(int(binary, 2)) for binary in binary_values)
    return text_result

# Exemplo de uso
binary_input = input("Digite a sequência binária: ")
text_output = binary_to_text(binary_input)
print("Texto convertido:", text_output)