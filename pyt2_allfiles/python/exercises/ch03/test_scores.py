#!/usr/bin/env python3

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter end to end input")
print("======================")

# initialize variables
cont = True

while cont:
    counter = 0
    score_total = 0
    test_score = "0"
    while test_score != "end":
        test_score = str(input("Enter test score: "))
        if test_score == "end":
            break
        if int(test_score) >= 0 and int(test_score) <= 100:
            score_total += int(test_score)
            counter += 1
        else:
            while int(test_score) < 0 or int(test_score) > 100:
                print(f"Test score must be from 0 through 100. "
                                       f"Score discarded. Try again:")
                test_score = str(input("Enter test score: "))
            score_total += int(test_score)
            counter += 1


    # calculate average score
    average_score = round(score_total / counter)

    # format and display the result
    print("======================")
    print(f"Total Score: {score_total}"
          f"\nAverage Score: {average_score}")
    print()
    answer = str(input("Enter another set of test scores (y/n)? "))
    while answer != "y" and answer != "n":
        print()
        print("Invalid Selection! Chose again")
        answer = str(input("Get entries for another trip (y/n)? "))
    if answer == "n":
        cont = False


