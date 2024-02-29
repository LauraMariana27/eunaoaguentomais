def dimensoesObj():
    while True:
        try:
            compObj = float(input("Informe o comprimento do objeto (cm): "))
            largObj = float(input("Informe a largura do objeto (cm): "))
            altObj = float(input("Informe a altura do objeto (cm): "))
            volume = compObj * largObj * altObj
            print("O volume do Objeto é de {} cm.".format(volume))

            if volume <= 1000:
                return 10.00
            elif volume <= 10000:
                return 20.00
            elif volume <= 30000:
                return 30.00
            elif volume <= 100000:
                return 50.00
            else:
                print("Volume do objeto acima do permitido!")
                continue
        except ValueError:
            print("Valor inválido. Digite um valor válido.")
            continue

def pesoObj():
    while True:
        try:
            peso = float(input("Informe o peso do Objeto (kg): "))

            if peso <= 0.1:
                return 1
            elif peso <= 1:
                return 1.5
            elif peso <= 10:
                return 2
            elif peso <= 30:
                return 3
            else:
                print("Peso acima do permitido!")
        except ValueError:
            print("Valor inválido. Digite um valor válido!")
            continue
def rotaObj():
    while True:
        rota = input("Selecione a rota desejada:"
        "\n CWB/SP - De Curitiba para São Paulo"
        "\n CWB/RJ - De Curitiba para Rio de Janeiro"
        "\n SP/CWB - De São Paulo para Curitiba"
        "\n SP/RJ - De São Paulo para Rio de Janeiro"
        "\n RJ/CWB - De Rio de Janeiro para Curitiba"
        "\n RJ/SP - De Rio de Janeiro para São Paulo"
        "\n Rota desejada: ")

        if rota == "CWB/SP" or rota == "cwbsp" or rota == "cwb/sp":
            return 1.2
        elif rota == "CWB/RJ" or rota == "cwbrj" or rota == "cwb/rj":
            return 1.5
        elif rota == "SP/CWB" or rota == "spcwb" or rota == "sp/cwb":
            return 1.2
        elif rota == "RJ/CWB" or rota == "rjcwb" or rota == "rj/cwb":
            return 1.5
        elif rota == "SP/RJ" or rota == "sprj" or rota == "sp/rj":
            return 1
        elif rota == "RJ/SP" or rota == "rjsp" or rota == "rj/sp":
            return 1
        else:
            print("Rota inexistente. Informe uma rota válida!")
            continue

print("------------------\n")
print("---Bem Vindo(a)---\n")
print("------------------\n")
volume = dimensoesObj()
peso = pesoObj()
rota = rotaObj()
total = volume * peso * rota
print(" ".format(volume, peso, rota))
print("Valor total do Frete: R$ {:.2f}"
    "\n Taxas: Volume {} x Peso {} x Rota {}".format(total, volume, peso, rota))