import random
import time
from SortingAlgorithms import sorting_algorithms, sorting_names
import asyncio
import matplotlib.pyplot as plt
from AlgorithmInfo import AlgorithmExecutionInfo


def generate_random_arrays(list_with_sizes):
    arrays = []
    for size in list_with_sizes:
        arrays.append([random.randint(0, 1000) for _ in range(size)])
    return arrays


def create_graphic(graph_name, algorithms, sizes):
    plt.clf()
    for algorithm in algorithms:
        plt.plot(sizes[:len(algorithm.execution_times)], algorithm.execution_times, label=algorithm.name)
        plt.legend()
    plt.xlabel('Elements')  # Название оси X
    plt.ylabel('Times')  # Название оси Y
    plt.title('Complexity of sorting algorithm')  # Заголовок графика
    plt.grid(True)  # Включите сетку
    plt.savefig(graph_name + '.png')


def create_combined_graphic(graph_name, algorithms1, algorithms2, sizes):
    plt.clf()
    fig, axs = plt.subplots(2, 1, figsize=(10, 15))

    for algorithm in algorithms1:
        axs[0].plot(sizes[:len(algorithm.execution_times)], algorithm.execution_times, label=algorithm.name)
    axs[0].legend()
    axs[0].set_xlabel('Elements')
    axs[0].set_ylabel('Times')
    axs[0].set_title('First Three Sorting Algorithms')
    axs[0].grid(True)

    for algorithm in algorithms2:
        axs[1].plot(sizes[:len(algorithm.execution_times)], algorithm.execution_times, label=algorithm.name)
    axs[1].legend()
    axs[1].set_xlabel('Elements')
    axs[1].set_ylabel('Times')
    axs[1].set_title('Second Three Sorting Algorithms')
    axs[1].grid(True)

    plt.tight_layout()
    plt.savefig(graph_name + '.png')


async def code_to_test():
    sizes1 = [100, 1000, 3000, 5000, 7000, 10000]
    sizes2 = [100, 1000, 3000, 5000, 7000, 10000]
    algorithms = []
    tasks = []
    arrays1 = generate_random_arrays(sizes1)
    arrays2 = generate_random_arrays(sizes2)

    for sorting_algorithm, sorting_name in zip(sorting_algorithms[:3], sorting_names[:3]):
        algorithms.append(AlgorithmExecutionInfo(sorting_algorithm, arrays2.copy(), sorting_name))

    for sorting_algorithm, sorting_name in zip(sorting_algorithms[3:], sorting_names[3:]):
        algorithms.append(AlgorithmExecutionInfo(sorting_algorithm, arrays2.copy(), sorting_name))

    for algorithm in algorithms:
        tasks.append(algorithm.get_execution_times(1))

    await asyncio.gather(*tasks)

    create_graphic("algorithms", algorithms, sizes2)
    create_graphic("first_three", algorithms[:3], sizes2)
    create_graphic("second_three", algorithms[3:], sizes2)
    create_combined_graphic("combined", algorithms[:3], algorithms[3:], sizes2)


async def main():
    start_time = time.time()
    await code_to_test()
    end_time = time.time()
    print("Execution time:", end_time - start_time)


asyncio.run(main())
