# Programa para inverter os caracteres de um texto

def inverte_string(original):
    invertida = ''
    for char in original:
        invertida = char + invertida
    return invertida

# Exemplo com um texto escolhido pelo usuario (pode ser modificada)
string_teste = "DiegoEstagiario"
resultado = inverte_string(string_teste)
print(resultado)