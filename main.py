import os


def clear():
    try:
        os.system('clear')
    except Exception:
        os.system('cls')


class Main:

    users = {}

    def set_nums(self, num1, num2):
        self.num1, self.num2 = num1, num2

    def operations(self, op):
        if op == 1:
            return self.num1 + self.num2

        if op == 2:
            return self.num1 - self.num2

        if op == 3:
            return self.num1 * self.num2

        if op == 4:
            return self.num1 / self.num2

    def calc_menu(self):
        while True:
            input('Presione enter para continuar')
            clear()
            print('\t\t CALCULATHOR')
            num1 = input('Ingrese el primer numero:\n')
            num2 = input('Ingrese el segundo numero:\n')
            op = input('Seleccione una operacion:\n1) +\n2) -\n3) *\n4) /\n')
            try:
                self.set_nums(float(num1), float(num2))
                op = int(op)
                print(f'\nEl resultado es: {self.operations(op)}')
            except Exception as e:
                print(f"FATAL ERROR: {e}")
                continue

    def add_user(self):
        clear()
        name = input('Ingrese el nombre del nuevo usuario:\n')
        self.users[name] = None
        print('Usuario agregado')
        sel = input('Dar de alta su salario:\n1) Si\n2)No\n')
        try:
            sel = int(sel)
            if sel == 1:
                self.set_user_salary(name)
            else:
                return None
        except Exception as e:
            print(f"FATAL ERROR: {e}")
            input('Presione enter para continuar')

    def set_user_salary(self, name=None):
        clear()
        if name is None:
            print(list(self.users.keys()))
            name = input('Ingrese el nombre del usuario:\n')
        if name not in self.users:
            print('ERROR: Usuario no encontrado')
            input('Presione enter para continuar')
            return None
        print(f'El salario actual de {name} es {self.users[name]}')
        salary = input(f'Ingrese el salario de {name} en pesos:\n')
        self.users[name] = salary
        print('Salario registrado')
        input('Presione enter para continuar')

    def get_user_salary(self):
        clear()
        print(list(self.users.keys()))
        name = input('Por favor ingrese el nombre del usuario:\n')
        if name not in self.users:
            print('Usuario no encontrado')
            input('Presione enter para continuar')
            return None
        print(self.users[name])
        input('Presione enter para continuar')

    def action(self, selection):
        if selection == 1:
            self.add_user()
        elif selection == 2:
            self.get_user_salary()
        elif selection == 3:
            self.set_user_salary()
        else:
            print("Opcion no disponible")

    def users_menu(self):
        while True:
            clear()
            print('\tREGISTRATHOR')
            print('Que desea hacer:')
            print('1) Agregar un nuevo usuario')
            print('2) Consultar el salario de un usuario')
            print('3) Modificar el salario de un usuario')
            print('4) Salir')
            selection = input()
            try:
                selection = int(selection)
                if selection == 4:
                    return None
                self.action(selection)
            except Exception as e:
                print(f'FATAL ERROR 01: {e}')


def main():
    current = Main()
    current.users_menu()


if __name__ == '__main__':
    main()
