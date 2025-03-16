class Array:

    def __init__(self, *args):
        self.array = args

    def sum(self) -> float:
        summa = 0

        for i in self.array:
            summa += i

        return summa

    def multiply(self) -> float:

        if len(self.array) == 0: return 0

        multiply = 1

        for i in self.array:
            if not isinstance(i,(int,float)): raise TypeError
            multiply *= i

        return multiply

    def average(self) -> float:
        return self.sum() / len(self.array)

lst =[1,2,3,4,5]
ar = Array(lst)
rez = ar.sum
print(rez)