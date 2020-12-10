data = {'roll_num':[],
		'name':[],
		'age':[],
		'marks':[]}

def appendDict(dict):
    check="n"
    check = input("\nDo you want to enter a record ? press (y) or (any key) : ")
    while check=='y' or check=='Y':
            rollNum=input("Enter Roll Number :")
            name=input("Enter Name :")
            while True:
                try:
                    age=int(input("Enter Age :"))
                    break
                except ValueError:
                    print("*Age in number [X]")
            while True:
                try:
                    marks=int(input("Enter Marks :"))
                    break
                except ValueError:
                    print("*Marks in number [X]")
                    
            if  rollNum!="" and name!="" and age!=0 and age<=120 and marks<=100:
                dict['roll_num'].append(rollNum)
                dict['name'].append(name)
                dict['age'].append(age)
                dict['marks'].append(marks)
            else:
                print("\nENTERED DATA IS IS WRONG FORMAT.")
                if rollNum=="":
                    print("Roll number is not filled. [X]")
                if name=="":
                    print("Name is not filled. [X]")
                if age > 120 or age==0:
                    print("Age should be under 120 and not Zero. [X]")
                if marks>100:
                    print("Marks should be under 100. [X]")
            check = input("\nDo you want to enter a record ? press (y) or (any key) :") 

def printDict(dict):
    rollno=dict['roll_num']
    print(rollno)
    
appendDict(data)
printDict(data)
print(data)

