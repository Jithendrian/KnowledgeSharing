from collections import defaultdict
def read_file_in_chunks(file_path, lines_per_chunk=1000):
    """Yield chunks of lines from the file."""
    with open(file_path, 'r') as file:
        chunk = []
        for i, line in enumerate(file):
            chunk.append(line.strip())
            if (i + 1) % lines_per_chunk == 0:
                yield chunk
                chunk = []
        if chunk:  # Yield the last chunk if it's not empty
            yield chunk


def map_phase(lines):
    """Emit key-value pairs for each vowel."""
    vowels = "aeiouAEIOU"
    mapped = defaultdict(int)
    for line in lines:
        for char in line:
            if char in vowels:
                mapped[char] += 1
    print(mapped)
    return mapped


# 3. Shuffle Phase
def shuffle_phase(all_mapped_data):
    shuffled_data = defaultdict(list)
    for mapped_data in all_mapped_data:
        for key, value in mapped_data.items():
            shuffled_data[key].append(mapped_data[key])
    return shuffled_data


# 4. Reduce Phase
def reduce_phase(shuffled_data):
    """Aggregate the counts and compute the total."""
    reduced = {}
    total_vowels = 0
    for key, values in shuffled_data.items():
        count = sum(values)  # Sum counts for each key
        reduced[key] = count
        total_vowels += count  # Add to total
    reduced['total'] = total_vowels  # Add total vowels count as a key
    return reduced


# Main Function
def count_vowels_with_multiple_keys(file_path, lines_per_chunk=1000):
    all_mapped_data = []
    for chunk in read_file_in_chunks(file_path, lines_per_chunk):
        mapped_data = map_phase(chunk)
        all_mapped_data.append(mapped_data)
    print(all_mapped_data)

    shuffled_data = shuffle_phase(all_mapped_data)
    print(shuffled_data)
    # Reduce Phase
    reduced_data = reduce_phase(shuffled_data)

    return reduced_data


# Example Usage
if __name__ == "__main__":
    file_path = "bp_text.txt"  # Replace with your file path
    result = count_vowels_with_multiple_keys(file_path)
    print("Vowel Counts with Total:", result)
