def payment_computation(r, hours):
    if hours > 40:
        return (hours-40)*(1.5*r) + r*40
    return r*hours

indicator = 0
while indicator == 0:
    try:
        r = eval(input('Please enter hourly rate.'))
        hours = eval(input('Please enter number of hours.'))
        result = payment_computation(r,hours)
        print(result)
        indicator = 1
    except:
        print('Please enter a number next time.')

print('We are done.')