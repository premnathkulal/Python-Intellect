def operate(str):
    ii = int(str[0])
    for i in range(len(str)):
        if str[i] in '+-*/%':
            if str[i] == '+':
                ii = ii + int(str[i + 1])
            elif str[i] == '-':
                ii = ii - int(str[i + 1])
            elif str[i] == '*':
                if str[i+1] == '*':
                    ii = ii ** int(str[i + 1])
                else:
                    ii = ii * int(str[i + 1])

            elif str[i] == '%':
                ii = ii % int(str[i + 1])

            elif str[i] == '/':
                if int(str[i + 1]) == 0:
                    continue
                else:
                    ii = ii / int(str[i + 1])
    return ii

def splittings(l):
    n = len(l)
    for i in range(2**n):
        left = [e for b, e in enumerate(l) if i & 2**b]
        right = [e for b, e in enumerate(l) if not i & 2**b]
        yield left, right

def expressions(l):
    if len(l) == 1:
        yield l[0]
    else:    
        for left, right in splittings(l):
            if not left or not right:
                continue
            for el in expressions(left):
                for er in expressions(right):
                    for operator in '+-*/%':
                        yield el + operator + er


print("Enter numbers : ")
inputArray = input().split()
inputString = ''.join(inputArray)

print("Enter Target : ")
target = int(input())

print('\nDifferent combinations of operator to reach given target are :')

for x in expressions(inputString):
    result = operate(x)
    if result == target:
        print(x,"=",result)
