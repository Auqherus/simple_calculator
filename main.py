class Calculator:
    
    def __init__(self):
        self.__result = 0

    def add(self, a):
        self.__result += a

    def subtract(self, a):
        self.__result -= a

    def multiply(self, a):
        self.__result *= a

    def divide(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        else:
            self.__result /= a

    def modulo(self, a):
        if a == 0:
            raise ValueError("Cannot divide by zero")
        else:
            self.__result %= a

    def power(self, a):
        self.__result **= a

    def square_root(self):
        self.__result **= 0.5

    def clear(self):
        self.__result = 0

    def get_result(self):
        return self.__result
    
def main():

    calc = Calculator()

    calc.add(3)
    calc.power(2)
    calc.multiply(4)
    calc.divide(2)
    calc.modulo(4)
    calc.subtract(232)
    calc.square_root()
    calc.multiply(16)
    calc.clear()
    calc.add(16)
    calc.power(4)
    print(calc.get_result()) # 65536

main()

