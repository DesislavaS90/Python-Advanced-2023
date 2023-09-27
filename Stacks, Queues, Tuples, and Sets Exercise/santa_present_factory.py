from collections import deque

materials = deque(int(x) for x in input().split())
magic_level = deque(int(x) for x in input().split())

presents = {}

operations = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

while materials and magic_level:
    material = materials.pop()
    current_level = magic_level.popleft()

    total_magic = material * current_level

    if total_magic in operations.keys():
        if operations[total_magic] not in presents.keys():
            presents[operations[total_magic]] = 1
            continue
        presents[operations[total_magic]] += 1
        continue

    if total_magic < 0:
        materials.append(material + current_level)
    elif total_magic > 0:
        materials.append(material + 15)
    elif total_magic == 0:
        if material != 0:
            materials.append(material)
        elif current_level != 0:
            magic_level.appendleft(current_level)

if 'Doll' in presents.keys() and 'Wooden train' in presents.keys() or \
     'Teddy bear' in presents.keys() and 'Bicycle' in presents.keys():
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if materials:
    materials = reversed(materials)
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for key, value in sorted(presents.items()):
    print(f'{key}: {value}')

