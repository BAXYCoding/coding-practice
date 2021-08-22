filein = input('Input an email log txt file please: ')
emaillog = open(filein)
days = dict()
for x in emaillog:
    if 'From ' in x:
        array = x.split()
        day = array[1]
        # day = day.split('@')
        # day = day[1]
        days[day] = days.get(day, 0)+1
    else:
        continue
new_list = list()
for k, v in days.items():
    tup = (v, k)
    new_list.append(tup)
    new_list = sorted(new_list, reverse=True)
print(new_list[0])
# # most = max(days, key=days.get)
# # print(most, days[most])
