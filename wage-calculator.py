def payment_computation(r, hours):
    if myhours > 40:
        return (hours-40)*(1.5*r) + r*40
    return r*hours

r = input('Please enter hourly rate')
hours = input('Please enter number of hours')