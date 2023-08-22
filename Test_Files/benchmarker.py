import time
import multiprocessing

def benchmark_task(max_duration):
    start_time = time.time()
    num_iterations = 0

    while time.time() - start_time < max_duration:
        # Simulate some simple task
        result = 2 + 2
        num_iterations += 1

    return num_iterations

def worker(max_duration, result_queue):
    result = benchmark_task(max_duration)
    result_queue.put(result)

def single_core_benchmark(max_duration):
    return benchmark_task(max_duration)

def multi_core_benchmark(num_processes, max_duration):
    result_queue = multiprocessing.Queue()
    processes = []

    for _ in range(num_processes):
        process = multiprocessing.Process(target=worker, args=(max_duration, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    total_result = 0
    while not result_queue.empty():
        total_result += result_queue.get()

    return total_result

def main():
    max_duration = 1.0  # Adjust the duration in seconds as needed
    num_processes = multiprocessing.cpu_count()

    single_core_result = single_core_benchmark(max_duration)
    multi_core_result = multi_core_benchmark(num_processes, max_duration)

    print("Single-core benchmark result:", single_core_result)
    print("Multi-core benchmark result:", multi_core_result)

if __name__ == "__main__":
    main()
