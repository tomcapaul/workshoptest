# Simple program to demonstrate conditionals, loops, processing list data,
# and output

# Create a list of test scores, note they could be read from the keyboard
# or a file
testScores = [101, 106, 76, 12, 70]

# Listing scores in a loop
print("Here are the scores we will process:")
for score in testScores:
    print(score, end=" ")

# Assume first score is the largest
maxScore = testScores[0]

# Set up our variable for summing all test scores to help compute the average
totalScore = 0

# Set up our variable to keep track of how many test scores we have checked
# to help compute the average
testsChecked = 0

# Walk through the list of scores using a for loop

for score in testScores:
    # Check current score against high score and save it as high score if it is bigger
    if score > maxScore:
        maxScore = score

    # Add current score to total of other scores and also increment count of how
    #  many scores have been checked
    totalScore = totalScore + score
    testsChecked = testsChecked + 1

# Now display our results
print()
print("Results from processing scores...")
print("Highest Test Score: ", maxScore)
print("Average Test Score: ", totalScore / testsChecked)

print("-------------------------------------------------------------------------------")
