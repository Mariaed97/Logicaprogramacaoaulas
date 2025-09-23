# desenhar um personagem
class Personagem:
    # construtor 
    def __init__(self, nome, vida):
        # encapsulalamento = o '__' para deixar privado
        self.__nome = nome 
        self.__vida = vida

# para acessar os atributos já que eles estão privados

        # definindo GET para chamar o nome (ler)
    @property
    def nome(self):
        return self.__nome
        
        # definindo SET para mudar o nome do personagem
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @ property
    def vida(self):
        return self.__vida
        
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def atacar(self, personagem):
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome}.')
        print(f'Agora esta com {personagem.vida}')
            

class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def curar(self, personagem):
        personagem.vida += 15
        print(f'{self.nome} usou poder de cura em {personagem.nome}')
        print(f'A vida de {personagem.nome} agora é de {personagem.vida}')

class Bruxa(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def pocao(self, personagem):
        personagem.vida -= 15
        print(f'{self.nome} lançou poção em {personagem.nome}.')
        print(f'Agora esta com {personagem.vida}')

class Invisivel(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)

    def invisivel(self, personagem):
        personagem.vida -= 20
        print(f'{self.nome} ficou invivível e atacou {personagem.nome}.')
        print(f'Agora esta com {personagem.vida}')

class Peppa(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
    
    def matar(self, personagem):
        print(f'{self.nome} matou os pais de {personagem.nome}.')
        print(f'Agora {personagem.nome} esta sem pais')


dada = Personagem('Dada', 100)
trevo = Mago('Trevo', 100)
arabela = Bruxa('Arabela', 100)
lalabond = Invisivel('Lalabond', 100)
pepa = Peppa('Peppa', 40) 

arabela.pocao(dada)
lalabond.invisivel(arabela)
trevo.curar(dada)
dada.atacar(arabela)
arabela.pocao(lalabond)
arabela.pocao(trevo)
trevo.curar(trevo)
lalabond.invisivel(trevo)
dada.atacar(arabela)
pepa.matar(arabela)
arabela.pocao(pepa)
dada.atacar(pepa)
trevo.curar(pepa)
dada.atacar(trevo)
arabela.pocao(trevo)
lalabond.invisivel(pepa)

print('---conclusão---')
print('Após Peppa matar os pais de Arabela, gerou uma grande guerra, trazendo a morte de Peppa.')