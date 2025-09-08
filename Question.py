english = int (input("Enter The Marks english :"))
maths = int (input("Enter The Marks maths :"))
hindi = int (input("Enter The Marks hindi :"))
science = int (input("Enter The Marks science :"))
sst = int (input("Enter The Marks sst :"))

Total_marks = english+sst+hindi+science+maths

persentage = Total_marks/500*100

print(english,sst,hindi,science,maths)
print(Total_marks)
print(persentage);
