def anagramkSolution(s1, s2):
    alist = list(s2)
    pos1 = 0
    stillOK = True
    while pos1 < len(s1) and stillOK:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
            else:
                pos2 = pos2 + 1
        if found:
            alist[pos2] = None  # 为防止重复查找，每查找到一个对应的便赋值为NONE
            print(alist)
        else:
            stillOK = False  # 如果s2中一个字符没有在s1中找到就说明查找失败了，跳出循环
        pos1 = pos1 + 1
    return stillOK

print(anagramkSolution('abcd', 'dcba'))
