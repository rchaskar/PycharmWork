n = int(input("Enter number of employees"))

employees={} #dictionary

for i in range(n):
        name=input("Enter Name")
        salary= input("Enter Salary")
        employees[name]=salary  #name is key and salary is value

while True:
    name=input("please enter name of an employee u want to search")
    salary=employees.get(name,-1) #will get the name from employee dictionary and
                                   #will return the salary of that employee
    if salary == -1:
        print("Employee does not exist")
    else:
        print("Salary of ",name ,"is",salary)
    choice=input("Do u want to continue further [Yes|No]")
    if choice=='No':
        break


x=5
if(x>3 and
   x<6):
    print(x)