class Ferramenta:
    def __init__(self, id, nome, preco, quantidade):
        self.id = id
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def __str__(self):
        return f'ID: {self.id}, Nome: {self.nome}, Preço: R${self.preco:.2f}, Quantidade: {self.quantidade}'


class LojaDeFerramentas:
    def __init__(self):
        self.ferramentas = {}

    def criar_ferramenta(self, id, nome, preco, quantidade):
        if id in self.ferramentas:
            print("Ferramenta com este ID já existe.")
        else:
            ferramenta = Ferramenta(id, nome, preco, quantidade)
            self.ferramentas[id] = ferramenta
            print(f'Ferramenta {nome} criada com sucesso.')

    def ler_ferramentas(self):
        if not self.ferramentas:
            print("Nenhuma ferramenta cadastrada.")
        else:
            for ferramenta in self.ferramentas.values():
                print(ferramenta)

    def atualizar_ferramenta(self, id, nome=None, preco=None, quantidade=None):
        if id not in self.ferramentas:
            print("Ferramenta não encontrada.")
        else:
            ferramenta = self.ferramentas[id]
            if nome is not None:
                ferramenta.nome = nome
            if preco is not None:
                ferramenta.preco = preco
            if quantidade is not None:
                ferramenta.quantidade = quantidade
            print(f'Ferramenta {id} atualizada com sucesso.')

    def deletar_ferramenta(self, id):
        if id in self.ferramentas:
            del self.ferramentas[id]
            print(f'Ferramenta {id} deletada com sucesso.')
        else:
            print("Ferramenta não encontrada.")


def main():
    loja = LojaDeFerramentas()

    while True:
        print("\nMenu:")
        print("1. Criar ferramenta")
        print("2. Ler ferramentas")
        print("3. Atualizar ferramenta")
        print("4. Deletar ferramenta")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            id = input("ID da ferramenta: ")
            nome = input("Nome da ferramenta: ")
            preco = float(input("Preço da ferramenta: "))
            quantidade = int(input("Quantidade da ferramenta: "))
            loja.criar_ferramenta(id, nome, preco, quantidade)

        elif opcao == '2':
            loja.ler_ferramentas()

        elif opcao == '3':
            id = input("ID da ferramenta a ser atualizada: ")
            nome = input("Novo nome da ferramenta (ou deixe em branco para não alterar): ")
            preco = input("Novo preço da ferramenta (ou deixe em branco para não alterar): ")
            quantidade = input("Nova quantidade da ferramenta (ou deixe em branco para não alterar): ")

            loja.atualizar_ferramenta(
                id,
                nome if nome else None,
                float(preco) if preco else None,
                int(quantidade) if quantidade else None
            )

        elif opcao == '4':
            id = input("ID da ferramenta a ser deletada: ")
            loja.deletar_ferramenta(id)

        elif opcao == '5':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
