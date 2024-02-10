isp = {
    '(': 0,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}
icp = {
    '(': 3,
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
}
infix = '(6+5*(2-8)/2)'
postfix = []
stack = []

for token in infix:
    if token.isdecimal() == True:
        postfix.append(token)
    elif token in '(+-*/':
        if not stack:
            stack.append(token)
        elif icp[token] > isp[stack[-1]]:
            stack.append(token)
        elif icp[token] <= isp[stack[-1]]:
            while stack and icp[token] <= isp[stack[-1]]:
                postfix.append(stack.pop())
            stack.append(token)
    elif token == ')':
        while stack[-1] != '(':
            postfix.append(stack.pop())
        stack.pop()

while stack:
    postfix.append(stack.pop())

print(''.join(postfix))

# ------------------------------------
postfix = '6528-*2/+'
stack = []

for char in postfix:
    print(stack)
    if char.isdecimal() == True:
        stack.append(char)
    else:
        B = int(stack.pop())
        A = int(stack.pop())
        if char == '+':
            stack.append(A + B)
        elif char == '-':
            stack.append(A - B)
        elif char == '*':
            stack.append(A * B)
        elif char == '/':
            stack.append(A / B)
    
print(stack.pop())