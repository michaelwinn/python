
class Vector():
    def __init__(self, data=[]):
        self.data = data

    def add(self, other_vector):
        num = []
        for i in range(0,len(self.data)):
            num.append(self.data[i] + other_vector.data[i])
        return Vector(num)

    def subtract(self, other_vector):
        num = []
        for i in range(0,len(self.data)):
            num.append(self.data[i] - other_vector.data[i])
        return Vector(num)

    def dot_product(self, other_vector):
        num = 0
        for i in range(0,len(self.data)):
            num += self.data[i]*other_vector.data[i]
        return num

    def __str__(self):
        return str(self.data)

    


a = Vector([2,1,-2])
b = Vector([-3,2,1])

c = a.add(b)

print(a)
print(b)
print(c)

print(a.add(c))

print(a.dot_product(b))
