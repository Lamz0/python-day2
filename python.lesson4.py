for i in range(1,15):
    if i == 3:
        print("skipping number 3")
        continue
    if i == 15:
        print("Stopping at number 15")
        break 
    print('Current number is: ', i)