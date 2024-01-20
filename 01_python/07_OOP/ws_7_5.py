# 아래 클래스를 수정하시오.
class Shape:
    def __init__(self, w, h) -> None:
        self.width = w
        self.height = h

    def __str__(self):
        return f'Shape: width={self.height}, height={self.width}'


shape1 = Shape(5, 3)
print(shape1)
