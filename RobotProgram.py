def move(cmd: str) -> int:
    if cmd == "L":
        return -1
    
    return 1

def checkMinLength(pos: int, steps: int, cmds: str) -> int:
    counter = 0
    curr_cmd = 0
    for _ in range(steps):
        if pos == 0:
            counter += 1
            curr_cmd = 0

        if curr_cmd >= len(cmds):
            break

        pos += move(cmds[curr_cmd])
        curr_cmd += 1

    return counter if pos else counter + 1

if __name__ == "__main__":
    no_of_testcases = int(input())

    for _ in range(no_of_testcases):
        cmds_len, pos, steps = [int(num) for num in (input().strip()).split()]
        cmds = input()
        counter = checkMinLength(pos, steps, cmds)
        print(counter)