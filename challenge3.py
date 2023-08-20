def highest_consonant_value(s):
    consonant_values = []
    current_value = 0

    consonant_mapping = {
        'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5,
        'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10,
        'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15,
        'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20,
        'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26
    }

    for char in s:
        if char in "aeiou":
            consonant_values.append(current_value)
            current_value = 0
        else:
            current_value += consonant_mapping[char]

    consonant_values.append(current_value)
    return max(consonant_values)

# Taking user input for the string
string = input("Enter a lowercase string with alphabetic characters: ")
result = highest_consonant_value(string)
print(f"The highest value of consonant substrings is: {result}")
