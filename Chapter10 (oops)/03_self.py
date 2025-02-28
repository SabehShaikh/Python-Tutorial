class Employee:
    language = "Python" # class attribute
    salary = 1000 # class attribute

    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning!")    

sabeh = Employee()
sabeh.language = "JavaScript" # object attribute

sabeh.greet()
sabeh.getInfo()
# Employee.getInfo(sabeh)


