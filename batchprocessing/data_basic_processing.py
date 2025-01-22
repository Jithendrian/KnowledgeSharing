def batch_process(data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]

def process_batch(batch):
    return sum(batch)

def combine_all_batches(batch_sums):
    return sum(batch_sums)

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
batch_size = 5

batch_sums = []
for batch in batch_process(data, batch_size):
    result = process_batch(batch)
    print(f"Batch {batch}: Result = {result}")
    batch_sums.append(result)

overall_result = combine_all_batches(batch_sums)
print(f"Overall Result {overall_result}")