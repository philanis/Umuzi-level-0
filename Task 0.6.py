def max_number(a,b,c):
    if a > b and a > c:
        largest = a
    elif b > a and b > c:
        largest = b
    else:
        largest = c
    return(largest)
max_number(12,10,7)