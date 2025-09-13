unit = int(input("Enter the reading you have"))

print(unit)

if unit>= 400 and unit <= 500 :
    print(f'Your reading is {unit} and pre unit is {6}',unit*6)
elif unit>= 300 and unit <= 400 :
    print(f'Your reading is {unit} and pre unit is {5}',unit*5)
elif unit>= 200 and unit <= 300 :
    print(f'Your reading is {unit} and pre unit is {3}',unit*3)
elif unit <= 200 :
    print("You Dont have to pay bill")    
               
