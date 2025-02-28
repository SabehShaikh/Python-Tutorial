class Calculator:

    def __init__(self, n):
        self.n = n 

    def square(self):
        print(f"square of {self.n} is {self.n * self.n}")

    def cube(self):
        print(f"cube of {self.n} is {self.n * self.n * self.n}")
      

    def squareroot(self):
        print(f"square root of {self.n} is {self.n ** 0.5}")
        

a = Calculator(5)   
a.square()
a.cube()
a.squareroot()
