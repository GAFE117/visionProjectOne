def case1():
    return "Esta es la opción 1"

def case2():
    return "Esta es la opción 2"

def case3():
    return "Esta es la opción 3"

def default_case():
    return "Opción no válida"

switch_case = {
    1: case1,
    2: case2,
    3: case3
}

choice = 2

result = switch_case.get(choice, default_case)()
print(result)

