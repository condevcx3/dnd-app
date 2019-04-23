""" 
Author: Connor Cozens
E-Mail: cozcon@gmail.com

Summary:    Class that imitates rolling 4d6 and dropping
            the lowest one, rerolling if the total of the
            rolls is less than 70.
"""
import random
number_list = []

# Roll 6 Numbers Between 4 and 18
while (sum(number_list) < 70):
    number_list = []
    for i in range(6):
        number_list.append(random.randint(3,18))
    # If the total is greater than or equal to 70, break
    if (sum(number_list) >= 70):
        break

# Print out the 6 stats
print("Your stats are: ")
for i in range(6):
    print("\t " + str(i+1) + ": " + str(number_list[i]))
# Print out the total of the stats
print("The total of your stats is: " + str(sum(number_list)))