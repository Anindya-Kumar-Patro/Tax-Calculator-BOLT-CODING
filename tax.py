class OldRegime:
    def __init__(self, income):
        self.income = income
        self.tax = 0

    def calculate_less_2_5(self, income):
        self.tax += income * 0
        return self.tax

    def calculate_less_5(self, income):
        self.tax += self.calculate_less_2_5(250000)
        self.tax += (income - 250000) * 0.05
        return self.tax

    def calculate_less_10(self, income):
        self.tax += self.calculate_less_5(500000)
        self.tax += (income - 500000) * 0.20
        return self.tax

    def calculate_greater_10(self, income):
        self.tax += self.calculate_less_10(1000000)
        self.tax += (income - 1000000) * 0.30
        return self.tax 

    def calculate_cess(self):
        return self.calculate_tax() * 1.04    

    def calculate_tax(self):
        if self.income <= 500000:
            return 0
        elif self.income <= 1000000:
            return self.calculate_less_10(self.income)
        else:
            return self.calculate_greater_10(self.income)


class NewRegime:
    def __init__(self, income):
        self.income = income
        self.tax = 0

    def calculate_less_3(self, income):
        self.tax += income * 0
        return self.tax

    def calculate_less_6(self, income):
        self.tax += self.calculate_less_3(300000)
        self.tax += (income - 300000) * 0.05
        return self.tax

    def calculate_less_9(self, income):
        self.tax += self.calculate_less_6(600000)
        self.tax += (income - 600000) * 0.10
        return self.tax

    def calculate_less_12(self, income):
        self.tax += self.calculate_less_9(900000)
        self.tax += (income - 900000) * 0.15
        return self.tax

    def calculate_less_15(self, income):
        self.tax += self.calculate_less_12(1200000)
        self.tax += (income - 1200000) * 0.20
        return self.tax

    def calculate_greater_15(self, income):
        self.tax += self.calculate_less_15(1500000)
        self.tax += (income - 1500000) * 0.30
        return self.tax           

    def calculate_cess(self):
        return self.calculate_tax() * 1.04    

    def calculate_tax(self):
        if self.income <= 700000:
            return 0
        elif self.income <= 900000:
            return self.calculate_less_9(self.income)
        elif self.income <= 1200000:
            return self.calculate_less_12(self.income)        
        elif self.income <= 1500000:
            return self.calculate_less_15(self.income)
        else:
            return self.calculate_greater_15(self.income)

def compare_and_calculate(income, deduction):
    old_tax = 0            
    new_tax = 0            
    taxable_income_old = 0            
    taxable_income_new = 0

    if income <= 500000:
        old_tax = 0
    else:
        taxable_income_old = income - deduction - 50000

    # Old Regime
    OR = OldRegime(taxable_income_old)
    if taxable_income_old <= 500000:
        old_tax = 0
    else:
        old_tax = OR.calculate_cess()  

    # New Regime
    NR = NewRegime(income - 50000)
    if income <= 750000:
        new_tax = 0
    else:
        new_tax = NR.calculate_cess()

    return old_tax, new_tax

if __name__ == "__main__":
    income = int(input(" Enter your Income : "))            
    deduction = int(input(" Enter your deduction : "))     

    old_tax, new_tax = compare_and_calculate(income, deduction)

    print(f"Old Tax = {old_tax}")
    print(f"New Tax = {new_tax}")
    if new_tax < old_tax:
        print(f"Choose New tax")
        print(f"Benefit : {old_tax - new_tax}")  
    else:
        print(f"Choose Old tax")
        print(f"Benefit : {new_tax - old_tax}")           




