office1=[]
office2=[]
office3=[]
n=int(input("enter the number of employees in first office"))
for i in range(n):
    name=input("enter the employees name")
    salary=input("enter the salary")
    office1[name]=salary
print("dictionary",office1)
num=int(input("enter the number of employees insecond office"))
for i in range(num):
    name1=input("enter the employees name")
    salary1=input("enter the salary")
    office2=[name1]=salary1
    print("dictionary",office2)
office3=office1.copy()
office3.update(office2)
print("merged Dictionary:",office3)
    
