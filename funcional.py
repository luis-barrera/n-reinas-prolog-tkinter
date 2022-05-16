cuad = lambda x: x**2

lista_cuad = list(map(cuad, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(lista_cuad)

# Comprehensión de listas
lista3 = [x*3 for x in range(1, 21) if x % 2 == 0]
print(lista3)

# Divisores
divisores = lambda n: [num for num in range(1, n) if n % num == 0]

##

# Lista de primos hasta n
def check_primo(n):
    for num in range(2, n-1):
        if (n % num == 0):
            return False

    return True


print("Primos")
primos = lambda n: [num for num in range(1, n) if check_primo(num)]

print(primos(100))

