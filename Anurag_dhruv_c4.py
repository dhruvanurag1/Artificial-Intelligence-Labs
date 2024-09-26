def solve(a, b):
    x, y, n, tracked = a, b, 1, []
    while pow(a ** 2 + b ** 2, 0.5) < 4:
        if (round(pow(a, 2) - pow(b, 2) + x, 2), round(2 * a * b + y, 2)) in tracked: return len(tracked) - tracked.index((round(pow(a, 2) - pow(b, 2) + x, 2), round(2 * a * b + y, 2)))
        tracked, n, a, b = tracked + [(a,b)], n+1, round(pow(a, 2) - pow(b, 2) + x, 2), round(2 * a * b + y, 2)
    return "ESCAPES " + str(n)
for b, a in enumerate(open('test.txt', 'r').read().splitlines()): print(str(b+1) + '.', solve(float(a.split()[0]), float(a.split()[1])))
