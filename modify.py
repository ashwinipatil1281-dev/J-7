import sys

default_scores = [75, 88, 92, 67, 81]

if len(sys.argv) > 1:
    scores = [float(s) for s in sys.argv[1:]]
    source = "User Input"
else:
    scores = default_scores
    source = "Self-assigned"

print(f"Scores: {scores} ({source})")
print("Sum:", sum(scores))
print("Average:", sum(scores) / len(scores))
print("Maximum:", max(scores))
print("Minimum:", min(scores))
