clothes = [int(x) for x in input().split()]
capacity_of_rack = int(input())

counter_rack = 1
sum_clothes = 0

while clothes:

    if clothes[-1] + sum_clothes <= capacity_of_rack:
        sum_clothes += clothes.pop()

    else:
        counter_rack += 1
        sum_clothes = 0

print(counter_rack)
