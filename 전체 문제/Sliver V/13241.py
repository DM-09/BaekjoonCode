def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

A, B = map(int, input().split())
print(lcm(A, B))
