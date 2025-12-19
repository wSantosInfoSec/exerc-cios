import hashlib
# Importar a biblioteca de Hash

print("--- CRIANDO CONTA ---")
senha_cadastro = input("Crie sua senha: ")

#o sistema destrói a senha, nunca guarda a senha em plaintext
hash_no_banco = hashlib.sha256(senha_cadastro.encode()).hexdigest()

print(f"Salvando no Banco de Dados: {hash_no_banco}")
print("(Note que eu joguei a senha original fora! Só guardei o lixo visual)")

print("\n--------------------------\n")
#\n aqui é quebra de linha,\t da um tab
print("--- TELA DE LOGIN ---")
senha_tentativa = input("Digite sua senha para entrar: ")

# Para conferir eu tenho que transformar em hash a tentativa tambem para comparar as hashs
hash_da_tentativa = hashlib.sha256(senha_tentativa.encode()).hexdigest()


if hash_no_banco == hash_da_tentativa:
    print(">>> ACESSO PERMITIDO! Os hashes sao iguais.")
else:
    print(">>> ACESSO NEGADO! Os hashes sao diferentes.")
