from utils import read, write
import heapq


def scheduler(n, tasks):
    threads = [(0, i) for i in range(n)]
    results = []
    for task in tasks:
        end_time, thread_index = heapq.heappop(threads)
        start_time = end_time
        results.append((thread_index, start_time))
        new_end_time = start_time + task
        heapq.heappush(threads, (new_end_time, thread_index))
    return results


def main():
    write(end='')
    data = [list(line) for line in read(type_convert=int)]
    n, m = data[0]
    tasks = data[1]
    result = scheduler(n, tasks)
    for line in result:
        write(*line, to_end=True)


if __name__ == '__main__':
    main()
