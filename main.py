def calculate_statistics(line):
    vowels = 0
    consonants = 0

    for character in line:
        if character.isalpha():
            if character.lower() in ['a', 'e', 'i', 'o', 'u']:
                vowels += 1
            else:
                consonants += 1

    return vowels, consonants


line_count = int(input("How many lines? "))
lines = []

for _ in range(line_count):
    line = input()
    lines.append(line)

total_vowels = 0
total_consonants = 0

for line in lines:
    vowels, consonants = calculate_statistics(line)
    total_vowels += vowels
    total_consonants += consonants

print("Number of vowels:", total_vowels)
print("Number of consonants:", total_consonants)

if __name__ == '__main__':
    calculate_statistics('PyCharm')


