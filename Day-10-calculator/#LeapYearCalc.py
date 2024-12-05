# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
    print("This may be a leap year, test if divisible by 100")
    if year % 100 == 0:
        print("This year is divisible my 100 meaning it may not be a leap year actually, lets check one more thing.")
        if year % 400 == 0:
            print(f"{year} is a leap year!")
        else:
            print(f"{year} is not a leap year..")
    else:
        print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year..")


