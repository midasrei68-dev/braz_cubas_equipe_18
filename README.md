dados.py
É para mostra os filmes disponiveis ou não, de generos de terror ,ação , mistério, comédia. 
filmes = Lista de filmes com os dicionários
fila_reservas = Lista para reservas (primeiro que entra, primeiro que sai)
pilha_devolucoes = Lista para devoluções (último que entra, primeiro que sai)

Utils.py
Funções simples que ajudam outras funções.
como criar textos, Imprimir uma linha de = (40 caracteres)
Centraliza e imprime o texto.

tarefas.py
Mostrar um título "CATÁLOGO"
Verifique se a lista está vazia
Se não estiver, mostre TODOS os filmes
Para cada filme, mostra: título, gênero, ano e disponibilidade.
basicamente, 1 listar_filmes, 2 cadastrar_filme, 3 alugar_filme, 4 devolver_filme.

main.py
O menu que empregada tudo.Importa todas as funções detarefas.py
Entre em um loop infinito ( while = "loop"  True = "verdade")
Mostrar um menu com 5 opções
Pede a escolha do usuário
Executa a função correspondente
Se você apertar 0, sai do loop e encerra
