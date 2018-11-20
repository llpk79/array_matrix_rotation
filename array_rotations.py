from random import randint
from collections import deque
from timeit import default_timer as timer

a = [x for x in range(50000)]
rotations = 20000
b = deque(a)


def pop_rot_left(array, rots):
    for _ in range(rots):
        num = array.pop(0)
        array.append(num)
    return array


def deque_rot_left(que, rots):
    for _ in range(rots):
        num = que.popleft()
        que.append(num)
    return que


def slice_rot_left(array, rots):
    return array[:rots] + array[rots:]


def modulo_rot_left(array, rots):
    array_len = len(array)
    new_array = [None] * array_len
    for i in range(array_len):
        new_array[i] = (i + rots) % array_len
    return new_array


times = {}


then = timer()
print(pop_rot_left(a, rotations))
now = timer()
pops = now - then
times[pops] = 'pops'
print('pops', pops)

then = timer()
print(deque_rot_left(b, rotations))
now = timer()
deq = now - then
times[deq] = 'deq'
print('deq', deq)

then = timer()
print(slice_rot_left(a, rotations))
now = timer()
slices = now - then
times[slices] = 'slices'
print('slices', slices)

then = timer()
print(modulo_rot_left(a, rotations))
now = timer()
mod = now - then
times[mod] = 'mod'
print('mod', mod)


times = list(sorted(times.items()))
print(times)
print(f'{times[0][1]} is {times[1][0]/times[0][0]} x faster than {times[1][1]} is {times[2][0]/times[1][0]} x'
      f'faster than {times[2][1]} is {times[3][0]/times[2][0]} x faster than {times[3][1]}')

