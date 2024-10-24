class Restaurante :

    restaurantes = []
    def __init__(self, nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self._ativo = False
        Restaurante.restaurantes.append(self)


    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def lista_restaurantes():
        print(f'{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Status'.ljust(25)}')
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {restaurante.ativo}')
    
    @property
    def ativo(self):
        return '☑' if self._ativo else '☒'


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

# parou na aula3 video 1
# dir(): Retorna uma lista das propriedades e métodos dos objetos especificados
# vars(): Retorna a propriedade __dict__ de um objeto
# print(restaurante_praca)
# print(restaurante_pizza)

Restaurante.lista_restaurantes()