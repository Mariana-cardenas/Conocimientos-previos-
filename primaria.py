class Persona:
    def __init__(self, nombre):
        self.nombre = nombre


class Estudiante(Persona):
    def __init__(self, nombre, notas):
        super().__init__(nombre)
        self.notas = notas

    def contador(self):
        cantidad = 0

        for nota in self.notas:
            if nota >= 2.5 and nota < 3.5:
                cantidad += 1

        return cantidad


estudiantes = [
    Estudiante("arnando", [1.1, 1.8, 3.3]),
    Estudiante("nicolas", [4.3, 1.6, 4.3]),
    Estudiante("daniel", [3.8, 0.7, 1.8]),
    Estudiante("maria", [0.6, 2.5, 4.0]),
    Estudiante("marcela", [0.5, 3.8, 1.2]),
    Estudiante("alexandra", [2.6, 4.6, 0.1])
]

notas = []

for estudiante in estudiantes:
    notas += estudiante.notas

promedio = sum(notas) / len(notas)

mayor = 0

for nota in notas:
    if nota > promedio:
        mayor += 1

regulares = 0

for estudiante in estudiantes:
    regulares += estudiante.contador()

reprobados = [0, 0, 0]

for estudiante in estudiantes:
    for i in range(3):
        if estudiante.notas[i] < 3:
            reprobados[i] += 1

materias = ["quimica", "idiomas", "historia"]

materia = materias[reprobados.index(max(reprobados))]

mejor = estudiantes[0]

for estudiante in estudiantes:
    if estudiante.notas[0] > mejor.notas[0]:
        mejor = estudiante

print(mayor)
print(regulares)
print(materia)
print(mejor.nombre)