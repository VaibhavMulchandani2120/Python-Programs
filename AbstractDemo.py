from abc import ABC,abstractmethod


class RBI(ABC):

    @abstractmethod
    def roi(self):
        pass

class SBI(RBI):
    def show(self):
        print("This is SBI")
    def roi(self):
        print("Rate of Interest Given By SBI is : ",6.5)


class ICICI(RBI):
    def show(self):
        print("This is ICICI")
    def roi(self):
        print("Rate of Interest Given By ICICI is : ",7.0)


s1=SBI()
s1.show()
s1.roi()

i1=ICICI()
i1.show()
i1.roi()
