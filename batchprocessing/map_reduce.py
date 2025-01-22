from collections import defaultdict
from File_Processing import count_vowels

def read_file_in_chunks(file_path, lines_per_chunk=1000):
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
    vowel_count = 0
    for line in lines:
        vowel_count += count_vowels(line)
    return [('vowel', vowel_count)]

def shuffle_phase(mapped_data):
    shuffled = defaultdict(list)
    for key, value in mapped_data:
        shuffled[key].append(value)
    return shuffled

def reduce_phase(shuffled_data):
    reduced = {}
    for key, values in shuffled_data.items():
        reduced[key] = sum(values)
    return reduced


# Main Function
def count_vowels_in_file(file_path, lines_per_chunk=1000):
    all_mapped_data = []

    # Chunk the file and process each chunk
    for chunk in read_file_in_chunks(file_path, lines_per_chunk):
        mapped_data = map_phase(chunk)  # Map
        all_mapped_data.extend(mapped_data)
    print(all_mapped_data)
    # Shuffle Phase
    shuffled_data = shuffle_phase(all_mapped_data)

    # Reduce Phase
    reduced_data = reduce_phase(shuffled_data)

    return reduced_data


# Example Usage
if __name__ == "__main__":
    file_path = "bp_text.txt"  # Replace with your file path
    result = count_vowels_in_file(file_path)
    print(f"Total Vowels in the File: {result['vowel']}")
