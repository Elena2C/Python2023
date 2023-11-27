class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def calculate_salary(self):
        pass


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def calculate_salary(self):
        return self.salary

    def manage_team(self):
        print(f"{self.name} is managing the {self.department} department.")


class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def calculate_salary(self):
        return self.salary

    def write_code(self):
        print(f"{self.name} is writing code in {self.programming_language}.")


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_quota):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_quota = sales_quota

    def calculate_salary(self):
        return self.salary + (0.1 * (self.sales_quota - 10000))

    def make_sale(self, sale_amount):
        print(f"{self.name} made a sale of ${sale_amount}.")


# Example usage:
manager = Manager("Ana", 1, 50000, "Human Resources")
engineer = Engineer("Bob", 2, 35000, "C++")
salesperson = Salesperson("Mary", 3, 40000, 1000)

print(f"{manager.name} has a salary of ${manager.calculate_salary()}.")
manager.manage_team()

print(f"{engineer.name} has a salary of ${engineer.calculate_salary()}.")
engineer.write_code()

print(f"{salesperson.name} has a salary of ${salesperson.calculate_salary()}.")
salesperson.make_sale(12000)
