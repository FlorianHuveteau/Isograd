import itertools

strand_length = 0 # Length of each strand == sum of the length of each fragment // 2
lines = []
n = int(input())
for _ in range(n):
    line = input()
    lines.append(line)
    strand_length += len(line)

strand_length //= 2
formatter = lambda a,b : "{}#{}".format(" ".join(a), " ".join(b))
trans = str.maketrans("ATCG", "TAGC")
result = None

for fragments in itertools.permutations(lines):
    a = "".join(fragments)[:strand_length]
    b = "".join(fragments)[strand_length:]
    if a.translate(trans) == b:
        l = 0
        for i, fragment in enumerate(fragments):
            l += len(fragment)
            if l == strand_length:
                result = formatter(fragments[:i + 1], fragments[i + 1:])
                break
    if result:
        break
print(result)