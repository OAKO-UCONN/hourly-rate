def payment_computation(r, hours):
    if myhours > 40:
        (1.5*r)*(hours-40)
    return r*hours

myrate = 20
myhours = 25
result = payment_computation(myrate,myhours)
print(result)
