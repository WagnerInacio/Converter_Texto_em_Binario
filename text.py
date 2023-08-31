def text_to_binary(text):
    binary_result = ' '.join(format(ord(char), '08b') for char in text)
    return binary_result

def binary_to_text(binary):
    binary_list = binary.split()
    text_result = ''.join(chr(int(binary, 2)) for binary in binary_list)
    return text_result

# Exemplo de uso
input_text = input("Digite o texto: ")
binary_representation = text_to_binary(input_text)
print("Texto em binário:", binary_representation)

converted_text = binary_to_text(binary_representation)
print("Texto convertido de binário:", converted_text)
