import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def length_of_side(self, p, q):
        temp = (p.x - q.x)**2 + (p.y - q.y)**2
        return math.sqrt(temp)    

class Triangle(Point):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.length_of_side(self.a, self.b) + self.length_of_side(self.b, self.c) + self.length_of_side(self.a, self.c)

    def print_class(self):
        print(u'Треугольник построен на точках:')
        print(u'A: (', self.a.x, u';', self.a.y, u')')
        print(u'B: (', self.b.x, u';', self.b.y, u')')
        print(u'C: (', self.c.x, u';', self.c.y, u')')
        print(u'Длины сторон:')
        print(u'AB =', self.length_of_side(self.a, self.b))
        print(u'BC =', self.length_of_side(self.b, self.c))
        print(u'AC =', self.length_of_side(self.a, self.c))


    def square(self):
        half = self.perimeter() / 2
        return math.sqrt(half * (half - self.length_of_side(self.a, self.b)) * (half - self.length_of_side(self.b, self.c)) * (half - self.length_of_side(self.a, self.c)))
    
    def compare(t1, t2):
        sq1 = t1.square()
        sq2 = t2.square()
        dif = sq1 - sq2
        if (dif > 0):
            print(u'Первая фигура больше на', dif)
        elif (dif == 0):
            print(u'Фигуры равны по площади')
        else:
            print(u'Вторая фигура больше на', abs(dif))

    def move(self, x, y):
        for p in (self.a, self.b, self.c):
            p.x += x
            p.y += y
        self.print_class()

class Quad(Triangle):
    def __init__(self, a, b, c, d):
        super().__init__(a, b, c)
        self.d = d

    def print_class(self):
        print(u'Квадрат построен на точках:')
        print(u'A: (', self.a.x, u';', self.a.y, u')')
        print(u'B: (', self.b.x, u';', self.b.y, u')')
        print(u'C: (', self.c.x, u';', self.c.y, u')')
        print(u'D: (', self.d.x, u';', self.d.y, u')')
        print(u'Длина стороны:', self.length_of_side(self.a, self.b))

    def square(self):
        return (self.length_of_side(self.a, self.b))**2

    def move(self, x, y):
        super().move(x, y)

print(u'Построим две фигуры')
figures = []
for j in range(0, 2):
    print(u'Какую фигуру хотите создать? 1 - треугольник, 2 - квадрат')
    k = input()
    points = []
    if int(k) == 1:
        n = 3
        for i in range(0, n):
            print(u'Введите', i + 1, u'точку (две координаты во float-формате, через Enter):')
            x = float(input())
            y = float(input())
            points.append(Point(x, y))
        figures.append(Triangle(points[0], points[1], points[2]))
    elif int(k) == 2:
        n = 4
        for i in range(0, n):
            print(u'Введите', i + 1, u'точку (две координаты во float-формате, через Enter):')
            x = float(input())
            y = float(input())
            points.append(Point(x, y))
        figures.append(Quad(points[0], points[1], points[2], points[3]))
    else:
        print(u'wtf')
    figures[j].print_class()
    print(u'Хотите передвинуть фигуру? Введите две float-координаты (0, если не хотите смещать):')
    x = float(input())
    y = float(input())
    figures[j].move(x, y)
print(u'Сравним фигуры по площади')
figures[0].compare(figures[1])
