# atividade biblioteca com json
import json
import os

ARQUIVO = "biblioteca.json"


def carregar_dados():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return []


def salvar_dados(livros):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(livros, f, indent=4, ensure_ascii=False)


def cadastrar_livro(livros):
    titulo = input("Título do livro: ")
    autor = input("Autor: ")

    livro = {"titulo": titulo, "autor": autor}
    livros.append(livro)
    salvar_dados(livros)
    print("Livro cadastrado com sucesso!")


def listar_livros(livros):
    if not livros:
        print("Nenhum livro cadastrado.")
        return

    print("=== LISTA DE LIVROS ===")
    for i in range(len(livros)):
         livro = livros[i]
         print(f"{i+1}. {livro['titulo']} - {livro['autor']}")

def atualizar_livro(livros):
    listar_livros(livros)
    if not livros:
        return
    try:
        num = int(input("Digite o número do livro que deseja atualizar: "))
        if 1 <= num <= len(livros):
            livro = livros[num - 1]
            livro["titulo"] = input(f"Novo título ({livro['titulo']}): ") or livro["titulo"]
            livro["autor"] = input(f"Novo autor ({livro['autor']}): ") or livro["autor"]
            salvar_dados(livros)
            print("Livro atualizado com sucesso!")
        else:
            print(" Número inválido.")
    except ValueError:
        print("Entrada inválida.")


def excluir_livro(livros):
    listar_livros(livros)
    if not livros:
        return
    try:
        num = int(input("Digite o número do livro que deseja excluir: "))
        if 1 <= num <= len(livros):
            livros.pop(num - 1)
            salvar_dados(livros)
            print("Livro excluído com sucesso!")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada inválida.")


def menu():
    livros = carregar_dados()
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1 - Cadastrar livro")
        print("2 - Listar livros")
        print("3 - Atualizar livro")
        print("4 - Excluir livro")
        print("5 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_livro(livros)
        elif opcao == "2":
            listar_livros(livros)
        elif opcao == "3":
            atualizar_livro(livros)
        elif opcao == "4":
            excluir_livro(livros)
        elif opcao == "5":
            print("Encerrando o sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()

