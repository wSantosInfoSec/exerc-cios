#brute force

mensagem_roubada = input("Cole aqui o texto cifrado (o lixo visual): ")

# Vamos tentar chaves de 1 a 20
for tentativa_chave in range(1, 21):
    texto_tentativa = ""
    
    for letra in mensagem_roubada:
        # Faz a engenharia reversa (subtrai a chave em vez de somar)
        numero_novo = ord(letra) - tentativa_chave
        texto_tentativa = texto_tentativa + chr(numero_novo)
    
    # Mostra o resultado para ver se faz sentido
    print(f"Tentando chave {tentativa_chave}: {texto_tentativa}")

print("---------------------------------------")
print("Ataque finalizado. Análise das palavras")
