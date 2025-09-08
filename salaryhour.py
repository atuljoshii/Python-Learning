Employee = input("Are Your Employee? Yes/No")


if (Employee=="yes"):
    gender = input("Enter your gender m/f")
    if(gender=="m"):
      
        salary = int(input("Enter Your Salary in deight"))
        hour = int(input("Enter Your extera working hour"))
        workinghour = hour*300
        total_salary = workinghour+salary
        print(total_salary)
    else :
        salary = int(input("Enter Your Salary in deight"))
        hour = int(input("Enter Your extera working hour"))
        workinghour = hour*300
        total_salary = workinghour+salary
        print(total_salary)

else :
    print("you are not the employee of this company")
    
    
    
    

