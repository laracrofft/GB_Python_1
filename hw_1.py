# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
# принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
# (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, a):
        self.b = '\n'.join(['\t'.join([str(j) for j in i]) for i in a])
        list_1 = []
        for i in a:
            list_1.append([j for j in i])
        self.a = list_1

    def __str__(self):
        self.c = str(self.b)
        return self.c

    def __add__(self, other):
        num_str = len(self.a)
        num_col = len(other.a[0])
        for i in range(num_str):
            for j in range(num_col):
                self.a[i][j] = self.a[i][j] + other.a[i][j]
            result = self.a
        return Matrix(result)


m_1 = Matrix([[12.5, 8, -1],
              [77, 0, 22],
              [4, 5, 94]])
m_2 = Matrix([[4, 28, -6],
              [6, 0, 3],
              [24, -5, 7]])
print(m_1 + m_2)
