from dados import filmes
from utils import titulo

def listar_filmes():
    titulo("CATÁLOGO")
    
    if not filmes:
        print("Nenhum filme cadastrado.")
        return
    
    for filme in filmes:
        disp = "Sim" if filme['disponivel'] else "Não"
        print(f"""
Título     : {filme['titulo']}
Gênero     : {filme['genero']}
Ano        : {filme['ano']}
Disponível : {disp}
""")


def cadastrar_filme():
    titulo("CADASTRAR FILME")
    
    nome = input("Título: ").strip()
    genero = input("Gênero: ").strip()
    
    try:
        ano = int(input("Ano: "))
    except ValueError:
        print("Digite um ano válido.")
        return
    
    filme = {
        "titulo": nome,
        "genero": genero,
        "ano": ano,
        "disponivel": True
    }
    
    filmes.append(filme)
    print(f"'{nome}' cadastrado!")


def alugar_filme():
    titulo("ALUGAR FILME")
    
    nome = input("Qual filme? ").strip().lower()
    
    for filme in filmes:
        if filme["titulo"].lower() == nome:
            if filme["disponivel"]:
                filme["disponivel"] = False
                print(f"'{filme['titulo']}' alugado!")
            else:
                print("Indisponível.")
            return
    
    print("Filme não encontrado.")


def devolver_filme():
    titulo("DEVOLVER FILME")
    
    nome = input("Qual filme? ").strip().lower()
    
    for filme in filmes:
        if filme["titulo"].lower() == nome:
            if not filme["disponivel"]:
                filme["disponivel"] = True
                print(f"'{filme['titulo']}' devolvido!")
            else:
                print("Já estava disponível.")
            return
    
    print("Filme não encontrado.")