print('\33[0;49;34mSeja bem vindo (a) ao portal MedUni\33[m')
print('Para se cadastrar: ')
usuario = input('Digite um nome de usuário:  ')
senha = input('Digite sua senha: ')

print('\n'*90)
print('Obrigado por se cadastrar! ')
login = str(input('Deseja fazer login? \33[49;92m S/N \33[m')).upper()
if login == "N":
    print('A MedUni agradece! ')
if login == "S":
    while True:
        log = input('Digite seu nome de usuário cadastrado: ')
        if log == usuario:
            sen = input('Digite sua senha:')
            if sen != senha:
                print('\33[49;31mSenha incorreta! Digite novamente: \33[m')
            if sen == senha:
                print('Seja bem vindo(a) ao portal do cliente MedUni! ')
                print('1- Agendar consultas')
                print('2- Em breve!')
                print('3- Em breve!')
                print('4- Em breve!')
                print('5- Em breve!')
                op = int(input('Digite a opção desejada: '))
                if op == 1:
                    print('1- Clínico Geral')
                    print('2- Pediátra')
                    print('3- Fonodiólgo')
                    print('4- Dermatologista')
                    op1 = int(input('Digite a opção desejada:'))
                    if op1 == 1:
                        print('Dr Carlos Alberto')
            break
        if log != login:
            print('Usuario não encontrado na base de dados UNIMED! ')




