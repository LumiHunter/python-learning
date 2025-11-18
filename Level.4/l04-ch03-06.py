"""
Section 3
Concurrency, CPU Bound vs I/O bound - CPU bound(1) - Synchronous
Keyword - CPU Bound
"""

# CPU-bound 예제

import time

def cpu_bound(number):
    return sum(i * i for i in range(number))

def find_sums(numbers):
    result = []
    for number in numbers:
        result.append(cpu_bound(number))
    return result

def main():
    numbers = [3_000_000 + x for x in range(30)]
    
    start_time = time.time()
    total = find_sums(numbers)

    print()
    print(f'Total list: {total}')
    print(f'Sum: {sum(total)}')

    duration = time.time() - start_time
    print()
    print(f'Duration: {duration} seconds')

if __name__ == "__main__":
    main()