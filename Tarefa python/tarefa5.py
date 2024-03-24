def calcular_preco(preco_original, desconto_percentual):
    desconto = desconto_percentual / 100
    preco_final = preco_original - (desconto)
    return preco_final

def main():
    preco_original = float(input("Me diga o preço do produto: R$"))
    desconto_percentual = float(input("Qual o desconto percentual do produto (%): "))

    preco_final = calcular_preco(preco_original, desconto_percentual)

    print(f"O preço final do produto após aplicar um desconto de {desconto_percentual}% é: R${preco_final:.2f}")

if __name__ == "__main__":
    main()