class AnimalEstimacao:
    def _init_(self, nome, raca, idade, responsavel, telefone):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.responsavel = responsavel
        self.telefone = telefone

def cadastrar_animal():
    nome = input("Rex: ")
    raca = input("golden retriever: ")
    idade = input("3 anos: ")
    responsavel = input("Maria: ")
    telefone = input("123-456-7890: ")

    # Criando uma instância do tipo abstrato de dados AnimalEstimacao
    animal_cadastrado = AnimalEstimacao(nome, raca, idade, responsavel, telefone)

    return animal_cadastrado

# Exemplo de uso da função
animal_cadastrado = cadastrar_animal()

# Exibindo os atributos do animal cadastrado
print("Cadastro do Animal:")
print(f"Nome: {animal_cadastrado.nome}")
print(f"Raça: {animal_cadastrado.raca}")
print(f"Idade: {animal_cadastrado.idade}")
print(f"Responsável: {animal_cadastrado.responsavel}")
print(f"Telefone: {animal_cadastrado.telefone}")