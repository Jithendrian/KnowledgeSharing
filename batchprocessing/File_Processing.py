def count_vowels(input_string):
    count = 0
    for ch in input_string:
        if ch.lower() in ['a','e','i','o','u']:
            count += 1
    return count

def main():
    res = 0
    with open('bp_text.txt', 'r') as file:
        content = file.read()
        res += count_vowels(content)
    print("Number of Vowels", res)

    with open('bp_text.txt', 'r') as file:
        contents = file.readlines()

    res = 0
    for content in contents:
        res += count_vowels(content)
    print("Number of Vowels line_by_line", res)

if __name__ == "__main__":
    main()