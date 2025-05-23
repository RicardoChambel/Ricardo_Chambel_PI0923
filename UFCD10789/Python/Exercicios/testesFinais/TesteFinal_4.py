""" 
Criar um programa em Python para gerenciar um catálogo de até 100 livros. 
O programa deve permitir as seguintes operações: 
    > Cadastrar livros no catálogo: 
        - Título 
        - Autor
        - Ano de publicação. 
    > Procurar por livros por:
        - Título
        - Autor 
        O programa deve exibir as posições onde o livro foi encontrado e mostrar o 
        conteúdo correspondente. 
    > Excluir livros partir da sua posição no catálogo: 
        A posição será dada pelo índice do livro na lista. 
    > Ordenar os livros cadastrados por:
        - Título
        - Autor
    > Listar todos os livros cadastrados exibindo:
        - Título
        - Autor
        - Ano 
    > Sair do programa

Menu do Programa: 
    O programa deve apresentar um menu com as seguintes opções: 
        > Adicionar novo livro 
        > Procurar por título ou autor 
        > Ordenar livros 
        > Listar livros 
        > Excluir livro 
        > Sair do Programa 
 
Requisitos: 
    O programa deve permitir a execução contínua das operações, retornando sempre ao menu principal após cada ação. 
    As operações de busca, exclusão e ordenação devem ser realizadas com base nas listas de títulos e autores. 
    O programa deve garantir que não sejam cadastrados mais de 100 livros. 
    Adicionar a possibilidade de verificar se o livro já está cadastrado antes de permitir o cadastro. 
 
8 pontos do teste estão destinados a: 
 - (2) Criar Algoritmos de procura e de validação. 
 - (2) Funções e reutilização das mesmas. 
 - (1) Utilização de boas praticas e standards. 
 - (1) Uso de Exceções.
"""

import os # uso isto para apagar a consola e deixar mais legivel ao utilizador

escolha=0
econtrado=0 # Usado na procura de livros
livroIndex=0
limite=100

livros=[]
livro = {
    "titulo": "",
    "autor": "",
    "ano": ""
}
livroTitulo=""
livroAutor=""
livroAno=""

# Funcao para apagar a consola
def clearScreen():
    os.system("cls")

def showMenu():
    print("\n- Biblioteca Chambelita -")
    print(" [1] Adicionar Livro")
    print(" [2] Procurar Livro")
    print(" [3] Ordenar Livros")
    print(" [4] Listar Livros")
    print(" [5] Excluir Livro")
    print(" [0] Sair")

def addLivro():
    while True:
        clearScreen()
        print("- Novo Livro -")
        # Pedir os atributos para o livro
        while True: # Titulo
            livroTitulo = input("Titulo do livro -> ")
            if livroTitulo != "":
                for livro in livros:
                    if livro["titulo"]==livroTitulo:
                        clearScreen()
                        print("- Ja existe um livro com esse titulo! -")
                        return
                break
            else:
                print("- Nome fantasma?! -")
        while True: # Autor
            livroAutor = input("Autor do livro -> ")
            if livroAutor != "":
                break
            else:
                print("- Autor fantasma?! -")
        while True: # Ano
            try:
                livroAno = int(input("Ano do livro -> "))
                break
            except:
                print("- Ano Invalido! -")
            
        # Criar o livro com os atributos recebidos com estrutura de um dicionario
        livro = {
            "titulo": livroTitulo,
            "autor": livroAutor,
            "ano":livroAno
        }
        livros.append(livro) # Adicionar o livro à lista de livros
        
        # Limpar o cmd, mostrar que o livro foi adicionado e voltar ao menu
        clearScreen()
        print("- Livro Adicionado! -\n")
        return

def procurarLivro():
    while True:
        clearScreen()
        if not livros:
            print("- Ainda nao existem livros registados! -")
            return
        print("- Procurar Livro -")
        print("[1] Procurar por Titulo")
        print("[2] Procurar por Autor")
        print("[0] Cancelar")
        try:
            escolha=int(input(">"))
            clearScreen()
            match escolha:
                case 1:
                    print("- Procurar Livro (Por Titulo) -")
                    escolha=input("Titulo a procurar:")
                    livroIndex=0
                    for livro in livros:
                        if livro['titulo']==escolha:
                            print("- Livro encontrado! -")
                            print(f"Posicao  [{livroIndex}]")
                            print(f"Titulo -> {livro['titulo']}")
                            print(f"Autor -> {livro['autor']}")
                            print(f"Ano -> {livro['ano']}")
                            return
                        livroIndex+=1
                    print("- Livro não encontrado! -")
                    return
                case 2:
                    print("- Procurar Livro (Por Autor) -")
                    escolha=input("Autor a procurar:")
                    for livro in livros:
                        if livro['autor']==escolha:
                            econtrado=1
                            print("- Livro encontrado -")
                            print(f"Titulo -> {livro['titulo']}")
                            print(f"Autor -> {livro['autor']}")
                            print(f"Ano -> {livro['ano']}")
                    
                    if econtrado!=1:
                        clearScreen()
                        print("- Livros nao encontrados -")
                        return
                    return
                    
                case 0:
                    return
                case _:
                    print("- Opcao Invalida -")
        except:
            clearScreen()
            print("- Valor invalido -")

def ordenarLivros():
    while True:
        clearScreen()
        if not livros:
            print("- Ainda nao existem livros registrados! -")
            return

        print("- Ordenar Livros -")
        print("[1] Ordenar por Titulo")
        print("[2] Ordenar por Autor")
        print("[0] Cancelar")
        try:
            escolha = int(input("> "))
            if escolha == 1:
                livros.sort(key=lambda livro: livro["titulo"].lower())
                clearScreen()
                print("- Livros ordenados por título! -")
                return
            elif escolha == 2:
                livros.sort(key=lambda livro: livro["autor"].lower())
                clearScreen()
                print("- Livros ordenados por autor! -")
                return
            elif escolha == 0:
                return
            else:
                print("- Opção invalida! -")
        except:
            print("- Valor invalido -")

def listarLivros():
    while True:
        clearScreen()
        if not livros:
            print("- Ainda nao existem livros registados! -")
            return
        print("- Livros (Titulos) -")
        livroIndex=0
        for livro in livros:
            print(f"- Livro {livroIndex}")
            print("> ", livro["titulo"])
            print("> ", livro["autor"])
            print("> ", livro["ano"])
            livroIndex+=1
        return

def excluirLivro():
    if not livros:
        print("- Ainda nao existem livros registrados! -")
        return
    while True:
        try:
            print("- Excluir Livro -")
            posicao = int(input("Posicao do livro no catalogo: "))

            if 0 <= posicao < len(livros):
                livro = livros[posicao]
                print("- Livro Encontrado! -")
                print(f"Título -> {livro['titulo']}")
                print(f"Autor -> {livro['autor']}")
                print(f"Ano -> {livro['ano']}")
                
                confirmacao = input("Pretende apagar o livro? (s/n): ").strip().lower()
                if confirmacao == "s":
                    livros.pop(posicao)
                    clearScreen()
                    print("- Livro excluido com sucesso! -")
                    return
                else:
                    clearScreen()
                    print("- Cancelado -")
                    return
            else:
                clearScreen()
                print("- Livro nao encontrado! -")
                return
        except ValueError:
            print("- Valor invalido! -")  

def main():
    while True:
        showMenu()
        try:
            escolha=int(input(">"))
            match escolha:
                case 1: # Adicionar um livro
                    if len(livros) != limite:
                        addLivro()
                    else:
                        clearScreen()
                        print("- Limite de 100 livros atingido! -")
                case 2: # Procurar por livro
                    procurarLivro()
                case 3: # Ordenar livros
                    ordenarLivros()
                case 4: # Listar livros
                    listarLivros()
                case 5: # Excluir livro
                    excluirLivro()
                case 0: # Sair
                    print("\n- Ate a proxima! -")
                    break
                case _: # (Default)
                    print("\n- Escolha Inválida -")
        except:
            print("- Valor invalido -\n")
        
if __name__ == "__main__":
    main()