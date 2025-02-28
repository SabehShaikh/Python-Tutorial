# create programmer class and store info about programemrs working at microsoft:

class Programmer:
    company = "Microsoft" # class attribute, cuz all are working in microsoft

    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = Programmer("Sabeh" , "5500" , "1234")
print(f"name: {p.name} \nsalary: {p.salary} \npin: {p.pin} \ncompany: {p.company}")

p1 = Programmer("Harry" , "5000" , "786")
print(f"name: {p1.name} \nsalary: {p1.salary} \npin: {p1.pin} \ncompany: {p1.company}")