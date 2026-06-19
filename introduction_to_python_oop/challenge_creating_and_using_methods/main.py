class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
            area = self.width * self.height
            return area
        
    def perimeter(self):
            perimeter = (self.width + self.height)*2
            return perimeter

rect = Rectangle(4, 5)
print(rect.area())
print(rect.perimeter())