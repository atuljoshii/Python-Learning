print("Grosary store")

aata = int (input("Enter price Of Aata :"))
maida = int (input("Enter The price Of maida :"))
suji = int (input("Enter The price Of suji:"))
tail = int (input("Enter The price Of tail:"))
masala = int (input("Enter The price Of masala :"))

total = aata+maida+suji+tail+masala
print(total)

discountp = int (input("Enter The discount you want to get:"))

discount = total*(discountp/100)
finaldis = total-discount


print("The Discount you get is ",finaldis)


#tottal*dis?100


#Discount % = (Discount Amount / Marked Price) × 100



