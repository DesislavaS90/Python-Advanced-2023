from collections import deque

textiles = deque([int(x) for x in input().split()])
medicament = deque([int(x) for x in input().split()])

result = {'MedKit': 0, 'Bandage': 0, 'Patch': 0}

while textiles:

    if not medicament:
        break

    current_textile = textiles.popleft()
    current_medication = medicament.pop()
    total = current_medication + current_textile

    if total == 100:
        result['MedKit'] += 1
    elif total == 40:
        result['Bandage'] += 1
    elif total == 30:
        result['Patch'] += 1

    elif total > 100:
        result['MedKit'] += 1
        my_num = medicament.pop()
        medicament.append(my_num + (total - 100))

    else:
        medicament.append(current_medication + 10)

if not textiles and not medicament:
    print('Textiles and medicaments are both empty.')

elif not textiles:
    print('Textiles are empty.')

elif not medicament:
    print('Medicaments are empty.')

if result:
    sorted_result = sorted(result.items(), key=lambda x: (-x[1], x[0]))
    for item, num in sorted_result:
        if num == 0:
            continue
        else:
            print(f'{item} - {num}')

if medicament:
    print(f"Medicaments left: {', '.join(map(str, sorted(medicament, reverse=True)))}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, sorted(textiles, reverse=True)))}")




