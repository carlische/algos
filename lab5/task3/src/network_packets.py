from utils import read, write


def network_packets(s, n, packets):
    if n == 0:
        return None
    deque = []
    result = []
    head = 0
    buffer_time = packets[0][0]
    for p in packets:
        start_time, p_i = p
        head = max([head] + [index for index in range(len(deque)) if deque[index] <= start_time])
        if len(deque[head+1:]) < s:
            result += [max(buffer_time, start_time)]
            buffer_time += p_i
            deque.append(buffer_time)
        else:
            result += [-1]
    return result


def main():
    data = [tuple(line) for line in read(type_convert=int)]
    s, n = data[0]
    packets = data[1:]
    write(end='')
    result = network_packets(s, n, packets)
    for res in result:
        write(res, to_end=True)


if __name__ == '__main__':
    main()
