def computepay(hours , rate ):
    if hours > 40.0:    
        overtimePay = (hours * rate ) + (hours - 40.0) * (rate * 0.5)
        pay = overtimePay
    else:
        regularpay = hours * rate
        pay = regularpay
    return pay

hoursWorked = input("Please enter the number of hours worked: ")
hourlyRate = input("Please enter the rate/hr: ")
fh = float(hoursWorked)
fr = float(hourlyRate)
xp = computepay(fh , fr)

print("Your Pay is: ",xp)
