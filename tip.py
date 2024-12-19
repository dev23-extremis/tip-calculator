print("WELCOME TO THE TIP CALCUALTOR!")

bill = float(input("What is the total amountof bill? ₹"))

tip = float(input("How much you would like to tip 10, 12, 15 ? "))

num_people =  float(input("How much people will split the bill ? "))

split = bill/num_people

new_bill = 0

if tip == 10:
    new_bill = split * 1.10

elif tip == 12:
    new_bill = split * 1.12

elif tip == 15:
    new_bill = split * 1.15

print(f"Each person should pay ₹{round(new_bill,2)}")
