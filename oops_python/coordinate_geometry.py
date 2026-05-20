## make a class of coordinate geometry by using followin cases 

"""
Write OOP classes to handel the following Scenarios:

-A user can create and view 2D cordinates
-A user can find out the distance between the two cordinate 
-A user can find the distance of cordinate form the origin 
-A user can check if a point lies on a given line  
-A user can find the distance between a given 2D point and a given line 
 """


class Point :

    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y
        
    def __str__(self):
        return '<{},{}>'.format(self.x_cod,self.y_cod)

    def euclidean_distance(self,other):
        distance=((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod)**2)**0.5
        return distance
        
    def origin_distance(self):
        distance=((self.x_cod-0)**2+(self.y_cod-0)**2)**0.5
        return distance


class Line:

    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C

    def __str__(self):
        return '{}x + {}y + {}'.format(self.A,self.B,self.C)

    def Point_on_line(line,point):
        if line.A*point.x_cod +line.B*point.y_cod+line.C==0:
            return " Lies on the line"
        else :
            return "does not lies on the line"

    def shortest_distance(line,point):
        return abs(line.A*point.x_cod+line.B*point.y_cod+line.C)/((line.A)**2+(line.B)**2)**0.5

## test 


p1=Point(0,0)
p2=Point(1,4)
print(p1)
print(p2)

print(p1.euclidean_distance(p2))


print(p1.origin_distance())


l1=Line(2,3,5)
p1=Point(2,0)
print(l1)


print(l1.Point_on_line(p1))

print(l1.shortest_distance(p1))