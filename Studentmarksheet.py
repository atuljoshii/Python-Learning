hindi = int(input("Enter The marks of hindi "))
english = int(input("Enter The marks of english "))
math = int(input("Enter The marks of math "))
science = int(input("Enter The marks of science "))
sst = int(input("Enter The marks of sst"))

print(hindi,english,math,science,sst)

Total_marks = english+sst+hindi+science+math

persentage = Total_marks/500*100

print(persentage)



if persentage>=85 and persentage<=100:
    print("Grade A")
elif persentage>=75 and persentage<=85:
    print("Grade B")
elif persentage>=65 and persentage<=75:
    print("Grade C")
elif persentage>=55 and persentage<=65:
    print("Grade D")
elif persentage>=50 and persentage<=55:
    print("Grade E")
else:
    print("You Enter Wrong Day")
