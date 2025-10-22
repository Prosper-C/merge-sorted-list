
import sys
import heapq
from typing import List, Iterator

def parse_line_of_ints(line: str) -> List[int]:
    line = line.strip()
    if not line:
        return []
    return [int(x) for x in line.split()]

def merge_k_sorted_iterables(iterables: List[Iterator[int]]) -> Iterator[int]:

    heap = []

    iters = [iter(it) for it in iterables]
    for i, it in enumerate(iters):
        try:
            first = next(it)
            heap.append((first, i))
        except StopIteration:
            pass
    heapq.heapify(heap)

    while heap:
        val, idx = heapq.heappop(heap)
        yield val
        try:
            nxt = next(iters[idx])
            heapq.heappush(heap, (nxt, idx))
        except StopIteration:
            pass

def read_input_file(filename: str) -> List[List[int]]:
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        first_line = f.readline()
        if not first_line:
            return []
        try:
            n = int(first_line.strip())
        except ValueError:
            raise ValueError("First line must contain integer N (number of lines).")
        for _ in range(n):
            line = f.readline()
            if line is None:
                line = ''
            lines.append(parse_line_of_ints(line if line is not None else ''))
    return lines

def write_output_file(filename: str, numbers: Iterator[int]) -> None:
    with open(filename, 'w', encoding='utf-8') as f:

        first = True
        for num in numbers:
            if first:
                f.write(str(num))
                first = False
            else:
                f.write(' ')
                f.write(str(num))
        f.write('\n')

def main(argv):
    in_fname = 'input.txt'
    out_fname = 'output.txt'
    if len(argv) >= 2:
        in_fname = argv[1]
    if len(argv) >= 3:
        out_fname = argv[2]

    lists = read_input_file(in_fname)
    merged_iter = merge_k_sorted_iterables(lists)
    write_output_file(out_fname, merged_iter)

if __name__ == "__main__":
    main(sys.argv)
