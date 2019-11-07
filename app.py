from classes.solider import Solider
from classes.vehicle import Vehicle

if __name__ == '__main__':
    s1 = Solider(100, 200, 1)
    s2 = Solider(100, 200, 2)
    s3 = Solider(0, 200, 3)
    s4 = Solider(0, 200, 4)
    v = Vehicle(100, 1000, [s1, s2])
    print(len(v.operators))
    print(len(v.active_operators))
