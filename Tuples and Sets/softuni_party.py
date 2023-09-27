number_of_reservations = int(input())
reservation_number = {input() for i in range(number_of_reservations)}

while True:
    command = input()

    if command == 'END':
        break

    if command in reservation_number:
        reservation_number.remove(command)

print(len(reservation_number))

for guest in sorted(reservation_number):
    print(guest)