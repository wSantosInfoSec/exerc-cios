def encriptar(texto, chave):
    resultado = ""
    
    for letra in texto:
        #Transforma a letra em numero (codigo ASCII)
        numero_original = ord(letra)
        
        # Soma a chave (O "Segredo")
        numero_novo = numero_original + chave
        
        #Transforma o numero novo de volta em letra
        nova_letra = chr(numero_novo)
        
        #Junta
        resultado = resultado + nova_letra
# comando ord(transforma em asc pro pc somar), comando  chr(reverte o processo)
    return resultado

print("--- SISTEMA DE CRIPTOGRAFIA SIMÉTRICA ---")
mensagem = input("Digite a mensagem secreta: ")
segredo = int(input("Digite a chave numérica (ex: 5): "))

texto_cifrado = encriptar(mensagem, segredo)

print("\n--------------------------------")
print(f"TEXTO PURO (Plaintext): {mensagem}")
print(f"TEXTO CIFRADO (Ciphertext): {texto_cifrado}")
print("--------------------------------")
