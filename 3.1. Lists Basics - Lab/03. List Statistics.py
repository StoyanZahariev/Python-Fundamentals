num = int(input())
positives = []
negatives = []

for n in range(num):
    current_number = int(input())
    if current_number >= 0:
        positives.append(current_number)
    else:
        negatives.append(current_number)
print(positives)
print(negatives)
print(f'Count of positives: {len(positives)}\nSum of negatives: {sum(negatives)}')
