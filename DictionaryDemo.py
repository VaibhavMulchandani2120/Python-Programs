d={101:"Pankaj",203:"Vaibhav",405:"Neh",506:"Dipak",908:"Vijay"}

print(d)
print(d.get(203))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(405))
print(d)
d.popitem()
print(d)
d1={222:"Vishwa",333:"Milan",444:"Rahul",555:"Abhishek"}
d.update(d1)
print(d)

for i in d:
    print(i," : ",d[i])

d[101]="Akash"
print(d)
