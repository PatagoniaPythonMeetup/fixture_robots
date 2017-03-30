from collections import namedtuple

Robot = namedtuple("Robot", "nombre escuela encargado")

def main():
    r1 = Robot("Ultron", "Los Avengers", "Nick Fury")
    r2 = Robot("Wall-e", "Pixar", "Sr. Disney")
    r3 = Robot("Ultron", "Los Avengers", "Nick Fury")
    print("r1 is r2", r1 is r2, end=", ")
    print("r1 == r2", r1 == r2)
    print("r1 is r1", r1 is r1, end=", ")
    print("r1 == r1", r1 == r1)
    print("r1 is r3", r1 is r3, end=", ")
    print("r1 == r3", r1 == r3)

if __name__ == '__main__':
    main()