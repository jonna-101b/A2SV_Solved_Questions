def solve():
    s1 = input()
    s2 = input()
    
    target_pos = s1.count('+') - s1.count('-')
    current_pos = s2.count('+') - s2.count('-')
    unknown_count = s2.count('?')
    diff = target_pos - current_pos
    if abs(diff) > unknown_count or (diff + unknown_count) % 2 != 0:
        print(f"{0.0:.12f}")
        return

    import math
    ways = math.comb(unknown_count, (unknown_count + diff) // 2)
    total_possibilities = 2**unknown_count
    probability = ways / total_possibilities
    
    print(f"{probability:.12f}")

solve()
