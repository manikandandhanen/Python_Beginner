available_parts = {
    "1": "computer",
    "2": "monitor",
    "3": "mouse",
    "4": "keyboard",
    "5": "mouse mat",
    "6": "hdmi cable",
    "7": "dvd drive"
}
current_choice = None
computer_parts = {}  # create an empty dictionary

while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        if current_choice in computer_parts:
            # it's already in, so remove it
            print(f"Removing {chosen_part}")
            computer_parts.pop(current_choice)
        else:
            print(f"adding {chosen_part}")
            computer_parts[current_choice] = chosen_part  # key value added
        print(f"Your list now contains: {computer_parts}")
    else:
        print("Please add option in the list")
        for key, value in available_parts.items():
            print(f"{key}: {value}")
        print("0: to finish")

    current_choice = input("> ")
