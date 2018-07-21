
class Employee:
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount = Employee.empCount + 1

    def disp_Name(self):
        print self.name
    def disp_salary(self):
        print self.salary
    def disp_count(self):
        print Employee.empCount

emp1 = Employee("lata",25000)
emp2 = Employee("surbhi",30000)
emp1.disp_Name()
emp1.disp_salary()
emp1.disp_count()
