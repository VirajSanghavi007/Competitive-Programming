sold = (str(input())).lower()
snew = ''

for i in sold:
    if(i in 'aieouy'):
        continue
    else:
        snew += ('.' + i)

print(snew)