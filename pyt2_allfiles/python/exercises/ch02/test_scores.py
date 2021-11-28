#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
#added these three variables and then put them in total score
score1 = int(input("Enter test score: "))
score2 = int(input("Enter test score: "))
score3 = int(input("Enter test score: "))
total_score = score3 + score2 + score1

# calculate average score
average_score = round(total_score / 3)
             
# format and display the result
print("======================")
print("Your Scores:  ", score1, score2,score3,"\nTotal Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye!")


