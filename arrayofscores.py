import sys

scores = list(map(int, sys.argv[1:]))

total = sum(scores)
average = total / len(scores)
maximum = max(scores)
minimum = min(scores)

print("scores:", scores)
print("sum:", total)
print("average:", average)
print("Maximum", maximun)
print("Minimum", minimum)