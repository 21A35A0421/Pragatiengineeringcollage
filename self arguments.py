#program to create self arg and access an obj
class abc:
    attribute1=10
    def display(self):
        print('this is in class')
obj=abc()
print(obj.attribute1)
obj.display()
