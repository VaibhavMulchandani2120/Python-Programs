l=[1,2,1.1,2.2,"tops",True,10,20,1,2,"Python"]

print(l)
l.append(100)
print(l)
l1=l.copy()
l1.append(200)
print(l1)
print(l)
l2=l
print(l2)
l2.append(300)
print(l2)
print(l)

print(l.count(1))
l3=[1000,2000,3000]
l.extend(l3)
print(l)
print(l.index(10))
l.insert(5,101)
print(l)
l.pop()
print(l)
l.pop(10)
print(l)
l.remove(10)
print(l)
l.reverse()
print(l)



