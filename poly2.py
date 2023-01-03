from abc import abstractmethod

class Loan:

    @abstractmethod
    def calculate_interest(self,total,years):
        pass


class BuildingLoan(Loan):

    def calculate_interest(self,total,years):
        return total * (8.5 / 100) * years


class SocialLoan(Loan):
    def calculate_interest(self, total,years):
        return total * (6.5 / 100) * years


class StartUpLoan(Loan):
    def calculate_interest(self, total, years):
        return total * (9/100) * years


# loan_1 = BuildingLoan()
# loan_2 = SocialLoan()
# loan_3 = StartUpLoan()
# loans = [loan_1,loan_2,loan_3]
# for i in loans:
#     print("Interest for ," , type(i), "  = " ,i.calculate_interest(20000,5))
#

def add(num1=0,num2=0,num3=0):
    return num1+num2+num3


print(add())