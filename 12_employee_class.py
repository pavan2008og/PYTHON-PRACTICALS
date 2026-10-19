class Employee:
    count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1

    def display(self):
        print("Name:", self.name, "| Salary:", self.salary)


e1 = Employee("Amit", 50000)
e2 = Employee("Riya", 60000)
e3 = Employee("Karan", 55000)

for e in (e1, e2, e3):
    e.display()

print("Total employees:", Employee.count)
