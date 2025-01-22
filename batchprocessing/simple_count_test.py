def count_vowels(input_string):
    count = 0
    for ch in input_string:
        if ch.lower() in ['a','e','i','o','u']:
            count += 1
    return count

print(count_vowels("India"))
print(count_vowels("india"))