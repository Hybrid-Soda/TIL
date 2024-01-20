# 아래 클래스를 수정하시오.
class StringRepeater:
    def repeat_string(self, count, my_string):
        for i in range(count):
            print(my_string)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
