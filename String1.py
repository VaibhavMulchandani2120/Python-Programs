s=input("Enter any String : ")

up=0
lw=0
al=0
nm=0
sp=0
spc=0

for i in s:
    if i.isupper():
        up=up+1
    elif i.islower():
        lw=lw+1
    if i.isalpha():
        al=al+1
    elif i.isnumeric():
        nm=nm+1
    elif i.isspace():
        sp=sp+1
    else:
        spc=spc+1
    


print("Total Upper Char: ",up)
print("Total Lower Char: ",lw)
print("Total Alphabets Char: ",al)
print("Total Numeric Char: ",nm)
print("Total Space Char: ",sp)
print("Total Special Char: ",spc)


