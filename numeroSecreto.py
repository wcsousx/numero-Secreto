import random

numeroSecreto = random.randint(1, 100)

tentativasMaximas = 5

print("Bem-vindo ao jogo de adivinhação!")
print("Tente adivinhar o número que estou pensando entre 1 e 100. Você tem {tentativasMaximas} tentativas.")

for tentativa in range(1, tentativasMaximas + 1):
    palpite = int(input("Tentativa {tentativa}: Qual é o seu palpite? "))
    
    if palpite < numeroSecreto:
        print("Muito baixo!")
    elif palpite > numeroSecreto:
        print("Muito alto!")
    else:
        print("Parabéns! Você acertou o número em {tentativa} tentativa(s).")
        break
else:
    print("Que pena! Você não conseguiu adivinhar o número. O número secreto era {numeroSecreto}.")
