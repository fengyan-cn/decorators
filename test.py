#函数
def user_check(func):
    def wrapper(username,password):
        if(username != 'root'):
            raise Exception('permission denied')
        elif(password != '1234'):
            raise Exception('password incorrect')
        else:
            #在函数内部被使用的函数
            return func(username,password)
    #返回的另一个函数
    return wrapper

#装饰器使用.为被调用的函数
@user_check
def login_user(username,password):
    print('login success')

login_user('root','1234')