contatos = []

def adicionar_contato(contatos, nome, telefone, email, favorito):
    boolean_favorito = True if favorito.lower() == 's' else False

    contato = {
        'nome': nome,
        'telefone': telefone,
        'email': email,
        'favorito': boolean_favorito
    }

    contatos.append(contato)
    return

def ver_contatos(contatos, somente_favoritos=False):
    contatos_filtrados = contatos if not somente_favoritos else \
                [contato for contato in contatos if contato['favorito']]

    for indice, contato in enumerate(contatos_filtrados, start=1):
        nome = contato['nome']
        telefone = contato['telefone']
        email = contato['email']
        caracter_favorito = '✓' if contato['favorito'] else ''

        print(f"""{indice}. Nome: {nome} - Telefone: {telefone} - E-mail: {email} - Favorito: [{caracter_favorito}]""")
    return

def editar_contato(contatos, indice_contato, nome, telefone, email, favorito):
    indice_contato_ajustado = int(indice_contato) - 1

    if 0 <= indice_contato_ajustado < len(contatos):
        contato = contatos[indice_contato_ajustado]
        contato['nome'] = nome
        contato['telefone'] = telefone
        contato['email'] = email
        contato['favorito'] = True if favorito.lower() == 's' else False

        print(f"Contato '{indice_contato}' atualizado com sucesso")
    else:
        print('Índice de contato inválido')

    return

def alterar_favorito(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1

    if 0 <= indice_contato_ajustado < len(contatos):
        contato = contatos[indice_contato_ajustado]
        contato['favorito'] = not contato['favorito']
        texto = 'tornou-se favorito' if contato['favorito'] else 'não é mais favorito'
        print(f"Contato '{indice_contato}' {texto}")
    else:
        print('Índice de contato inválido')

    return

def apagar_contato(contatos, indice_contato):
    indice_contato_ajustado = int(indice_contato) - 1

    if 0 <= indice_contato_ajustado < len(contatos):
        contato = contatos[indice_contato_ajustado]
        contatos.remove(contato)
        print(f"Contato '{indice_contato}' foi removido")
    else:
        print('Índice de contato inválido')

    return

while True:
    print('\nMenu da agenda de contatos')
    print('1.Adicionar Contato')
    print('2.Ver Contatos')
    print('3.Editar Contato')
    print('4.Marcar/Desmarcar Contato como Favorito')
    print('5.Ver Contatos Favoritos')
    print('6.Apagar Contato')
    print('7.Sair')

    escolha = input('Digite a sua escolha: ')

    if escolha == '1':
        nome = input('Informe o nome do contato: ')
        telefone = input('Informe o telefone do contato: ')
        email = input('Informe o e-mail do contato: ')
        favorito = input('Informe se o contato é favorito? (S - SIM) ou (N - NÃO): ')

        adicionar_contato(contatos, nome, telefone, email, favorito)
    elif escolha == '2':
        ver_contatos(contatos)

    elif escolha == '3':
        ver_contatos(contatos)

        indice_contato = input('Informe o número do contato que deseja editar: ')
        nome = input('Informe o novo nome do contato: ')
        telefone = input('Informe o novo telefone do contato: ')
        email = input('Informe o novo e-mail do contato: ')
        favorito = input('Informe se ocontato é favorito? (S - SIM) ou (N - NÃO): ')
        editar_contato(contatos, indice_contato, nome, telefone, email, favorito)
    elif escolha == '4':
        ver_contatos(contatos)

        indice_contato = input('Informe o número do contato que deseja marcar ou desmarcar como favorito: ')
        alterar_favorito(contatos, indice_contato)
    elif escolha == '5':
        ver_contatos(contatos, somente_favoritos=True)

    elif escolha == '6':
        ver_contatos(contatos)

        indice_contato = input('Informe o número do contato que deseja apagar: ')
        apagar_contato(contatos, indice_contato)
    elif escolha == '7':
        break

print('Programa finalizado')
