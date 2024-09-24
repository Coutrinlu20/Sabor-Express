class Restaurante :

    restaurantes = []
    def __init__(self, nome,categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False
        Restaurante.restaurantes.append(self)


    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    def lista_restaurantes():
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante.nome} | {restaurante.categoria} | {restaurante.ativo}')


restaurante_praca = Restaurante('Praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurantes = [restaurante_praca, restaurante_pizza]

# parou na aula3 video 1
# dir(): Retorna uma lista das propriedades e métodos dos objetos especificados
# vars(): Retorna a propriedade __dict__ de um objeto
# print(restaurante_praca)
# print(restaurante_pizza)

Restaurante.lista_restaurantes()