# example hello.py

class Complex:
     def __init__(self, realpart, imagpart):
         self.r = realpart
         self.i = imagpart

if __name__ == "__main__":
    print __name__
    demo = Complex(10,11)
    print demo.r
