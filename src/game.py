"""Guess number game"""

import numpy as np

number = np.random.randint(1, 101) # generating the number

# count of tries
count = 0

while True:
    count+=1
    predict_number = int(input("Guess number from 1 to 100: "))
    
    if predict_number > number:
        print("Number should be lower!")

    elif predict_number < number:
        print("Number should be higher!")
    
    else:
        print(f"You did guess right! The number is = {number}, {count} tries")
        break #end game, breaking the loop
