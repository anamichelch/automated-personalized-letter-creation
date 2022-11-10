

#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
with open('Input/Names/invited_names.txt') as names:
    names = names.readlines()

with open('Input/Letters/starting_letter.txt') as letter:
    content = letter.read()

all_new_contents = []

#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

for name in names:
    new_name = name.strip('\n')
    new_content = content.replace('[name]',new_name)
    with open(f'./Output/ReadyToSend/letter_for_{new_name}.txt', mode="w") as f:
        f.write(new_content)





