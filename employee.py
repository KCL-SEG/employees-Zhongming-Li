"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        if (self.contract.get_contract_type() == "salary"):
            if (self.commission.get_commission_type() == "bonus"):
                return (self.contract.get_salary() + self.commission.get_commission_amount())
            else:
                return (self.contract.get_salary() + self.commission.get_commission_amount()*self.commission.get_contract_num())
        else:
            if (self.commission.get_commission_type() == "bonus"):
                return (self.contract.get_salary()*self.get_contract_hours() + self.commission.get_commission_amount())
            else:
                return (self.contract.get_salary()*self.get_contract_hours() + self.commission.get_commission_amount()*self.commission.get_contract_num())

    def __str__(self):
        return (f'{self.name} works on {self.contract.get_contract_str()} {self.commission.get_commission_str()}. Their total pay is')


class Contract:
    def __init__(self, salary, hours, contract_type):
        self.hours = hours
        self.contract_type = contract_type

    def get_salary(self):
        return self.salary

    def get_contract_hours(self):
        return self.hours

    def get_contract_type(self):
        return self.contract_type

    def get_contract_str(self):
        if (self.contract_type=='salary'):
            return (f'a monthly salary of {self.salary}')
        else:
            return (f'a contract of {self.hours} hours at {self.salary}/hour')



class Commission:
    def __init__(self, contract_num, commission_amount, commission_type):
        self.contract_num = contract_num
        self.commission_amount = commission_amount
        self.commission_type = commission_type

    def get_contract_num(self):
        return self.contract_num

    def get_commission_amount(self):
        return self.commission_amount

    def get_commission_type(self):
        return self.commission_type

    def get_commission_str(self):
        if (commission_type==None):
            return ' '
        elif (commission_type=='bonus'):
            return (f' and receives a bonus commission of {self.amount}')
        else:
            return (f' and receives a commission for {self.contract_num} contract(s) at {self.amount}/contract')


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', (4000, None, 'salary'), None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', (25, 100, 'hourly'), None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', (3000, None, 'salary'), (4, 200, 'contract'))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', (25, 150, 'hourly'), (3, 220, 'contract'))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', (2000, None, 'salary'), (None, 1500, 'bonus'))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', (30, 120, 'hourly'), (None, 600, 'bonus'))
