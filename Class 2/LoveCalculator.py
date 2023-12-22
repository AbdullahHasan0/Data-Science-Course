f_name = input("Enter Your Name:\n").upper()  # Prompt the user to enter their name and convert it to uppercase
s_name = input("Enter Partner Name:\n").upper()  # Prompt the user to enter their partner's name and convert it to uppercase
name = f_name + s_name  # Concatenate the two names

c1 = sum(character in ['T', 'R', 'U', 'E'] for character in name)  # Count the occurrences of characters 'T', 'R', 'U', 'E' in the concatenated name
c2 = sum(character in ['L', 'O', 'V', 'E'] for character in name)  # Count the occurrences of characters 'L', 'O', 'V', 'E' in the concatenated name

print(f"Your Love Compatibility Score is {c1}{c2}")  # Print the love compatibility score