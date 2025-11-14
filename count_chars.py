statement = input("")

counts = {}
for char in statement:
    if char == " ":
        continue
    if char not in counts:
        counts[char] = 0
    counts[char] += 1

print(f" {counts}")
