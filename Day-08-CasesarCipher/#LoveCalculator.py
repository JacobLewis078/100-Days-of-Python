# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#convert names to all lowercase
lowercase_name1 = name1.lower()
lowercase_name2 = name2.lower()

#count TRUE in both names
true_total = 0
true_total += lowercase_name1.count("t")
true_total += lowercase_name2.count("t")
true_total += lowercase_name1.count("r")
true_total += lowercase_name2.count("r")
true_total += lowercase_name1.count("u")
true_total += lowercase_name2.count("u")
true_total += lowercase_name1.count("e")
true_total += lowercase_name2.count("e")

#count LOVE in both names
love_total = 0 
love_total += lowercase_name1.count("l")
love_total += lowercase_name2.count("l")
love_total += lowercase_name1.count("o")
love_total += lowercase_name2.count("o")
love_total += lowercase_name1.count("v")
love_total += lowercase_name2.count("v")
love_total += lowercase_name1.count("e")
love_total += lowercase_name2.count("e")

love_score = str(true_total) + str(love_total)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) >=40 and int(love_score) <=50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")