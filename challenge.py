# Import required modules
import random 
import time

# Define constants
OPERATORS = ["+", "-", "/", "*"]  # Possible mathematical operators
MIN_OPERAND = 1  # Minimum possible value for operands
MAX_OPERAND = 14  # Maximum possible value for operands
TOTAL_PROBLEMS = 12  # Total number of problems the user will solve

# FUNCTION: generate a random math problem
def generate_problem():
    # Generate random numbers for the problem
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    # Choose a random operator
    operator = random.choice(OPERATORS)
    
    # Construct the problem as a string
    expr = str(left) + " " + operator + " " + str(right)
    # Calculate the answer to the problem
    answer = eval(expr)
    
    # If the answer is a whole number float, convert to integer
    if isinstance(answer, float) and answer.is_integer():
        answer = int(answer)
    
    # Return the problem and its answer
    return expr, answer

# Initialize a counter for incorrect answers
wrong = 0
# Prompt user to start the challenge
input("Press Enter to start!")
# Display a separator
print("----------------------")

# Record the time when the challenge starts
start_time = time.time()

# Loop to generate and ask user TOTAL_PROBLEMS number of problems
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    # Keep prompting the user until they answer correctly
    while True:
        guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
        # Exit loop if user's answer matches the correct answer
        if guess == str(answer):
            break
        # If incorrect, increment the wrong counter
        wrong += 1
        
# Record the time when the challenge ends
end_time = time.time()
# Calculate total time taken
total_time = end_time - start_time
        
# Display a separator
print("----------------------")
# Congratulate user and display their time
print("Nice work! You finished in,", total_time, "seconds!")  

