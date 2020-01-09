lst = [int(i) for i in open('DayFive.txt').read().rstrip().split(',')]
param, pointer, skip = {}, 0, (4,4,2,2,3,3,4,4)

while lst[pointer] != 99:
    opcode = lst[pointer] % 100
    for i in range(1,4):
        mode = lst[pointer]//int('100'.ljust(i+2, '0')) % 10
        param[str(i)] = pointer + i if mode else lst[pointer + i]
    if opcode == 1:
        lst[param['3']] = lst[param['1']] + lst[param['2']]
    if opcode == 2:
        lst[param['3']] = lst[param['1']] * lst[param['2']]
    if opcode == 3:
        lst[param['1']] = int(input('1 or 5?: '))
    if opcode == 4:
        print(lst[param['1']])
    if opcode == 5 and lst[param['1']]:
        pointer = lst[param['2']] - 3
    if opcode == 6 and not lst[param['1']]:
        pointer = lst[param['2']] - 3
    if opcode == 7:
        lst[param['3']] = 1 if lst[param['1']] < lst[param['2']] else 0
    if opcode == 8:
        lst[param['3']] = 1 if lst[param['1']] == lst[param['2']] else 0
    pointer += skip[opcode-1] 