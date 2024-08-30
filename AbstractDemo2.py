from abc import ABC,abstractmethod


class TRI(ABC):

    @abstractmethod
    def postpaid(self):
        pass

class Vodafone(TRI):
    def show(self):
        print("This is Vodafone")
    def postpaid(self):
        print("Minimum package of Postpaid in V is : ",99)

class Airtel(TRI):
    def show(self):
        print("This is Airtel")
    def postpaid(self):
        print("Minimum package of Postpaid in Airtel is : ",199)

class Jio(TRI):
    def show(self):
        print("This is Jio")
    def postpaid(self):
        print("Minimum package of Postpaid in Jio is : ",299)


v1=Vodafone()
v1.show()
v1.postpaid()

a1=Airtel()
a1.show()
a1.postpaid()

j1=Jio()
j1.show()
j1.postpaid()
