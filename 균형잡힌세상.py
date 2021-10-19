while True:
    stack = []
    s = input()
    if s == '.':
        break
    for c in s:
        if c == '(' or c == '[':
            stack.append(c)
        elif c == ')':       
            if len(stack) == 0 or stack.pop() != '(':
                print('no')
                break
        elif c == ']':       
            if len(stack) == 0 or stack.pop() != '[':
                print('no')
                break
    else:
        if len(stack) == 0:
            print('yes')
        else:
            print('no')