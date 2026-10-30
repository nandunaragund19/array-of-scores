import sys

scores = list(map(int, sys.argv[:]))

total = sum(scores)
average = total / len(scores)

print("scores:", scores)
print("sum:", total)
print("average:", average)