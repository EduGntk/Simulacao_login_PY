#printa o nome do programa
print("Bem vindo ao MaxUse\n")
#"banco de dados" onde ficarão guardadas as informações de login
conta={}
#variáveis de cadastro
email=""
senha=""
n=""
conta.update({n:[email, senha]})


#o usuário escolhe se vai logar ou cadastrar
anuncio=int(input("Logar (1) ou Cadastrar (2): "))
#se escolher cadastrar, roda este codigo


if anuncio==2:
    print("\nCadastre sua conta para o nosso app!\n")
    #o usuário digita as informações de login
    n=(input("Digite seu nome para o perfil: "))
    email=str(input("Digite seu email: "))
    senha=input("Digite sua senha (utilize no mínimo 4 caracteres): ")
    senha2=input("Digite sua senha novamente: ")
    #se as informações não estiverem vazias, o codigo rodará este pedaço
    if "@gmail.com" in email or "@hotmail.com" in email or "@camporeal.edu.br" in email or "@yahoo.com" in email:
        if email!="" and senha!="":
            #se as senhas coincidirem, o codigo rodará este pedaço
            if len(senha)>=4 and len(senha2)>=4:
                if senha==senha2:
                    print("Conta criada com sucesso!\n")
                    #o codigo adicionará a conta ao banco de dados
                    conta.update({n:[email, senha]})
                    #o usuário decide se vai continuar para o login
                    resp=str(input("Continuar para o login?"))
                    #se sim, o codigo roda esse pedaço
                    if resp=="sim" or resp=="Sim" or resp=="SIM" or resp=="s" or resp=="afirmativo":
                            print("\nDigite seus dados para realizar o login.")
                            #o usuário deve informar suas informações de login
                            email1=str(input("Digite seu email: "))
                            senha1=input("Digite sua senha: ")
                            #o codigo roda dentro do banco de dados
                            for i in conta[n]:
                                #se as informações coincidirem com o banco de dados, o usuário loga
                                if email1 in conta[n] and senha1 in conta[n]:
                                    print("Logado com sucesso!")
                                    break
                                #senão, o codigo informa o erro
                                else:
                                    print("Email ou senha errados ou conta inexistente, tente novamente.")
                                    break
                    else:
                        print("Cadastro finalizado.")
                #se as senhas forem incompatíveis, mostrará este erro
                else: 
                    print("Senhas incompatíveis.") 
            else:
                print("Senha muito curta, escolha uma senha mais forte")
        #se o usuario nao informar as infos, mostrará este erro
        else:
            print("Campo não preenchido, digite novamente.")
    else:
        print("Domínio inexistente ou incorreto. (utilize @gmail.com, por exemplo)")



#se o usuário escolher logar, roda essa parte
if anuncio==1:
    print("Digite seus dados para realizar o login.\n")
    #o usuario digita as infos de login
    email1=str(input("Digite seu email: "))
    senha1=input("Digite sua senha: ")
    #se os dados estiverem no banco de dados, o usuário conseguirá logar
    if email1!="" and senha1!="":
        for i in conta[n]:
            if email1 in conta[n] and senha1 in conta[n]:
                print("Logado com sucesso!")
                break
            #se não estiverem, mostrará este erro
            else:
                print("Email ou senha errados ou conta inexistente, tente novamente.")
                break
    else:
        print("Campo não preenchido, digite novamente.")