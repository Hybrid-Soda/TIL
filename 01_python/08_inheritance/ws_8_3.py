# 아래 클래스를 수정하시오.
class Animal:
    def __init__(self):
        pass

class Cat:
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def meow(self):
        print('야옹!')


cat1 = Cat("야옹")
cat1.meow()
