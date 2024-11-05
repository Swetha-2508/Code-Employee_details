class Employee:
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_salary = emp_salary
        self.emp_department = emp_department

    def display_employee(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Employee Name: {self.emp_name}")
        print(f"Employee Salary: {self.emp_salary}")
        print(f"Employee Department: {self.emp_department}")

    def add_employee(emp_list):
        emp_id = int(input("Enter employee ID: "))
        emp_name = input("Enter employee name: ")
        emp_salary = float(input("Enter employee salary: "))
        emp_department = input("Enter employee department: ")

        new_employee = Employee(emp_id, emp_name, emp_salary, emp_department)
        emp_list.append(new_employee)
        print("Employee added successfully!") 
    def calculate_salary(self, hours_worked):
        if hours_worked > 40:
            overtime = hours_worked - 40
            ot_amount = (overtime * (self.emp_salary / 40))
            month_salary = self.emp_salary + ot_amount
        else:
            month_salary = self.emp_salary
        return month_salary
employee = Employee(1, 'John Doe', 50000, 'Engineering')
hours_worked = 45
month_salary = employee.calculate_salary(hours_worked)
print(f"Monthly Salary: {month_salary}")

employees = []
Employee.add_employee(employees)    
