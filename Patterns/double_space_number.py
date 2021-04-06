current_number = 1
stop = 2
rows = 3

for i in range(rows):
    for j in range(1, stop):
        print(current_number , end=" ")
        current_number += 1
    print()
    stop += 2    