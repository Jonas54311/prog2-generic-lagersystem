from typing import TypeVar, Generic
T = TypeVar("T")

class Lager(Generic[T]):
    def __init__(self, instans):
        self.mängd = 0 #lokal klassvariabel
        self.instans = instans #lokal instansvariabel

    def yttre(self, val):
        value = val #enclosing
        def innre():
            print(value)
        innre()

obj = Lager(123)
obj.yttre(5)

#En lokal variabel i en funktion dör efter att funktionen är klar, än om funktionen används fler gånger, en klassvariabel dör då klassen dör.
#För att variabeln i den andra metoden är lokal