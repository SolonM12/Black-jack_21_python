from random import randint

Sair = ""
vez = 0

while True:
    # Baralhos
    A = 11
    J, Q, K = 10, 10, 10
    baralhoOuro = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
    baralhoCopas = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
    baralhoEspadas = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
    baralhoPaus = [A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K]
    baralho = [baralhoOuro, baralhoPaus, baralhoCopas, baralhoEspadas]

    # funções

    def voltar():
        return input('pressione ENTER para voltar')


    def continuar():
        return input('Pressione ENTER para continuar...')


    def mostrarCartas():
        print(f'\tCartas do Dealer: {maoDealer}')
        print(f'\tSuas cartas:{maoJogador}')


    def adicionarCarta(jogador, repetir=1):
        for n in range(repetir):
            x = randint(0, 3)
            i = len(baralho[x]) - 1
            y = randint(0, i)
            jogador.append(baralho[x][y])
            del (baralho[x][y])


    def verificarAs(tresAs):
        if A in tresAs:
            for a in tresAs:
                soma = sum(tresAs)
                while soma > 21:
                    if a == 11:
                        valor = tresAs.index(A)
                        tresAs[valor] = 1
                        break
                    else:
                        pass
        return tresAs


    def verificarVitoria(mao1, mao2, vitoria='semvitorias'):
        suaMao = sum(mao1)
        maoOponente = sum(mao2)
        if suaMao > 21:
            vitoria = 'voceEstourou'
        elif maoOponente > 21:
            vitoria = 'oponenteEstourou'
        elif suaMao == 21:
            vitoria = 'voceFez21'
        elif maoOponente == 21:
            vitoria = 'Oponentefez21'
        elif suaMao > maoOponente:
            vitoria = 'vantagemSuaMao'
        elif maoOponente > suaMao:
            vitoria = 'vantagemOponente'
        elif suaMao == maoOponente:
            vitoria = 'empate'
        return vitoria

    # Variáveis

    vez += 1
    maoDealer = []
    maoJogador = []
    somaJogador = 0
    somaDealer = 0

    # Começa o jogo

    print()
    if vez > 1:
        Dealer = input('Deseja jogar novamente? [S]/[N]').lower()
    else:
        Dealer = input('Vamos jogar 21? [S]/[N]').lower()
    if Dealer == 's':
        while somaJogador < 21 and somaDealer < 21:
            somaJogador = sum(maoJogador)
            somaDealer = sum(maoDealer)
            # Distribui duas cartas para cada um
            adicionarCarta(maoJogador, repetir=2)
            adicionarCarta(maoDealer, repetir=2)
            # Verifica regra do ás para jogador apenas
            verificarAs(maoJogador)
            print(f'\tCartas do Dealer: [{maoDealer[0]}, ?]')
            print(f'\tSuas cartas:{maoJogador}')
            # verificar vitória
            analise1 = verificarVitoria(maoJogador, maoDealer)
            if analise1 == 'voceFez21' and (10 == maoDealer[0] or 11 == maoDealer[0]):
                print('Blackjack!!!, vamos ver a outra carta do Dealer!')
                continuar()
                verificarAs(maoDealer)
                print(f'\tCartas do Dealer: {maoDealer}')
                print(f'\tSuas cartas: {maoJogador}')
                somaJogador = sum(maoJogador)
                somaDealer = sum(maoDealer)
                analiseBJ = verificarVitoria(maoJogador, maoDealer)
                if somaDealer == somaJogador:
                    print(
                        'incrível!!! Este é um empate raríssimo chamado "push" onde ambos jogadores fazem um '
                        'Blackjack de primeira!')
                    voltar()
                    break
                elif somaDealer < somaJogador:
                    print('Parabéns você venceu com um Blackjack!!!')
                    voltar()
                    break
                else:
                    print(f'Erro!, análise retornou: "{analiseBJ}", Jogador:{maoJogador}, Dealer{maoDealer}')
            elif analise1 == 'voceFez21':
                print('Blackjack!!! Você venceu!!!')
                voltar()
            elif analise1 == 'vantagemSuaMao' or analise1 == 'vantagemOponente' or analise1 == 'empate' or analise1 == 'Oponentefez21':
                Dealer = input('Oque deseja fazer? Comprar[C], Parar[P]').lower()
                while Dealer != 'c' and Dealer != 'p':
                    print('Por favor, responda com "P"ou "C".')
                    Dealer = input('Oque deseja fazer? Comprar[C], Parar[P]').lower()
                while Dealer == 'c':
                    adicionarCarta(maoJogador)
                    print(f'\tCartas do Dealer: [{maoDealer[0]}, ?]')
                    print(f'\tSuas cartas:{maoJogador}')
                    somaJogador = sum(maoJogador)
                    if somaJogador > 21:
                        print('Que pena! Você estourou!')
                        v = voltar()
                        break
                    if somaJogador == 21:
                        print('Blackjack vamos ver a outra carta do Dealer.')
                        continuar()
                        mostrarCartas()
                        somaDealer = sum(maoDealer)
                        if somaDealer == 21:
                            print('Senhoras e senhores temos um empate!!!')
                            v = voltar()
                            break
                        else:
                            print('Você venceu!!! Meus parabéns!!!')
                            v = voltar()
                            break
                    Dealer = input('Oque deseja fazer? Comprar[C], Parar[P]').lower()
                if Dealer == 'p':
                    print('Você parou! Aqui está a outra carta do dealer:')
                    verificarAs(maoDealer)
                    mostrarCartas()
                    analise2 = verificarVitoria(maoJogador, maoDealer)
                    if analise2 == 'vantagemOponente':
                        print('Sinto muito! O dealer venceu!')
                        voltar()
                        break
                    elif analise2 == 'Oponentefez21':
                        print('O Dealer fez um Blackjack!!! Você perdeu amigo')
                        voltar()
                        break
                    print('Vez da casa!')
                    continuar()
                    somaDealer = sum(maoDealer)
                    while somaDealer < 17:
                        adicionarCarta(maoDealer)
                        verificarAs(maoDealer)
                        somaDealer = sum(maoDealer)
                        somaJogador = sum(maoJogador)
                        print(f' O Dealer comprou: {maoDealer[-1]}. ')
                        mostrarCartas()
                        if somaDealer > 21:
                            print('O Dealer estourou! Você venceu!!!')
                            voltar()
                            break
                        continuar()
                    if somaDealer > 21:
                        break
                    analise3 = verificarVitoria(maoJogador, maoDealer)
                    if analise3 == 'vantagemSuaMao':
                        print('Parabéns você venceu essa rodada!!!')
                        voltar()
                        break
                    elif analise3 == 'vantagemOponente':
                        print('Que pena, você perdeu essa rodada!!!')
                        voltar()
                        break
                    elif analise3 == 'empate':
                        print('Senhoras e senhores, essa rodada foi um empate!!!')
                        voltar()
                        break
                    else:
                        print(f'Erro!, análise 3 retornou: "{analise3}", Jogador:{maoJogador}, Dealer{maoDealer}')
            else:
                print(f'Erro!, análise 1 retornou: "{analise1}", Jogador:{maoJogador}, Dealer{maoDealer}')
    elif Dealer == 'n':
        Sair = input('Deseja sair? [S]/[N]').lower()
    else:
        print('por favor responda com sim ou não')
    if Sair == 's':
        break