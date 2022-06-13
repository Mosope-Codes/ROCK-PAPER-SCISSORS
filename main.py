import random

user_response_in_upper_case = ""
cpu_selection = ""

while user_response_in_upper_case == cpu_selection:
    rock_paper_scissors = ["R", "P", "S"]
    cpu_selection = random.choice(rock_paper_scissors)
    cpu_selection_in_uppercase = cpu_selection.upper()

    user_response = input("Pick 'R' for Rock, 'P' for Paper, 'S' for Scissors: ")
    user_response_in_upper_case = user_response.upper()
    while user_response_in_upper_case not in rock_paper_scissors: 
        print("*Error: Input either 'R', 'P' or 'S' ")
        user_response = input("Pick 'R' for Rock, 'P' for Paper, 'S' for Scissors: ")
        user_response_in_upper_case = user_response.upper()
        continue

    if user_response_in_upper_case == "R":
        user_response_to_words = "Rock"
    if cpu_selection_in_uppercase == "R":
        cpu_selection_to_words = "Rock"
    if user_response_in_upper_case == "P":
        user_response_to_words = "Paper"
    if cpu_selection_in_uppercase == "P":
        cpu_selection_to_words = "Paper"
    if user_response_in_upper_case == "S":
        user_response_to_words = "Scissors"
    if cpu_selection_in_uppercase == "S":
        cpu_selection_to_words = "Scissors"


   
    print(f"Player({user_response_to_words}) : CPU({cpu_selection_to_words})")

    if (user_response_in_upper_case == "R") and (cpu_selection_in_uppercase == "S"):
        print("Player won")
    elif (user_response_in_upper_case == "P") and (cpu_selection_in_uppercase == "R"):
        print("Player won")
    elif (user_response_in_upper_case == "S") and (cpu_selection_in_uppercase == "P"):
        print("Player won")

    if (cpu_selection_in_uppercase == "R") and ( user_response_in_upper_case == "S"):
        print("CPU won")
    elif (cpu_selection_in_uppercase == "P") and (user_response_in_upper_case == "R"):
        print("CPU won")
    elif (cpu_selection_in_uppercase == "S") and (user_response_in_upper_case == "P"):
        print("CPU won")

    if user_response_in_upper_case == cpu_selection_in_uppercase:
        print("Its a tie. ")
    continue        

    

