# MINI JOGO - ADIVINHE O NÚMERO

import random
jogar = "s"
nivel = 0
cont = 0
placar = []

while jogar == "s":
    # jogadorr escolhe o nivel de dificuldade
    dificuldade = input("🎮Ecolha o nivel - 🐣 facil - 🐱 medio - 🐉 dificil: ")
    # cada nivel trás uma quantidade maior de possibilidades
    if dificuldade == "facil":
        al = random.randint(1, 10)
        nivel = 10
        vida = 10
    elif dificuldade == "medio":
        al = random.randint(1, 50)
        nivel = 50
        vida = 5
    elif dificuldade == "dificil":
        al = random.randint(1, 100)
        nivel = 100
        vida = 3
    else:
        print("❌comando invalido")
        break
    # variavel para contar tentativas
    tentativas = 1
    valor = int(input(f"🤔 adivinhe o numero entre 1 e {nivel}: "))

    while cont < vida:
        cont += 1
        # da dicas se o valor é maior ou menor
        if valor < al:
            print("🔼tente de novo com um valor maior")
        else:
            print("🔽tente de novo com o valor menor")

        valor = int(input("👉 valor: "))
        tentativas += 1

    if valor == al:
        print(f"\n🎉parabens vc acertou em {tentativas} tentativas🎯")
    else:
        print("GAME OVER!")

    # guarda o nome e numeros de tentativas do jogador
    nome = input("digite seu nome: ")
    placar.append({"nome": nome, "tentativa": tentativas})
    # placar.append(tentativas)

    # mantem ou não o laço
    jogar = input("quer continuar jogando: (s/n): ")

print("\n🏆 TOP 3 MELHORES JOGADORES 🏆")
trofeus = ["🥇", "🥈", "🥉"]
# ordena o placar pelas tentativas (menor = melhor)
placar.sort(key=lambda var: var["tentativa"])

for i in range(min(3, len(placar))):
    print(f"{trofeus[i]} {i+1}° lugar {placar[i]['nome']}")
