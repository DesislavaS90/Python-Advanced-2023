numbers = [int(x) for x in input().split()]

negatives = 0
positives = 0

for x in numbers:
    if x > 0:
        positives += x
    else:
        negatives += x

print(negatives)
print(positives)

if positives > abs(negatives):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')