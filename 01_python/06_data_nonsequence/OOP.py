# OOP : 객체 지향 프로그래밍
a = 1
b = '가'
c = [1, 2, 3]
d = range(1, 10)
e = map(int, '123')
f = set()
g = dict()
def some():
    return False
h = some

def other(arg):
    print(arg)

def some(func, arg):
    func(arg)
    return None

some(other, '안녕하세요')

# a, b, c, d 모두 리스트 -> 모두 append 메서드 사용가능
a = [1, 2]
b = ['a', 'b']
c = ['ㄱ', 'ㄴ']
d = list('가')

class Person:
    def breath(self):
        pass