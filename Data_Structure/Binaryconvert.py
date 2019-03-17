'''

栈的应用

'''

# 进制转换
from Stack import StackData

def baseConvert(number, base):
    s = StackData()
    d = '0123456789ABCDEF'
    try:
        num = int(number)
        while num > 0:
            cem = num % base
            s.push(cem)
            num = num // base

        bin = ''
        while s.isEmpty() == False:
            bin = bin + d[s.pop()]

        # print("转换后的%d进制是："% (base), end='')
        # print(bin)
        return bin

    except:
        print("输入错误")

print(baseConvert(15, 16))
