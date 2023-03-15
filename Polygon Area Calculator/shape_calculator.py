class Rectangle:
    
    def __init__(self, width, height):     
        self.width = width
        self.height = height
    
    def set_width(self, width):      
        self.width = width
    
    def set_height(self, height):      
        self.height = height
        
    def get_area(self):      
        area = self.width * self.height
        return area
        
    def get_perimeter(self):  
        perimeter = 2 * self.width + 2 * self.height
        return perimeter
        
    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
        
    def get_picture(self):
        
        if self.height < 50 and self.width < 50:
            picture = ''
            for i in range(self.height):
                picture += '*' * self.width + '\n'
            return picture
        else:
            return "Too big for picture."
            
        
    def get_amount_inside(self, shape):
        
        width_fit = self.width // shape.width
        height_fit = self.height // shape.height
        return width_fit * height_fit
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)
    
    def set_side(self, side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f"Square(side={self.width})"
        