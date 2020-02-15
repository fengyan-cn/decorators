from collections import Iterable

print(isinstance([],Iterable))
print(isinstance({},Iterable))
print(isinstance((),Iterable))
print(isinstance('',Iterable))
print(isinstance(6,Iterable))

ll = iter(range(20))

while True:
    try:
        print(next(ll))
    except StopIteration:
        break

