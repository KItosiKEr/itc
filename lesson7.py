def rev_list():
    list_1 = ['name' , 'age' , '1' , '19']
    print(list_1[:2][::-1])
    print(list_1[2:4][::-1])
    list2 = list_1[:2][::-1]
    list3 = list_1[2:4][::-1]


rev_list()   


f1 = 1 
f2 = 1

n = int(input())
print(f1,f2,)
while f2 < n:
    f1,f2 = f2,f1 + f2
    print(f2,)

def suma():
    a = int(input('введите числло :'))
    b = int(input('введите втророе число :'))
    rav = a + b
    print(rav)

suma() 

def subtraction():
    a = int(input(":первое число:"))
    b = int(input(":вторчое число :"))
    ravno = a - b 
    print(ravno)

subtraction()  

def two_funk():
    suma()
    subtraction()

two_funk()    