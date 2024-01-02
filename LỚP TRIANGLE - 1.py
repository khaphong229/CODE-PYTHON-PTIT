from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Triangle:
    def __init__(self, p1, p2, p3):
        self.points = [p1, p2, p3]

    def distance(self, p1, p2):
        return sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)

    def is_valid_triangle(self):
        a = self.distance(self.points[0], self.points[1])
        b = self.distance(self.points[1], self.points[2])
        c = self.distance(self.points[2], self.points[0])

        return a + b > c and b + c > a and c + a > b

    def perimeter(self):
        return round(self.distance(self.points[0], self.points[1]) +
                     self.distance(self.points[1], self.points[2]) +
                     self.distance(self.points[2], self.points[0]), 3)


if __name__ == "__main__":
    t = int(input())

    for _ in range(t):
        coordinates = list(map(float, input().split()))

        p1 = Point(coordinates[0], coordinates[1])
        p2 = Point(coordinates[2], coordinates[3])
        p3 = Point(coordinates[4], coordinates[5])

        triangle = Triangle(p1, p2, p3)

        if triangle.is_valid_triangle():
            print(triangle.perimeter())
        else:
            print("INVALID")
