class Triangle:
    def __init__(self, a:int, b:int, c:int):
        self.a, self.b, self.c = a, b, c

        if not self.is_triangle(a, b, c):
            raise Exception(a,b,c, 'it"s not a triangle')

    def culculate_square(self):
        s = (self.a + self.b + self.c) / 2

        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
        # print('The area of the triangle is %0.2f' % area)


    def is_triangle(self, a, b, c):
        return a + b >= c and b + c >= a and a + c >= b

    def __repr__(self):
        return "Triangle, {}, {}, {}".format(self.a, self.b, self.c)


# t = Triangle(1, 5, 3)
t = Triangle(3,4,5)


print(t.culculate_square())
print(t)



