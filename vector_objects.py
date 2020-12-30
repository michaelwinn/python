import math

class Vector():
    def __init__(self, data=[]):
        self.data = data

    def __add__(self, other_vector):
        """Define the additive property of vectors"""
        num = []
        for i in range(0,len(self.data)):
            num.append(self.data[i] + other_vector.data[i])
        return Vector(num)

    def __sub__(self, other_vector):
        num = []
        for i in range(0,len(self.data)):
            num.append(self.data[i] - other_vector.data[i])
        return Vector(num)

    def __mul__(self, other_vector):
        if type(other_vector) == type(self):
            return self.dot_product(other_vector)
        elif isinstance(other_vector,int) or isinstance(other_vector,float):
            num = []
            for i in range(0,len(self.data)):
                num.append(other_vector*self.data[i])
            return Vector(num)

    def __rmul__(self, other_vector):
        return self.__mul__(other_vector)

    def __truediv__(self, other_vector):
        if isinstance(other_vector,int) or isinstance(other_vector,float):
            num = []
            for i in range(0,len(self.data)):
                num.append(self.data[i] / other_vector)
            return Vector(num)
        else:
            raise TypeError('Can only divide vector by scalar.')

    def dot_product(self, other_vector):
        num = 0
        for i in range(0,len(self.data)):
            num += self.data[i]*other_vector.data[i]
        return num

    def norm(self):
        return math.sqrt(self.dot_product(self))

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self.data)

    def __iter__(self):
        return self.data.__iter__()
