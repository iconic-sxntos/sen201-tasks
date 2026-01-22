candidates = {
    "Candidate A": 0,
    "Candidate B": 0,
    "Candidate C": 0
}

def display_candidates():
    print("\nAvailable Candidates:")
    for candidate in candidates:
        print(candidate)

def cast_vote():
    display_candidates()
    choice = input("Enter candidate name: ")

    if choice in candidates:
        candidates[choice] += 1
        print("Vote cast successfully!")
    else:
        print("Invalid candidate.")

def display_results():
    print("\nVoting Results:")
    for candidate, votes in candidates.items():
        print(f"{candidate}: {votes} votes")

while True:
    print("\n1. Vote")
    print("2. View Results")
    print("3. Exit")

    option = input("Choose an option: ")

    if option == "1":
        cast_vote()
    elif option == "2":
        display_results()
    elif option == "3":
        print("Voting ended.")
        break
    else:
        print("Invalid option.")
