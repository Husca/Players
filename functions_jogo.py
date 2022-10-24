def jogo():
    while True:
        opt = input("Deseja A) inserir um jogador,B) ver a lista de jogadores ou C) para sair? ")

        if opt.upper() == "A":

            nome = input("Qual o nome do jogador? ")
            clube = input("Qual o clube que joga? ")
            altura = input("Qual a sua altura em cm? ")
            assistencias = input("Qual o seu número de assistências? ")

            player_tip = input("A) Jogador de Futebol, B) Jogador de Basket, C) outro? ")

            if player_tip.upper() == "A":

                golos = input("Qual o número de golos? ")
                penalties = input("Qual o número de penalties que marcou? ")

                novo_jogador = FutebolPlayer(nome=nome, clube=clube, altura=altura, penalties=penalties, golos=golos,
                                             assistencias=assistencias)

                with open("bd_jogadores.txt", "w") as file:
                    file.write(str(novo_jogador.__dict__))

            elif player_tip.upper() == "B":

                cestos = input("Qual o número de cestos? ")

                novo_jogador = BasketPlayer(nome=nome, clube=clube, altura=altura, cestos=cestos,
                                            assistencias=assistencias)

                with open("bd_jogadores.txt", "w") as file:
                    file.write(str(novo_jogador.__dict__))

            else:
                print("Tipo de jogador não reconhecido")
                continue

        elif opt.upper() == "B":

            with open("bd_jogadores.txt", "r") as file:
                lista_jogadores = file.read()
                print(lista_jogadores)

        elif opt.upper() == "C":
            print("Programa terminado")
            break

        else:
            print("Opção não reconhecida")
            print("Por favor repita")
            continue
