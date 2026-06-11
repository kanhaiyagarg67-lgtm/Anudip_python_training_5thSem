'''
Problem Statement:
Compare correct answers with student answers and:
1. Calculate score
2. Display incorrectly answered question numbers
3. Count correct and wrong answers
4. Determine Pass/Fail (minimum 60%)
'''

# List containing correct answers
correct = ['A', 'C', 'B', 'D', 'A']

# List containing student's answers
student = ['A', 'B', 'B', 'D', 'C']

# ---------------------------------------------
# Task 1: Calculate Score
# ---------------------------------------------

print("Score of Student :")

# Variable to store score
score = 0

# Traverse both lists using index
for i in range(len(correct)):

    # If answer matches, increase score
    if correct[i] == student[i]:
        score += 1

# Display score
print(score)

print("--------------------------------------")

# ---------------------------------------------
# Task 2: Display incorrectly answered questions
# ---------------------------------------------
print("The incorrectly question numbers are:")
# Empty list to store wrong question numbers
wrong_answer = []

# Traverse both lists again
for i in range(len(correct)):

    # If answers do not match
    if correct[i] != student[i]:

        # Store question number (i+1)
        wrong_answer.append(i + 1)

# Display list of wrong question numbers
print(wrong_answer)

print("--------------------------------------")

# ---------------------------------------------
# Task 3: Count correct and wrong answers
# ---------------------------------------------

print("No. of correct and wrong answers are:")

# Counters for correct and wrong answers
correct_ans = 0
wrong_ans = 0

# Traverse lists again
for i in range(len(correct)):

    # Count correct answers
    if correct[i] == student[i]:
        correct_ans += 1

    # Count wrong answers
    else:
        wrong_ans += 1

# Display counts
print("Correct answers are:", correct_ans)
print("Wrong answers are:", wrong_ans)

print("------------------------------")

# ---------------------------------------------
# Task 4: Determine Pass/Fail
# ---------------------------------------------

# Calculate percentage
percentage = (correct_ans / (correct_ans + wrong_ans)) * 100

# Check pass/fail condition
if percentage >= 60:
    print("Student is Pass")
else:
    print("Student is Fail")
