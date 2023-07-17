# SISTEMA DE BANCO 
import time

menu = """ 

**** MENU ****

[d] Deposito
[s] Saque
[e] Extrato
[q] Sair
 

***********

"""



saldo = 0 
limite = 500
extrato = ''
numero_saque = 0
limite_saque = 3 

#Solicitar nome do cliente para localizar sua conta 

nome = input('Digite seu nome: ')
if nome == "":
    print("****** Digite seu nome correto ******")
    
    
    
else:    
    print("Localizando sua conta aguarde....")
    time.sleep(3)

    print(f'Conta localizada')
    print(f"Olá {nome.upper().strip()}, seja bem-vindo a sua conta")
    print(f'Seu saldo é R${saldo}')
   
    


    # Menu de condições 

    while True: 

        # Opção do menu 
        opcao = input(f'Selecione a opção desejada {menu}:')

        #Deposito

        if opcao == "d":
            print('Realizando Operação...')
            time.sleep(2)
            valor = int(input('Digite o valor do deposito?: R$ '))

            #Regra para deposito
            if valor > 0:
                print('Realizando Operação....')
                time.sleep(2)
                print("***Deposito Realizado Com Sucesso***")
                saldo += valor
                extrato += (f'Deposito: R$ {valor:.2f} Seu limite de saque é R$ {limite}')

            else:
             print(f'Operação Invalida')

             # saque

        elif opcao == "s":
            print('Realizando Operação....')
            time.sleep(2)
            valor = int(input("Digite o valor do saque? R$ "))

            excedeu_saldo = valor > saldo
            excedeu_limite = valor > limite
            excedeu_saques = numero_saque == limite_saque 

            # Regras de saque
            if excedeu_saldo:
             print('Realizando Operação....')
             time.sleep(2)
             print('Não há saldo suficente para essa operação')

            elif excedeu_limite:
              print('Realizando Operação....')
              time.sleep(2)
              print('Falha na Operação***Operação excedeu o limite de *** R$500.00 por saque')

            elif excedeu_saques:
               print('Realizando Operação....')
               time.sleep(2)
               print('Falha na Operação***Operação excedeu o limite de *** 3 saques Diarios')


               # Finalizando saque 
            elif valor > 0:
               print('Realizando Operação....')
               time.sleep(2)
               print('***Saque Realizado Com Sucesso***')
               saldo -= valor
               extrato += ('Saque: R$ {valor:.2f}')
               numero_saque += 1

            else:
               print('Falha na operação***Tente de Novo')   
           
           # Extrato 

        elif  opcao == "e": 
            print('Realizando Operação....')
            time.sleep(2)
            print(f'''Saldo total em conta: **R${saldo:.2f}**\n\nLimite de **R$ {limite}** por saque\n\nLimite de ** 3 ** saques diarios disponiveis\n\nSaques realizados **{numero_saque}** de 3 Disponiveis ''') 
          


          # finalizando sistema (Sair do sistema)
        elif opcao == "q":
         print('***Realizando Operação***')
         time.sleep(2)
         print('***Obrigado por utilizar nosso banco***')
         print('***Volte sempre***')
         time.sleep(1)
         break

           


        
                  

                 
       
           
               

           