def postfix(x):
    y = str() # output expression
    p = dict(zip('(^%/*+-', [3,2]))
    stack = list()
    for i in x:
        #print('When i then y',i, type(y))
        if i == '(':
            stack.append(i)
            continue
        
        if i == ')':
            t = stack.pop()
            while not t == '(':
                y += t
            continue
        
        if i in p.keys():
            while p[i] == p[stack[-1]] or p[i] < p[stack[-1]]:
                y += stack.pop()
            continue
        #print(type(y),type(i))
        y += i
        print('Token:', i, 'Stack:', stack, 'Postfix:', y)
    while(len(stack)):
        y += stack.pop()
    return y

x = '(a+b)*c'
print(x)
print(postfix(x))