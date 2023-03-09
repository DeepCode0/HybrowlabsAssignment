def is_anagram(str1, str2):
    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Remove all spaces from both strings
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    # Check if the length of both strings are the same
    if len(str1) != len(str2):
        return False

    # Create a dictionary to store the frequency of characters in str1
    freq = {}
    for char in str1:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Check if each character in str2 is present in the dictionary and has the same frequency
    for char in str2:
        if char not in freq:
            return False
        else:
            freq[char] -= 1
            if freq[char] < 0:
                return False

    # Check if all characters in str1 have been used
    for value in freq.values():
        if value != 0:
            return False

    # If all conditions are met, then the strings are anagrams
    return True
