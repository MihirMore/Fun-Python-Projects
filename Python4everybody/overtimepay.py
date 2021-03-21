hoursWorked = float(input("Enter hours: "))
ratePerHr = float(input("Enter rate/hr: "))
regularPay = hoursWorked * ratePerHr
if hoursWorked > 40.0:    
    overtimePay = regularPay + (hoursWorked - 40.0) * (ratePerHr * 0.5)
    print("Your pay is: ",overtimePay)
else:    
    print(regularPay)
        