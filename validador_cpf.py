from random import randint
import os

entrada = 1
while entrada != 3:
    entrada = int(input("O que você quer fazer? \n"\
                f'1 - Gerar CPF \n'\
                f'2 - Validar CPF \n'
                f'3 - Sair '))
    if entrada == 1:
        digitos=[]
        #Gerando 9 números aleatórios
        for i in range(0,9):
            digitos.append(randint(0,9))

        #Números para multiplicação dos digitos
        algoritmo = [10,9,8,7,6,5,4,3,2]

        #Variavél total soma que irá armazena o resultado de cada multiplicação
        total_soma=[]

        #For para multiplicar os itens das duas listas
        for i in range(0,len(digitos)):
            #Adicionando a lista total_soma o valor de todas as multiplicações
            total_soma.append(digitos[i] * algoritmo[i])

        #Somanando todos os valores da lista total_soma
        total = sum(total_soma)

        #Multiplicando o total dos valores por 10
        total = total*10

        #Módulo de total por 11 / Resulta em 4
        digito = total % 11
        #Caso o módulo acima seja maior que 9 o dígito será igual a 0
        if digito > 9:
            digito = 0

        #Adicionando o primeiro digito após o traço '-' do nosso cpf
        digitos.append(digito)

        #Criando uma variável para armazenar o nosso cpf
        digitos_2 = ''

        #Armazenando os números do cpf na nossa variável
        for i in range(0,len(digitos)):
            digitos_2 += str(digitos[i])

        #Formatando nosso cpf ex.: 123.456.789.1
        formatacao_10digitos = digitos_2[:3]+'.'+digitos_2[3:6]+'.'+digitos_2[6:9]+'-'+digitos_2[9:10]

        ############################################################################################################
        ############################################################################################################
        ############################################################################################################
        #Gerando nosso Segundo dígito verificador

        #Atribuindo mais um valor ao nosso algoritmo, já que adicionamos mais um número ao nosso
        #gerador de cpf
        #algoritmo = [10,9,8,7,6,5,4,3,2]
        algoritmo.insert(0,11)
        #[11,10,9,8,7,6,5,4,3,2]

        #resetando os valores para gerar o Segundo dígito verificador
        total_soma = []
        total = []
        #For para multiplicar os itens das duas listas
        for i in range(0,len(digitos)):
            #Adicionando a lista total_soma o valor de todas as multiplicações
            total_soma.append(digitos[i] * algoritmo[i])
        #Somanando todos os valores da lista total_soma
        total = sum(total_soma)
        #Multiplicando o total dos valores por 10
        total = total*10
        #Módulo de total por 11 / Resulta em 4
        digito = total % 11
        if digito > 9:
            digito = 0
        #Adicionando nosso segundo digito aos digitos
        digitos.append(digito)

        #criando variável para armazenar todos os digítos
        digitos_3 =''

        #Armazenando os digitos
        for i in range(0,len(digitos)):
            digitos_3 += str(digitos[i])
        #Formatando nosso cpf ex.: 123.456.789.12

        formatacao_11digitos = digitos_3[:3]+'.'+digitos_3[3:6]+'.'+digitos_3[6:9]+'-'+digitos_3[9:11]
        os.system('cls')
        print("Gerando cpf.....\n"
              f'########################################\n'
              f'##########-> {formatacao_11digitos} <-##########\n'
              f'########################################\n'
              f'{40*"="}\n'
              f'Cpf gerado com sucesso\n'
              f'{40*"="}')
        continue

    if entrada == 2:
        os.system('cls')
        print(f'########################################\n'
              f"##########->VALIDADOR DE CPF <-##########\n"
              f'########################################\n')
        
        cpf = input("Digite seu cpf sem pontos ou traços. Ex:12345678912\n")
        cpf_formatado10 = cpf[0:9]
        cpf_digito10= cpf[9:10]
        print(cpf_digito10)

        digitos10 = list(cpf_formatado10)
        algoritmo10 = [10,9,8,7,6,5,4,3,2]
        total_soma10 = []

        for i in range(0,len(digitos10)):
            total_soma10.append(int(digitos10[i]) * algoritmo10[i])

        total10= sum(total_soma10)
        total10 = total10*10
        digito10 = total10 % 11
        if digito10>9:
            digito10 = 0


        if digito10 == int(cpf[9:10]):
            cpf_formatado11 = cpf[0:10]
            cpf_digito11= int(cpf[10:11])

            digitos11= list(cpf_formatado11)
            algoritmo11 = [11,10,9,8,7,6,5,4,3,2]
            total_soma11 = []

            for i in range(0,len(digitos11)):
                total_soma11.append(int(digitos11[i]) * algoritmo11[i])

            total11 = sum(total_soma11)
            total11 = total11*10
            digito11 = total11 % 11
            if digito11>9:
                digito11 =0
            if digito11 == cpf_digito11:
                os.system('cls')

                print(f'{40*"="}\n'
              f'O cpf: {cpf} é valido\n'
              f'{40*"="}')
                continue
            else:
                os.system('cls')

            
                print(f'{40*"="}\n'
              f'Esse cpf é inválido\n'
              f'{40*"="}')
                continue
        else:
            os.system('cls')
            print(f'{40*"="}\n'
              f'Esse cpf é inválido\n'
              f'{40*"="}')
            continue
    if entrada ==3:
        print("saindo.....")
        break
    else: 
        print("Erro, digite um valor válido")
        continue
