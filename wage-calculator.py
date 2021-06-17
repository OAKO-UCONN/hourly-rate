def payment_computation(r, hours):
    if hours > 40:
        return (hours-40)*(1.5*r) + r*40
    return r*hours

r = eval(input('Please enter hourly rate'))
hours = eval(input('Please enter number of hours'))
result = payment_computation(r,hours)
print(result)