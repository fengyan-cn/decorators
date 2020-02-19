def varfunc():
    var = 0
    print('var = %d' % var)
    var += 1

if __name__ == '__main__':
    for i in range(3):
        varfunc()


class Varfunc(object):
    staticvar = 5
    def varfunc(self):
        self.staticvar += 1
        print(self.staticvar)
print(Varfunc.staticvar)
a = Varfunc()
for i in range(3):
    a.varfunc()
