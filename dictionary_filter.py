# Dictionary of student names and their scores
scores = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}

# Define the threshold value
threshold = int(input("Enter the threshold score: "))

# Filter the dictionary based on the threshold
filtered_scores = {name: score for name, score in scores.items() if score > threshold}

print(filtered_scores)
