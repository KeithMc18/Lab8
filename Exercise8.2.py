import random as rand


class Employee:

    def __init__(self, name_in, wages_in, hours_worked_in):
        self.name = name_in
        self.employee_num = rand.randint(1000, 9999)
        self.wages_per_hour = wages_in
        self.hours_worked_per_week = hours_worked_in

    def calculate_salary(self):
        weekly_wage = self.wages_per_hour * self.hours_worked_per_week
        return weekly_wage

    def print_details(self):
        print('Name:                        ', self.name)
        print('Employee Number:             ', self.employee_num)
        print('Hourly Rate:                 ', self.wages_per_hour)
        print('Weekly Hours worked:         ', self.hours_worked_per_week)
        print('---------------------------------')
        print('Weekly Wage:                 ', self.calculate_salary())


# noob = Employee('New guy', 21, 40)
# noob.print_details()


class Trainee(Employee):

    def __init__(self, name_in, wages_in, hours_worked_in, training_hours_in):
        super().__init__(name_in, wages_in, hours_worked_in)
        self.training_hours = training_hours_in

    def calculate_salary(self):
        training_wage = self.training_hours * 5
        add_training_wage = super().calculate_salary() + training_wage
        return add_training_wage

    def print_details(self):
        super().print_details()
        print('Includes training wage:      ', self.calculate_salary())


jim = Trainee('Jim', 10, 40, 5)
jim.print_details()

