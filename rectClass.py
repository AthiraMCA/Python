

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def __str__(self):
        return f"Rectangle(length={self.length}, width={self.width}, area={self.area()})"

if __name__ == "__main__":
    length = int(input("Enter the length of the rectangle: "))
    width = int(input("Enter the width of the rectangle: "))
    rect = Rectangle(length, width)

    print(f"The area of the rectangle is: {rect.area()} square units")
    print(rect)