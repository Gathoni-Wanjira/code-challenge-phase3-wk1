
def get_consonant_value(char):
    return ord(char) - ord('a') + 1

def highest_consonant_value(s):
    consonant_values = []
    current_value = 0

    for char in s:
        if char in "aeiou":
            consonant_values.append(current_value)
            current_value = 0
        else:
            current_value += get_consonant_value(char)

    consonant_values.append(current_value)
    return max(consonant_values)

# Taking user input for the string
string = input("Enter a lowercase string with alphabetic characters: ")
result = highest_consonant_value(string)
print(f"The highest value of consonant substrings is: {result}")
