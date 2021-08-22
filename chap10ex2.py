filein = input('Input an email log txt file please: ')
emaillog = open(filein)
days = dict()
for x in emaillog:
    if 'From ' in x:
        array = x.split()
        day = array[5]
        day = day.split(':')
        day = day[0]
        days[day] = days.get(day, 0)+1
    else:
        continue
new_list = list()
for k, v in days.items():
    tup = (k, v)
    new_list.append(tup)
    new_list = sorted(new_list)
for m, n in new_list:
    print(m, n)
# # most = max(days, key=days.get)
# # print(most, days[most])
