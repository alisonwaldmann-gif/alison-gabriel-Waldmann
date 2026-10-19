# atividade1 - cachorro
#1. Cachorro
class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade

    def latir(self):
        print(f"{self.nome} diz: Au au!")

    def mostrar_info(self):
        print(f"Nome: {self.nome} | Raça: {self.raca} | Idade: {self.idade} anos")


# 1. Criando dois cachorros diferentes
cachorro1 = Cachorro("Rex", "Pastor Alemão", 3)
cachorro2 = Cachorro("Mel", "Poodle", 5)

# 2. Chamando os métodos para o primeiro cachorro
cachorro1.latir()
cachorro1.mostrar_info()

# 3. Chamando os métodos para o segundo cachorro
cachorro2.latir()
cachorro2.mostrar_info()

# 4. Alterando a idade do primeiro cachorro diretamente pelo atributo
cachorro1.idade = 4

# 5. Chamando mostrar_info() novamente para conferir a alteração
print("Após atualizar a idade do Rex:")
cachorro1.mostrar_info()

# atividade2 - livro
#2. Livro
class Livro:
    def __init__(self, titulo, autor, total_paginas):
        self.titulo = titulo
        self.autor = autor
        self.total_paginas = total_paginas
        self.paginas_lidas = 0

    def ler(self, paginas):
        self.paginas_lidas += paginas
        # Garante que as páginas lidas não ultrapassem o total do livro
        if self.paginas_lidas > self.total_paginas:
            self.paginas_lidas = self.total_paginas

    def porcentagem_lida(self):
        return (self.paginas_lidas / self.total_paginas) * 100

    def paginas_restantes(self):
        return self.total_paginas - self.paginas_lidas

    def terminou(self):
        return self.paginas_lidas == self.total_paginas


# 1. Criando dois livros com números de páginas diferentes
livro1 = Livro("Dom Casmurro", "Machado de Assis", 256)
livro2 = Livro("O Hobbit", "J.R.R. Tolkien", 320)

# --- Sessões de Leitura: Livro 1 ---
print(f"--- Livro 1: {livro1.titulo} ---")

# Sessão 1
livro1.ler(64)
print(f"Porcentagem lida: {livro1.porcentagem_lida()}%")
print(f"Páginas restantes: {livro1.paginas_restantes()}")
print(f"Terminou o livro?: {livro1.terminou()}")

# Sessão 2 (Lendo o restante das páginas + excedente para testar o limite)
print("\nLendo mais 200 páginas...")
livro1.ler(200)
print(f"Porcentagem lida: {livro1.porcentagem_lida()}%")
print(f"Páginas restantes: {livro1.paginas_restantes()}")
print(f"Terminou o livro?: {livro1.terminou()}")


# --- Sessões de Leitura: Livro 2 ---
print(f"--- Livro 2: {livro2.titulo} ---")

# Sessão 1
livro2.ler(160)
print(f"Porcentagem lida: {livro2.porcentagem_lida()}%")
print(f"Páginas restantes: {livro2.paginas_restantes()}")
print(f"Terminou o livro?: {livro2.terminou()}")

# Sessão 2
print("\nLendo mais 80 páginas...")
livro2.ler(80)
print(f"Porcentagem lida: {livro2.porcentagem_lida()}%")
print(f"Páginas restantes: {livro2.paginas_restantes()}")
print(f"Terminou o livro?: {livro2.terminou()}")



