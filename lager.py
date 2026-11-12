from typing import TypeVar, Generic
T = TypeVar("T")
number = 123 #global

class Lager(Generic[T]):
    def __init__(self, instans: T):
        self.mängd = 0 #lokal klassvariabel
        self.instans = instans #lokal instansvariabel

    def yttre(self, val):
        value = val #enclosing
        def innre():
            other_value = 12 #Lokal
            print(value + other_value)
        innre()

obj = Lager[int](number)
obj.yttre(5)

#En lokal variabel i en funktion dör efter att funktionen är klar, än om funktionen används fler gånger, en klassvariabel dör då klassen dör
#För att variabeln i den andra metoden är lokal