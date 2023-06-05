from collections import Counter

wordList = input("Enter a list of words: ").split()

Occurrences = Counter(wordList)

print("Occurrences:")
for word, count in Occurrences.items():
    print(f"{word}: {count}")