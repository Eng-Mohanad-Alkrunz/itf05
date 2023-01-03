from abc import abstractmethod


class SecurityGuard:

    @abstractmethod
    def behave(self):
        pass


class GeneralManager(SecurityGuard):
    def behave(self):
        print("Welcome , you can pass")


class Employee(SecurityGuard):

    def behave(self):
        m_id = input("Please Enter Your ID")
        print("Welcome , you can pass")


general_manager = GeneralManager()
employee = Employee()
my_list = [general_manager,employee]
for i in my_list:
    if isinstance(i,GeneralManager):
        print("Welcome Sir,",end=" ")
    i.behave()
