scores = {"Alice": 85, "Bob": 92, "Charlie": 85, "David": 93}

max_score = max(scores.values())

print(max_score)

top_scores = [name for name, score in scores.items() if score == max_score]

print(top_scores)