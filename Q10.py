"""Write a python program to change the first item (22) of a list within the following tuple
to 222.
tuple1 = (11, [22, 33], 44, 55)"""
t1=  (11, [22, 33], 44, 55)
temp=t1[1][1]
t1[1][1]=222
print(t1)

