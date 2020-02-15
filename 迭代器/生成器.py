def foo():
    for i in range(10):
        yield {'text':1,'sortable':2}


for i in foo():
    print(i)