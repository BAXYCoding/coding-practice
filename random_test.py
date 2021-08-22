days = 10
file_list = ['l', 'b', 'c', 'd', 'f', 't', 'd']
while days >= 0:
    for y in range(len(file_list)):
        if days >= 0:
            days -= 1
            print(days)
            if days == 0:
                print([y])


def add_time(start, duration, start_day=''):
    am_pm = ''
    start_time = ''
    days = ''
    real_duration = ''
    for q in start:

        split_start = str(q.split(':')).split()
        start_time = float(split_start[0])+float(split_start[1])/60
        am_pm = split_start[2].lower()
        if am_pm == pm:
            start_time = start_time + float('12')
    for w in duration:
        split_duration = w.split(':', ' ')
        if split_duration[0] > len(range(24)):
            days = float(split_duration[0]//24)
            duration_hours = float(split_duration[0] % 24) + float(split_duration[1])
            real_duration = days + duration_hours
        else:
            real_duration = float(split_duration[0])+float((split_duration[1]/60))

    if start_day != '':
        new_time = 0
    return new_time
