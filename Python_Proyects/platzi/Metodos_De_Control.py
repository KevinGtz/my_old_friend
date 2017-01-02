"""
# Estructura IF
nombre = 'Kevin'
if nombre == 'saul':
    print('Hola saul')

else:
    print('hola kevin')

#Estructura while

contador = 0
while contador <= 5:
    print('numero %i' % contador)
    contador = contador + 1

#Estructura For

for i in range(10):
    print('Numero %i' %i)

for i in 'Hola Mundo':
    print('%s' %i)  """


class Estudiante(object):
    def __init__(self,nombre,edad):
        self.nombre= nombre
        self.edad=edad

    def hola(self):
        if self.edad > 18:
            return '%s es mayor' %self.nombre
        else:
            return'%s es menor' %self.nombre


