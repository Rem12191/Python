import random

# Define possible responses
affirmation_responses = ["Yes, definitely.", "It is certain.", "Without a doubt."]
non_commital_responses = ["Reply hazy, try again.", "Ask again later.", "Cannot predict now."]
negative_responses = ["Don't count on it.", "My sources say no.", "Outlook not so good."]

# Function to simulate Magic 8 Ball
def magic_8_ball():
    question = input("Ask the Magic 8 Ball a yes-no question: ")
    response_category = random.choice(["affirmation", "non_commital", "negative"])

    if response_category == "affirmation":
        print(random.choice(affirmation_responses))
    elif response_category == "non_commital":
        print(random.choice(non_commital_responses))
    else:
        print(random.choice(negative_responses))

# Main program loop
while True:
    magic_8_ball()
    
    while True:
        another_question = input("Ask another question? (yes/no): ").lower()
        if another_question in ["yes", "no"]:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if another_question == "no":
        break

print("Goodbye! Thank you for using the Magic 8 Ball.")