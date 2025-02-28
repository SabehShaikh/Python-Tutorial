class Employee:
    language = "Python" # class attribute
    salary = 1000 # class attribute

    def __init__(self, name, language, salary):
        print("This is constructor, IT WILL RUN AUTOMATICALLY")
        self.name = name
        self.language = language
        self.salary = salary


    def getInfo(self):
        print(f"The language is {self.language} and the salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good morning!")    

sabeh = Employee("Sabeh", "JavaScript" , 2500)
print(f"The name of employee is {sabeh.name} and the salary is {sabeh.salary}")


