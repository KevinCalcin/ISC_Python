hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter rate:")
r = float(rate)

if h > 40:
    bruto =  40 * float(rate)
    extra = ((h-40) * 1.5) * r
    end = bruto + extra
else:
    end = h * r
print(end);
