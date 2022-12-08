"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Contract:
    def __init__(self, salary, hours, contract_type):
        self.salary = salary * hours
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
        if (self.commission_type=='no'):
            return ('')
        elif (self.commission_type=='bonus'):
                return (f' and receives a bonus commission of {self.amount}')
        else:
            return (f' and receives a commission for {self.contract_num} contract(s) at {self.amount}/contract')



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
                return (self.contract.get_salary()*self.contract.get_contract_hours() + self.commission.get_commission_amount())
            else:
                return (self.contract.get_salary()*self.contract.get_contract_hours() + self.commission.get_commission_amount()*self.commission.get_contract_num())

    def __str__(self):
        return (f'{self.name} works on {self.contract.get_contract_str()}{self.commission.get_commission_str()}.  Their total pay is {self.get_pay()}.')



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie_contract = Contract(4000, 1, 'salary')
billie_commission = Commission(0, 0, 'no')
billie = Employee('Billie', billie_contract, billie_commission)
print(str(billie))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie_contract = Contract(25, 100, 'hourly')
charlie_commission = Commission(0, 0, 'no')
charlie = Employee('Charlie', charlie_contract, charlie_commission)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee_contract = Contract(3000, 1, 'salary')
renee_commission = Commission(4, 200, 'no')
renee = Employee('Renee', renee_contract, renee_commission)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan_contract = Contract(4000, 1, 'salary')
jan_commission = Commission(3, 220, 'other')
jan = Employee('Jan', jan_contract, jan_commission)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie_contract = Contract(2000, 1, 'salary')
robbie_commission = Commission(1, 1500, 'bonus')
robbie = Employee('Robbie', robbie_contract, robbie_commission)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel_contract = Contract(30, 120, 'hourly')
ariel_commission = Commission(1, 600, 'bonus')
ariel = Employee('Ariel', ariel_contract, ariel_commission)
