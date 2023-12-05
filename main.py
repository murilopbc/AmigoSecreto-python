import random

print("Bem-Vindo ao Amigo Secreto!")

participantes_amigo_secreto = []

while True:
    try:
        opt = int(input("Digite '1' para adicionar, '2' para remover, '3' para sortear ou '4' para sair: "))

        if opt == 1:
            nome = input("Digite o nome do participante: ")
            if nome in participantes_amigo_secreto:
                print("Esse nome já se encontra na lista!")
            else:
                participantes_amigo_secreto.append(nome)
                print(f"{nome} adicionado. Participantes atuais: {participantes_amigo_secreto}")
        elif opt == 2:
            nome_remover = input("Digite o nome que deseja remover da lista: ")
            if nome_remover in participantes_amigo_secreto:
                participantes_amigo_secreto.remove(nome_remover)
                print(f"{nome_remover} removido. Participantes atuais: {participantes_amigo_secreto}")
            else:
                print("Nome não encontrado na lista. Digite novamente!")
        elif opt == 3:
            if len(participantes_amigo_secreto) < 3:
                print("É necessário pelo menos três pessoas para realizar o sorteio.")
            else:
                nomes_sem_repetir = list(set(participantes_amigo_secreto.copy()))
                while True:
                    random.shuffle(nomes_sem_repetir)
                    sorteios = list(zip(participantes_amigo_secreto, nomes_sem_repetir))

                    if all(a != b for a, b in sorteios):
                        for nome, amigo_secreto in sorteios:
                            print(f"{nome}, você sorteou {amigo_secreto}")
                        break
        elif opt == 4:
            print("Saindo do programa. Até a próxima!")
            break
        else:
            print("Opção inválida! Digite 1, 2, 3 ou 4.")
    except ValueError:
        print("Valor Inválido! O valor esperado é um número inteiro.")
