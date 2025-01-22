from File_Processing import count_vowels
import concurrent.futures
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
                chunk = []
        if chunk:
            yield chunk

result = 0
file_name = 'bp_text.txt'
batch_size = 1000
batch_number = 0
chunk_results = []
total_vowels = 0
for chunk in batch_process_file(file_name, batch_size):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        chunk_results.append(executor.submit(process_chunk, chunk))
        results_list = []
        for chunk_result in concurrent.futures.as_completed(chunk_results):
            results_list.append(chunk_result.result())
total_vowels = sum(results_list)
print(f"Total Vowels =  {total_vowels}")