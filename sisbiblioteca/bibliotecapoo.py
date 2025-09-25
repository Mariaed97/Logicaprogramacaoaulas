import json
import os


class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def __str__(self):
        return f"{self.titulo} - {self.autor}"


class Biblioteca:
    ARQUIVO = "biblioteca.json"

    def __init__(self):
        self.livros = self.carregar_dados()

    def carregar_dados(self):
        # get = serve pra ler(lembrete)
        if os.path.exists(self.ARQUIVO):
            with open(self.ARQUIVO, "r", encoding="utf-8") as f:
                dados = json.load(f)
                return [Livro(livro.get("titulo", ""), livro.get("autor", "")) for livro in dados]
        return []

    def salvar_dados(self):
        # Salva os livros no JSON
        with open(self.ARQUIVO, "w", encoding="utf-8") as f:
            json.dump([livro.__dict__ for livro in self.livros], f, indent=4, ensure_ascii=False)

    def cadastrar_livro(self):
        titulo = input("Título do livro: ")
        autor = input("Autor: ")
        novo_livro = Livro(titulo, autor)
        self.livros.append(novo_livro)
        self.salvar_dados()
        print("Livro cadastrado com sucesso!")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro cadastrado.")
            return
        print("\n=== LISTA DE LIVROS ===")
        for i, livro in enumerate(self.livros, start=1):
            print(f"{i}. {livro}")
        print()

    def atualizar_livro(self):
        self.listar_livros()
        if not self.livros:
            return
        try:
            num = int(input("Digite o número do livro que deseja atualizar: "))
            if 1 <= num <= len(self.livros):
                livro = self.livros[num - 1]
                livro.titulo = input(f"Novo título ({livro.titulo}): ") or livro.titulo
                livro.autor = input(f"Novo autor ({livro.autor}): ") or livro.autor
                self.salvar_dados()
                print("Livro atualizado com sucesso!")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

    def excluir_livro(self):
        self.listar_livros()
        if not self.livros:
            return
        try:
            num = int(input("Digite o número do livro que deseja excluir: "))
            if 1 <= num <= len(self.livros):
                self.livros.pop(num - 1)
                self.salvar_dados()
                print("Livro excluído com sucesso!")
            else:
                print("Numero inválido.")
        except ValueError:
            print("Entrada invalida.")


class SistemaBiblioteca:
    def __init__(self):
        self.biblioteca = Biblioteca()

    def menu(self):
        while True:
            print("=== SISTEMA DE BIBLIOTECA ===")
            print("1 - Cadastrar livro")
            print("2 - Listar livros")
            print("3 - Atualizar livro")
            print("4 - Excluir livro")
            print("0 - Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                self.biblioteca.cadastrar_livro()
            elif opcao == "2":
                self.biblioteca.listar_livros()
            elif opcao == "3":
                self.biblioteca.atualizar_livro()
            elif opcao == "4":
                self.biblioteca.excluir_livro()
            elif opcao == "0":
                print(" Encerrando o sistema...")
                break
            else:
                print(" Opção inválida. Tente novamente.")


if __name__ == "__main__":
    app = SistemaBiblioteca()
    app.menu()
