#!/usr/bin/env python3

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")


def get_scores():
    scores = []
    while True:
        score = input("Enter test score: ")
        if score == "x":
            return scores
        else:
            score = int(score)
            if 0 <= score <= 100:
                scores.append(score)
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")


def process_scores(scores):
    scores.sort()
    # calculate average score
    average = sum(scores) / len(scores)

    # format and display the result
    print()
    print("Score total:       ", sum(scores))
    print("Number of Scores:  ", len(scores))
    print("Average Score:     ", average)
    print("Low Score:         ", scores[0])
    print("High Score:        ", scores[len(scores) - 1])
    print("Median Score:      ", scores[int(len(scores)/2)])


def main():
    display_welcome()
    score_total= get_scores()
    process_scores(score_total)
    print("")
    print("Bye!")


# if started as the main module, call the main function
if __name__ == "__main__":
    main()
