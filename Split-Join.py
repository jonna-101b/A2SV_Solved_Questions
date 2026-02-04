def split_and_join(line):
    line = list(line)
    replaced = []
    for char in line:
        if char == " ":
            replaced.append("-")
            continue
            
        replaced.append(char)
        
    return "".join(replaced)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)