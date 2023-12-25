import time
import multiprocessing
import matplotlib.pyplot as plt


def benchmark_task(max_duration):
    start_time = time.time()
    num_iterations = 0

    while time.time() - start_time < max_duration:
        # Simulate some simple task
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

def result_graph(single_core_val, multi_core_val):
    plt.subplot(1,2,1)    
    plt.plot(single_core_val,label='Single core values')
    plt.legend()
    
    plt.subplot(1,2,2)
    plt.plot(multi_core_val,label='Multi core values')
    plt.legend()
    
    plt.show()

def main():
    num_benchmarks = 20
    single_core_val = []
    multi_core_val = []
    single_core_mean = 0
    multi_core_mean = 0

    max_duration = 1.0  # Adjust the duration in seconds as needed
    num_processes = multiprocessing.cpu_count()

    for i in range(0,num_benchmarks):
        print(f"starting benchmark {i+1}...")
        single_core_result = single_core_benchmark(max_duration)
        multi_core_result = multi_core_benchmark(num_processes, max_duration)
        single_core_val.append(single_core_result/100)
        multi_core_val.append(multi_core_result/100)

    for j in range(0,num_benchmarks):
        single_core_mean += single_core_val[j]
        multi_core_mean += multi_core_val[j]
    
    print("Single-core benchmark result:", round(single_core_mean))
    print("Multi-core benchmark result:", round(multi_core_mean))
    
    result_graph(single_core_val, multi_core_val)

    
        
    
if __name__ == "__main__":
    main()