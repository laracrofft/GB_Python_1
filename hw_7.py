# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», реализуйте перегрузку
# методов сложения и умножения комплексных чисел. Проверьте работу проекта, создав экземпляры класса (комплексные
# числа) и выполнив сложение и умножение созданных экземпляров. Проверьте корректность полученного результата.


class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = f'{self.a} + {self.b}j'

    def __add__(self, other):
        print(f'Сумма n1 и n2:')
        return f'c = {self.a + other.a} + {self.b + other.b}j'

    def __mul__(self, other):
        print(f'Произведение n1 и n2:')
        return f'c = {self.a * other.a - (self.b * other.b)} + {self.b * other.a + (self.a * other.b)}j'

    def __str__(self):
        return f'c = {self.a} + {self.b}j'


n1 = ComplexNumber(1, 1)
n2 = ComplexNumber(1, 4)
print(n1)
print(n2)
print(n1 + n2)
print(n1 * n2)
