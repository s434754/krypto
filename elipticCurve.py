from utils import binpow, euler_test, rnwd
from random import randint


class ElipticCurve:
    def __init__(self, l=128, A=None, B=None, p=None):
        self.p = p
        self.A = A
        self.B = B
        self.points = []

        if (A is None or B is None):
            while (True):
                self.A = randint(2, self.p)
                self.B = randint(2, self.p)
                d = (4 * binpow(self.A, 3, self.p)) % self.p + \
                    (27 * binpow(self.B, 2, self.p)) % self.p
                if d != 0:
                    break

    def printCurve(self):
        print("E : Y^2 = X^3 + {}X + {}, nad F{}".format(str(self.A),
              str(self.B), str(self.p)))
        print(f'A:{self.A} B:{self.B}\n')

    def printPoints(self):
        for point in self.points:
            print("x: {}, y: {} \n".format(str(point[0]), str(point[1])))

    def generatePoints(self, n=1):
        ''' n - number of points to generate '''
        for _ in range(n):
            while (True):
                x = randint(2, self.p)
                xd = x**3 + self.A * x + self.B
                if euler_test(xd, self.p):
                    y = binpow(xd, (self.p+1)//4, self.p)
                    if (n == 1):
                        self.points.append([x, y])
                        return [x, y]
                    self.points.append([x, y])
                    break

    def checkPoint(self, P):
        x = P[0]
        y = P[1]
        if (y**2) % self.p == (x**3 + self.A * x + self.B) % self.p:
            print("Punkt x: {}, y: {} należy do krzywej. \n".format(str(x), str(y)))
            return True
        else:
            print("Punkt x: {}, y: {} nie należy do krzywej. \n".format(str(x), str(y)))
            return False

    def opositePoint(self, P):
        x = P[0]
        y = P[1]
        print("Punkt przeciwny to x: {}, y: {} \n".format(str(x), str(self.p - y)))
        return [x, self.p - y]

    def sumPoints(self, P1, P2):
        x1 = P1[0]
        y1 = P1[1]
        x2 = P2[0]
        y2 = P2[1]

        # P + O = P
        if x2 == float('inf') and y2 == float('inf'):
            print("Suma P + O = P = ({}, {}) \n".format(str(x1), str(y1)))
            return [x1, y1]
        # O + P = P
        elif x1 == float('inf') and y1 == float('inf'):
            print("Suma O + P = P = ({}, {}) \n".format(str(x2), str(y2)))
            return [x2, y2]
        # P + Q = R
        elif x1 != x2:
            u = rnwd(x1 - x2, self.p)
            lamb = ((y1 - y2) % self.p) * u
            x3 = (lamb ** 2 - x1 - x2) % self.p
            y3 = ((lamb * (x1 - x3) % self.p) - y1) % self.p
            print(
                "Suma dwóch różnych punktów P + Q = R = ({}, {}) \n".format(str(x3), str(y3)))
            return [x3, y3]
        # P + P = 2P = Q
        elif x1 == x2 and y1 == y2:
            u = rnwd(2*y1, self.p)
            lamb = (3 * x1 ** 2 + self.A) * u
            x3 = (lamb ** 2 - 2*x1) % self.p
            y3 = ((lamb * (x1 - x3) % self.p) - y1) % self.p
            print("Suma dwóch tych samych punktów to 2P = Q = ({}, {}) \n".format(
                str(x3), str(y3)))
            return [x3, y3]
        # P + Q = O gdy Q = -P
        elif x1 == x2 and y1 == self.p-y2:
            print("Suma dwóch przeciwnych punktów to P + Q = O \n")
            return [float('inf'), float('inf')]
        else:
            print("Blad")
            return [None, None]


# Zadanie        1
curve = ElipticCurve(p=68719476731, l=300)
curve.printCurve()
# Zadanie 2
p = 68719476731
A = 49710749469
B = 5286130045
c = ElipticCurve(p=p, A=A, B=B)
Punkt = c.generatePoints(n=1)
c.printPoints()
c.checkPoint(Punkt)
# Zadanie 3
p = 7
A = 2
B = 4
x = 3
y = 4
c = ElipticCurve(p=p, A=A, B=B)
Punkt = [x, y]
Punkt2 = c.opositePoint(Punkt)
# Zadanie 4
# O = [float('inf'),   float('inf')]
p = 68719476731
A = 2645887931
B = 63508942644
x1 = 56174319723
y1 = 50334202836
x2 = 15593395299
y2 = 42666859491

Punkt1 = [x1, y1]
Punkt2 = [x2, y2]
c = ElipticCurve(p=p, A=A, B=B)
c.sumPoints(Punkt1, Punkt2)
