class Employee:
    def __init__(self,Deptno,Empid,Ename,sal):
        self.Empid = Empid
        self.Ename = Ename
        self.sal = sal
        self.Deptno = Deptno

def Add_Emp(Deptno,Empid,Ename,sal):
    e = Employee(Deptno,Empid,Ename,sal)
    emptup = (Deptno,Empid,Ename,sal)
    f = open("emp.txt","a")
    f.write(str(emptup))
    f.write("\n")
    f.close()

def Display_Emp():
    with open("emp.txt","r") as emp_f:
        for line in emp_f:
            print(line)

def Separate_Emp():
    data_file = open("emp.txt","r")
    content = data_file.readlines()[-1]
    line = str(content)
    data = line.strip(")\n").strip("(").split(",")
    if(data[0] == str(10)):
        f10 = open("emp10.txt","a")
        f10.write(line)
    if(data[0] == str(20)):
        f20 = open("emp20.txt","a")
        f20.write(line)
    if(data[0] == str(30)):
        f30 = open("emp30.txt","a")
        f30.write(line)                




while(True):
    print("MENU")
    print("1. Add_emp\n2. Display_emp\n3. Seperate_data\n4. Exit\n")
    n1 = int(input("choose an option\n"))
    menu_list = [1,2,3,4]
    if n1 not in menu_list:
        n1 = int(input("please choose an option from the menu\n"))
    elif(n1 == 1):
        print("enter the details: ")
        Empid = int(input("enter the employee id\n"))
        if(Empid<100):
            print("Enter the correct employee id\n")
            Empid = int(input("enter the employee id\n"))
    
        Ename = input("Enter the name of the employee\n")
        Ename = Ename.upper()
    
        sal = int(input("enter the salary\n"))
        if(sal <3000):
            print("enter correct salary\n")
            sal = int(input("enter the salary\n"))
    
        deplist = [10,20,30]
        Deptno = int(input("Enter department number\n"))
        if Deptno not in deplist:
            print("enter the correct dept no\n")
            Deptno = int(input("Enter department number\n"))
    
        Add_Emp(Deptno,Empid,Ename,sal)

    elif(n1 == 2):
        Display_Emp()

    elif(n1 == 3):
        Separate_Emp()

    else:
        break





