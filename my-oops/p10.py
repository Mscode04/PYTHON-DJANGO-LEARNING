class Shape():
    def area(slef,a,b=0):
        if a and b !=0:
            print(f'rectange area is {a*b}')
        else:
            print(f'area of circle is {(a**2)*3.14}')    
obj=Shape()
obj.area(2)       
obj.area(2,3)       