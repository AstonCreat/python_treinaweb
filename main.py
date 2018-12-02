from usuario import Usuario
#todos recursos
# import usuario


continuar = 1
list_user = []

while continuar != 0:
    try:
        nome = input("Digite o seu nome: ")
        idade = int(input("Digite o sua idade: "))
        sobrenome = input("Digite o seu sobrenome: ")

        usuario = Usuario(nome, idade, sobrenome)
        list_user.append(usuario)

        if idade == 99:
            break
        if idade == 98:
            continue
        print(f"Olá, {usuario.nome} {usuario.sobrenome}, sua idade é {usuario.idade}")

        if idade <= 17:
            print(f"{usuario.nome} é adolescente")
        elif idade >= 18 and idade <= 50:
            print(f"{usuario.nome} é adulto")
        else:
            print(f"{usuario.nome} é idoso")
        continuar = int(input("Deseja continuar cadastrando 0 - para sair 1 - cadastrar:"))

    except ValueError:
        print("Você deve informa um numero válido")
else:
    print("Lista de usuários cadastrados: ")
    for lt in list_user:
        print(f"Nome completo: {lt.nome} {lt.sobrenome} - Idade {lt.idade}")

    print("O loop entrou em else")


