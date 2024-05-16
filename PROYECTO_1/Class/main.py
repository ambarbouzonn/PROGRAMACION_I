from class_personaje import Personaje

personaje_1 = Personaje("IroMan", True, True, "Inteligencia", 500)
personaje_2 = Personaje("Thor", False, True, "Trueno", 700)
personaje_3 = Personaje("Spider Man", True, False, "Aracnido", 300)
personaje_4 = Personaje("Groot", False, False, "Iam Groot", 500)

Personaje.describerse(personaje_1)
Personaje.describerse(personaje_2)


descripcion = print(personaje_1.describerse())

descripcion = print(personaje_2.describerse())
print(descripcion)

personaje_1.volar(1000, 200)
personaje_2.volar(100, 50)

personaje_3.puede_volar = True

personaje_3.volar(100, 50)

personaje_1.atacar(personaje_3)
personaje_4.atacar(personaje_1)