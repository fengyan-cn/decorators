def check(test):
    def check_inner(filename):
        a = filename.split('.')
        if(a[1] != 'txt'):
            raise Exception('文件格式不对')
        else:
            return test(filename)
    return check_inner

@check
def test(filename):
    print('success')

test('D:\test.txt')
