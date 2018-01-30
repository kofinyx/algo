'''
Created on Jan 26, 2018

@author: fiihagan30
'''


class stack():

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


s = stack()
print('It is {} that mystack is empty'.format(s.isEmpty()))
s.push(2)
s.push(4)
s.pop()
s.push('pen')
print('{} is on top of the stack s'.format(s.peek()))


def revstring(mystr):
    st = stack()
    l = ''
    for c in list(mystr):
        st.push(c)
    while not st.isEmpty():
        l = l + st.pop()
    return l


def revstring2(mystr):
    l = ''
    myl = list(mystr)
    myl.reverse()
    for i in myl:
        l = l + i
    return l


print(revstring('Emmanuel'))
print(revstring2('Emmanuel'))


def baseConverter(decNum, base):
    remStack = stack()
    digits = "0123456789ABCDEF"
    while decNum > 0:
        rem = decNum % base
        remStack.push(rem)
        decNum = decNum // base
    binString = ''
    while not remStack.isEmpty():
        binString = binString + digits[remStack.pop()]
    return binString


num = 233
base = 16
print('The number {} is equal to {} in base {}'.format(
    num, baseConverter(num, base), base))
