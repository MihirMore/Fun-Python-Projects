count = 0
total = 0.0

while True:
    sval = input("Please enter a number or finish: ")
    if sval == "finish":
        break
    try:
        fval = float(sval)
    except:
        print("Please enter a valid input.")
        continue

    count += 1
    total += fval
average = format(total/count, ".2f")
print(f"Total = {total}, numbers entered = {count} , average = {average}")


