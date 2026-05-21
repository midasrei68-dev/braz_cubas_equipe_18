from tarefas import *

while True:
    print("""
1 - Listar Filmes
2 - Cadastrar Filme 
3 - Alugar Filme
4 - Devolver Filme
0 - Sair
""")

    opcao = input("Escolha: ")

    if opcao == "1":
        listar_filmes()
    elif opcao == "2":
        cadastrar_filme()
    elif opcao == "3":
        alugar_filme()
    elif opcao == "4":
        devolver_filme()
    elif opcao == "0":
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida.")