#Logica E (and)
#logica do login
#email e a senha sejam true

verifica_email = True
verifica_senha = False

verifica_login = verifica_email and verifica_senha
print(verifica_login)

if verifica_login:
    print("Entrar no programa")

    #logica ou(or)

    logica_ou = False or False or False
    print(logica_ou)

    #NOT
    negacao = not True
    print(negacao)

    if not verifica_senha:
        print("senha incorreta hein....")

        #ESCOLHER USUARIO

        match escolha_usuario:
        case 0:
        print("Sair do programa")
        case 1:
        print("Entrar no programa")