zmienna = 1
zmienna2 = "Abc"

lista = [1, 2, "A", "F", "H", ]

print(lista)
print(lista[0])
print(lista[4])

lista[2] = 3
print(lista[2])
print(lista)

tekst = "Hello World"
print(tekst[4])

print(lista + ["G", "K"])
print(lista * 3)

lista2 = (lista + ["G", "K"])
print(lista2 * 3)

print("Ilość elementów: ", len(lista))
print("Ilość elementów: ", len(lista2))

lista.append("L")
print(lista)

lista.append(lista2)
print(lista)

print(lista[6][3])

lista.insert(3, 3)
print(lista)

print("Ilość: ", lista.count(3))

print("Ilość: ", lista.count("H"))
print("Ilość: ", (lista + lista2).count("H"))

print("index: ", lista.index("F"))
print("index: ", lista.index(3))

lista.remove("F")
print(lista)

lista.remove(lista2)
print(lista)


lista3 = [1, 20, 35, -5, 0, ]

print("Min: ", min(lista3))
print("Max: ", max(lista3))

lista3.sort()
print(lista3)

lista3.reverse()
print(lista3)

lista3.clear()
print(lista3)