# data = open('files.txt')
# for i in data:
#     print(data.read())

with open('files2.txt', 'w') as file:
    data = ['at', 'ahf', 'skfkf']
    for s in data:
        file.write(s + '\n')