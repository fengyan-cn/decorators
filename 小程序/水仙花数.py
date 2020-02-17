def judgenum(n):
    unit = int(n % 10)
    decade = int(n / 10 % 10)
    hundred = int(n / 100 % 10)
    if n == pow(unit,3) + pow(decade,3) + pow(hundred,3):
        print('%s是水仙花数'%n)

for i in range(100,1000):
    judgenum(i)
