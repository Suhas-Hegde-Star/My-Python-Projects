# Define the function to check the answer
def check_guess(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        # Increasing coorect anwer score
        if guess.lower() == answer.lower():
            print("Correct Answer")
            score = score + 1
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Sorry, Wrong answer. Try again")
            attempt = attempt + 1

    # Lives
    if attempt == 2:
        print("The correct answer is", answer)

score = 0
print("ANIMAL QUIZ !!")

# Question 1
guess1 = input("\nWho is the God of Cricket?(Full Name) ")
check_guess(guess1, "Sachin Ramesh Tendulkar" or "Sachin Tendulkar")

# Question 2
guess2 = input("\nWho won the first ever Cricket World Cup in 1975? ")
check_guess(guess2, "West Indies")

# Question 3
guess3 = input("\n What is the largest cricket stadium in the world by Boundary? ")
check_guess(guess3, "Melbourne")

# Question 4
guess4 = input("\n What is the largest cricket stadium in the world by Capacity?")
check_guess(guess4, "Narendra Modi Stadium")

# Question 5
guess5 = input("\nWhen did India win the latest World Cup? ")
check_guess(guess5, "2024")

# Print the total score
print("\nYour score is", str(score))