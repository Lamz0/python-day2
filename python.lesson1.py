age = int(input("Enter you age: "))
if age >= 18 and age <= 100: 
    print('You are ready to vote')
elif age < 18 and age >= 16:
    print('You can get drivers license')
else:
    print("You are not allowed to vote or have drivers lisence")