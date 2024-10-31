limit = int(input ("Enter a number: "))
count = 0 

for num in range (3, limit + 1, 3): #Only even numbers
    count += 1
print("Sum of even numbers up to,", limit, "is:", count)