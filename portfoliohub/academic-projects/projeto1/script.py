# script.py
# Um pequeno programa que soma números até que o usuário digite "fim"

print("Digite números para somar. Digite 'fim' para terminar.")
soma = 0
while True:
    entrada = input("Número: ")
    if entrada.lower() == "fim":
        break
    try:
        soma += float(entrada)
    except ValueError:
        print("Entrada inválida. Digite um número ou 'fim'.")
print(f"Soma total: {soma}")
