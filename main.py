import os


def clear():
    try:
        os.system('clear')
    except Exception:
        os.system('cls')


class Main:

    num1 = int
    num2 = int
    rslt = int

    u_fist_name = str
    u_last_name = str
    u_salarary = float

    def set_num1(self, num1):
        self.num1 = num1

    def set_num2(self, num2):
        self.num2 = num2

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
                self.set_num1(int(num1))
                self.set_num2(int(num2))
                op = int(op)
                print(f'\nEl resultado es: {self.operations(op)}')
            except Exception as e:
                print(f"FATAL ERROR: {e}")
                continue


def main():
    current = Main()
    current.calc_menu()


if __name__ == '__main__':
    main()
