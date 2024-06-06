import asyncio
import time


def timing_decorator(func):
    async def wrapper(*args, **kwargs):
        start_time = time.time()
        result = await func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        return execution_time
    return wrapper


def split_list(lst, n):
    return [lst[i:i + n] for i in range(0, len(lst), n)]


class AlgorithmExecutionInfo:

    xlabel = 'Element'
    ylabel = 'Execution time'

    def __init__(self, async_sorting_algorithm, arrays, algorithm_name):
        self.name = algorithm_name
        self.__async_sorting_algorithm = timing_decorator(async_sorting_algorithm)
        self.__arrays = arrays
        self.execution_times = []

    async def get_execution_times(self, number_of_tests):
        tasks = []
        for array in self.__arrays:
            for _ in range(number_of_tests):
                tasks.append(self.__async_sorting_algorithm(array.copy()))

        all_execution_times = await asyncio.gather(*tasks)

        for times, array in zip(split_list(all_execution_times, number_of_tests), self.__arrays):
            self.execution_times.append(sum(times) / len(times))
