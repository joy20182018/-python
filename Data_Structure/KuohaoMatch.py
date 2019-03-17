'''

栈的应用

''''''
from Stack import Stack

def perCheck(str):
    s = Stack()

    if not s.isEmpty():
         for i in range(len(str)):
            if str[i] == '(':
                s.push(str[i])
            elif str[i] == ')':
                if not s.isEmpty():
                    s.pop()
                else:
                    s.push(str[i])


            elif str[i] == '[':
                s.push(str[i])
            elif str == ']':
                if not s.isEmpty() :
                    s.pop()
                else:
                    s.push(str[i])


            elif str[i] == '{':
                s.push(str[i])
            elif str == '}':
                if not s.isEmpty():
                    s.pop()
                else:
                    s.push(str[i])


            else:
                print("error")


        if s.isEmpty():
            print("Matching Success")
        else:
            print("Matching Failed")

    else:
        print("benlaijiushikongde")


str = '({{)[[}}]]'
perCheck(str)
