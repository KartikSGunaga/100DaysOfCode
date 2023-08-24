def powerOf(base, exp):
    if(exp == 0):
        return 1

    return (base * (powerOf(base, exp - 1)))


base = int(input('Enter the base: '))
exp = int(input('Enter the exponent: '))

print(f"{base} raised to {exp} is: {powerOf(base, exp)}.")