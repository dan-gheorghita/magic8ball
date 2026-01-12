```python
# Import the random module to generate a random integer
import random

# Define a function to get an answer based on the given answer number
def getAnswer(answerNumber):
    # If the answer number is 1, return a specific answer
    if answerNumber == 1:
       return 'It is certain'
    # If the answer number is 2, return a specific answer
    elif answerNumber == 2:
        return 'It is decidedly so'
    # If the answer number is 3, return a specific answer
    elif answerNumber == 3:
        return 'Yes'
    # If the answer number is 4, return a specific answer
    elif answerNumber == 4:
        return 'Reply hazy, try again'
    # If the answer number is 5, return a specific answer
    elif answerNumber == 5:
        return 'Ask again later'
    # If the answer number is 6, return a specific answer
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    # If the answer number is 7, return a specific answer
    elif answerNumber == 7:
        return 'My reply is no'
    # If the answer number is 8, return a specific answer
    elif answerNumber == 8:
        return 'Outlook not so good'
    # If the answer number is 9, return a specific answer
    elif answerNumber == 9:
        return 'Very doubtful'

# Generate a random answer number between 1 and 9
r = random.randint(1, 9)

# Get the answer for the generated answer number
fortune = getAnswer(r)

# Print the generated fortune
print(fortune)
```