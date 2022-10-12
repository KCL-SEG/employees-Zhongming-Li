"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, salary, commission):
        self.name = name
        self.salary = salary
        self.commission = commission

    def get_pay(self):
        return get_salary(self.salary)+get_commission_amount(self.commission)

    def __str__(self):
        return (f'{self.name} works on {get_salary_str(self.salary)} {get_commission_str(self.commission)}. Their total pay is {get_pay(self)}')


class SalaryInterface:
    def __init__(self):
        pass

    def get_salary(self):
        pass

    def get_salary_str(self):
        pass


class MonthlySalary(SalaryInterface):
    def __init__(self, salary_amount):
        self.salary_amount = salary_amount

    def get_salary(self):
        return salary_amount

    def get_salary_str(self):
        return (f'a monthly salary of {self.salary_amount}')


class HourlySalary(SalaryInterface):
    def __init__(self, salary_amount, hours):
        self.salary_amount = salary_amount
        self.hours = hours

    def get_salary(self):
        return self.salary_amount * self.hours

    def get_salary_str(self):
        return (f'a contract of {self.hours} hours at {self.salary_amount}/hour')



class CommissionInterface:
    def __init__(self):
        pass

    def get_commission_amount(self):
        pass

    def get_commission_str(self):
        pass


class BonusCommission(CommissionInterface):
    def __init__(self, commission_amount):
        self.commission_amount = commission_amount

    def get_commission_amount(self):
        return self.commission_amount

    def get_commission_str(self):
        return (f' and receives a bonus commission of {self.commission_amount}')


class ContractCommission(CommissionInterface):
    def __init__(self, contract_num, commission_amount):
        self.contract_num = contract_num
        self.commission_amount = commission_amount

    def get_commission_amount(self):
        return self.commission_amount*self.contract_num

    def get_commission_str(self):
        return (f' and receives a commission for {self.contract_num} contract(s) at {self.commission_amount}/contract')


class NoCommission(CommissionInterface):
    def __init__(self):
        pass

    def get_commission_amount(self):
        pass

    def get_commission_str(self):
        pass




# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', (25, 100), None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', (3000, None), (4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', (25, 150), (3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', (30, 120), 600)
