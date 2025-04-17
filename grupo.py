class SistemaDeGrupos:
    def __init__(self):
        self.vertices = set()  # pessoas
        self.arestas = {}  
        self.grupos = {} 

    def criar_pessoa(self, nome):
        if nome in self.vertices:
            print(f"Pessoa '{nome}' já existe.")
        else:
            self.vertices.add(nome)
            self.arestas[nome] = {}
            print(f"Pessoa '{nome}' criada com sucesso.")

    def criar_grupo(self, grupo_id, membros=None):
        if grupo_id in self.grupos:
            print(f"Grupo '{grupo_id}' já existe.")
            return

        self.grupos[grupo_id] = set()

        if membros:
            membros_validos = [m for m in membros if m in self.vertices]
            
            # ✅ Adiciona todos os membros ao grupo
            self.grupos[grupo_id].update(membros_validos)
            
            # ✅ Conecta os pares de membros
            for i in range(len(membros_validos)):
                for j in range(i+1, len(membros_validos)):
                    self.adicionar_conexao(membros_validos[i], membros_validos[j], grupo_id)

        print(f"Grupo '{grupo_id}' criado com sucesso.")

    def adicionar_conexao(self, pessoa1, pessoa2, grupo_id):
        self.arestas[pessoa1][pessoa2] = grupo_id
        self.arestas[pessoa2][pessoa1] = grupo_id

    def adicionar_pessoa_ao_grupo(self, nome, grupo_id):
        if nome not in self.vertices:
            print(f"Pessoa '{nome}' não existe.")
            return
        if grupo_id not in self.grupos:
            print(f"Grupo '{grupo_id}' não existe.")
            return

        for membro in self.grupos[grupo_id]:
            self.adicionar_conexao(nome, membro, grupo_id)
        self.grupos[grupo_id].add(nome)
        print(f"Pessoa '{nome}' adicionada ao grupo '{grupo_id}'.")

    def listar_grupos(self):
        if not self.grupos:
            print("Nenhum grupo criado ainda.")
            return
        for grupo_id, membros in self.grupos.items():
            print(f"Grupo '{grupo_id}': {sorted(membros) if membros else 'Sem membros'}")

    def mostrar_conexoes(self):
        print("\nConexões no grafo:")
        for pessoa in self.arestas:
            if self.arestas[pessoa]:
                print(f"{pessoa} está conectado a: {self.arestas[pessoa]}")

def menu():
    print("\n=== Sistema de Grupos ===")
    print("1. Criar pessoa")
    print("2. Criar grupo")
    print("3. Adicionar pessoa ao grupo")
    print("4. Listar grupos")
    print("5. Mostrar conexões")
    print("6. Sair")
    return input("Escolha uma opção: ")

if __name__ == "__main__":
    sistema = SistemaDeGrupos()
    
    while True:
        opcao = menu()
        
        if opcao == "1":
            nome = input("Digite o nome da pessoa: ")
            sistema.criar_pessoa(nome)
        
        elif opcao == "2":
            grupo_id = input("Digite o nome do grupo: ")
            membros = input("Digite os nomes dos membros separados por vírgula (ou pressione Enter para grupo vazio): ")
            if membros.strip():
                membros = [m.strip() for m in membros.split(",")]
                sistema.criar_grupo(grupo_id, membros)
            else:
                sistema.criar_grupo(grupo_id)
        
        elif opcao == "3":
            nome = input("Digite o nome da pessoa: ")
            grupo_id = input("Digite o nome do grupo: ")
            sistema.adicionar_pessoa_ao_grupo(nome, grupo_id)
        
        elif opcao == "4":
            sistema.listar_grupos()
        
        elif opcao == "5":
            sistema.mostrar_conexoes()
        
        elif opcao == "6":
            print("Encerrando o programa...")
            break
        
        else:
            print("Opção inválida!")
