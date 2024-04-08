print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?") 

name1 = name1.lower()
name2 = name2.lower()

t1 = name1.count("t")
r1 = name1.count("r")
u1 = name1.count("u")
e1 = name1.count("e")

t2 = name2.count("t")
r2 = name2.count("r")
u2 = name2.count("u")
e2 = name2.count("e")

true_count_name1 = t1 + r1 + u1 + e1
true_count_name2 = t2 + r2 + u2 + e2
true_count_total = true_count_name1 + true_count_name2

l1 = name1.count("l")
o1 = name1.count("o")
v1 = name1.count("v")
e1 = name1.count("e")

l2 = name2.count("l")
o2 = name2.count("o")
v2 = name2.count("v")
e2 = name2.count("e")

love_count_name1 = l1 + o1 + v1 + e1
love_count_name2 = l2 + o2 + v2 + e2
love_count_total = love_count_name1 + love_count_name2

trueLove_score = str(true_count_total) + str(love_count_total)
trueLove_score = int(trueLove_score)

if trueLove_score < 10 or trueLove_score >= 90:
    print(f"Your score is {trueLove_score}, you go together like coke and mentos.")
elif trueLove_score >= 40 and trueLove_score <= 50:
    print(f"Your score is {trueLove_score}, you are alright together.")
else:
    print(f"Your score is {trueLove_score}.")
