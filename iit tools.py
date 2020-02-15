class square:
    def CalculateArea(self):
#def is use to define some function
        print("Enter side")
#print statement is use to get print of written
        self.s=float(input())
#float function is use to enter decimal value
        area=self.s*self.s
        return(area)
#return is use for returning the value 
    def CalculatePerimeter(self):
#def is use to define some function
        perimeter=4*self.s
        return(perimeter)
c=square()
x=c.CalculateArea()
#calculating the area
y=c.CalculatePerimeter()
#calculating the perimeter
print("Area of square is=%f"%(x))
print("Perimeter of square is=%f"%(y))
