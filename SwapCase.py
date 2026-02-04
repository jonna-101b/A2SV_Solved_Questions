def swap_case(s):
    newStr = ""
    for char in s:
        newStr += char.lower() if char.isupper() else char.upper()
        
    return newStr

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)