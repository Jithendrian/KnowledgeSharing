from File_Processing import count_vowels
def process_chunk(chunk):
    vowel_chunk_count = 0
    for line in chunk:
        vowel_chunk_count += count_vowels(line)
    return vowel_chunk_count

def batch_process_file(filename, chunk_size):
    with open(filename, 'r') as file:
        chunk = []
        for line in file:
            chunk.append(line)
            if len(chunk) >= chunk_size:
                yield chunk
                chunk = []  # Reset chunk for the next batch
        if chunk:  # Process remaining lines
            yield chunk

result = 0
file_name = 'bp_text.txt'
batch_size = 1000
batch_number = 0
for chunk in batch_process_file(file_name, batch_size):
    batch_number += 1
    local_result = process_chunk(chunk)
    print(f"Batch Number {batch_number}, Batch Results : {local_result}")
    result += local_result
print(f"Processed chunk: Result = {result}")
