#write a program that has a class name circle,use a classs verible to define the  values of constant pi.use this class varible to caluclate area and circumferencee with specified radius,where radius is 7.5
class circle:
    pi=3.14159
    def cir(self,radius):
        print('area=',circle.pi*radius**2)
        print('cir=',2*circle.pi*radius)
n=circle()
n.cir(7.5)
