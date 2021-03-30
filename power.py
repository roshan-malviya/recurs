def p(b,po):
    if po==1:
        return(b)
    return(p(b,po-1)*b)

base=int(input('enter base'))
power=int(input('enter power '))

print (p(base,power))