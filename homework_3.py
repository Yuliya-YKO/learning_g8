somephrase = "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"
print(somephrase)

# task #1
print(len(somephrase))

# task #2
print(len(somephrase.split(' ')))

# task #3

smstr = somephrase.split(' ')
print(smstr)

# task #4

recoveredList = []
for i in smstr:
    recoveredList.append(
        i.replace('е', str('&')).replace('і', str('&')).replace('и', str('&')).replace('о', str('&')).replace('у', str('&')).replace('я', str('&')).replace('є', str('&')).replace('а', str('&')))

print(recoveredList)

delimiter = ' '
my_string = delimiter.join(recoveredList)
print(my_string)