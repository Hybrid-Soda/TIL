# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, w, h) -> None:
        self.width = w
        self.height = h

    def print_info(self):
        print(f'Width: {self.width}')
        print(f'Height: {self.height}')
        print(f'Area: {self.width * self.height}')
        print(f'Perimeter: {2 * (self.width + self.height)}')


shape1 = Shape(5, 3)
shape1.print_info()
