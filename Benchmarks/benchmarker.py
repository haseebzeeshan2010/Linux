import time

def benchmark_task(max_duration):
    start_time = time.time()
    num_iterations = 0

    while time.time() - start_time < max_duration:
        # Simulate some simple task
        result = 2 + 2
        num_iterations += 1

    return num_iterations

def main():
    max_duration = 1.0  # Adjust the duration in seconds as needed
    result = benchmark_task(max_duration)

    print("Benchmark result:", result)

if __name__ == "__main__":
    main()
