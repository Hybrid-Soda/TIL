one = 3
two = 5
if one and two:
    print('and 연산 통과')
else:
    print('and 연산 통과 못함')

one = 3
two = 0
if one or two:  # if 3: 과 같은 조건문
    print('or 연산 통과')
else:
    print('or 연산 통과 못함')
print(one or two)

# 빈문자열은 True도 False도 아님
print('' == True)
print('' == False)

# 그러나 빈문자열을 조건문에 넣으면 False로 처리됨
if '':
    print('빈 문자열은 빈 문자열')
else:
    print('아무일도 ..')

three = ''
four = '4'

print(three and four)
if three and four:  # if '':
    print('3과 4')
else:
    print('실패')

# 0이 아니다 라고 하는게 더 직관적
if one > 0 or one < 0:
    pass
if one != 0:
    pass

if one % 2:
    print('홀수')

if one % 2 == 1:
    print('홀수')
else:
    print('짝수')

if True:
    print('홀홀')