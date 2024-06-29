class Filme:

    para_assistir = []
    assistidos = []

    def __init__(self, titulo, genero, duracao):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self.__assistido = False
        self.__avaliacao = 'Não avaliado'
        Filme.para_assistir.append(self)

    def __str__(self):
        return f'Filme: {self.titulo} | Gênero: {self.genero} | Duração: {self.duracao}min' if self.__assistido == False else f'Filme: {self.titulo} | Gênero: {self.genero} | Duração: {self.duracao}min | Avaliação: {self.__avaliacao}'
    
    @property
    def status_assistido(self):
        return self.__assistido
    
    @status_assistido.setter
    def status_assistido(self, novo_status):
        self.__assistido = novo_status

    def assistir_filme(self):
        self.status_assistido = True
        Filme.para_assistir.remove(self)
        Filme.assistidos.append(self)

    @classmethod
    def listar_para_assistir(cls):
        for filme in cls.para_assistir:
            print(filme)

    @classmethod
    def listar_assistidos(cls):
        for filme in cls.assistidos:
            print(filme)

    @property
    def status_avaliacao(self):
        return self.__avaliacao
    
    @status_avaliacao.setter
    def status_avaliacao(self, nota):
        self.__avaliacao = f'{nota}/10'

    def avaliar_filme(self, nota):
        if self.status_assistido == True:
            self.status_avaliacao = nota
        else:
            print('Você não pode avaliar um filme que não assistiu.')



filme1 = Filme('Star Wars', 'Ação', 100)
filme2 = Filme('Pelé', 'Documentário', 180)
filme3 = Filme('Whiplash', 'Drama', 120)


filme2.assistir_filme()
filme2.avaliar_filme(2)
Filme.listar_assistidos()
print()
Filme.listar_para_assistir()