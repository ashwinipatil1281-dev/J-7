import sys

if len(sys.argv) < 2:
    print("Usage: python main.py score1 score2 ... scoreN")
    sys.exit(1)

scores = [float(s) for s in sys.argv[1:]]

print("Sum:", sum(scores))
print("Average:", sum(scores) / len(scores))
print("Maximum:", max(scores))
print("Minimum:", min(scores))