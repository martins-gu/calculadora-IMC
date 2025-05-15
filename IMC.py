peso = float(input("Digite o seu peso: "))
altura =float(input("Digite o sua altura: "))

imc = peso / (altura * altura)

print(f"o imc é: {imc: .1f}")

if imc <18.5:
    print("Magro")
elif imc >=18.5 and imc <=24.9:
    print("Peso Normal")
elif imc >25:
    print("Sobrepeso")