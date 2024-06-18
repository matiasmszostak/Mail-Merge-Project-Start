name_list = []
letter_list = []

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_content = letter_file.read()

with open("./Input/Names/invited_names.txt") as names_file:
    names_file = names_file.readlines()
    for name in names_file:
        stripped_name = name.strip()
        new_letter = letter_content.replace("[name]", stripped_name)

        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode="w") as completed_letter:
            completed_letter.write(new_letter)