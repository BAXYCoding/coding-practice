def add_time(start, duration, start_day=''):
    days = 0
    real_duration = 0
    days_of_week = [
        'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday',
        'saturday'
    ]
    hours_in_day = [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,
        20, 21, 22, 23, 24
    ]
    start_hours = 0
    start_minutes = 0
    new_time = 0
    end_day = ''
    start_day = start_day.lower()
    final_am_pm = None
    n_days_later = '({} days later)'
    final_hour = 0
    final_time = '{}:{}'
    final_minutes = 0
    loop_count_hours = 0

    def day_finder(day_counter):
        nonlocal end_day
        nonlocal days
        day_counter = int(days)
        start_day_index = days_of_week.index(start_day)
        for g in days_of_week[start_day_index:]:
            if day_counter > 0:
                day_counter -= 1
            elif day_counter == 0:
                end_day = g
                break
        if end_day == '':
            while day_counter >= 0:
                for y in range(len(days_of_week)):
                    if day_counter > 0:
                        day_counter -= 1
                    elif day_counter == 0:
                        end_day = days_of_week[y]
                        day_counter -= 1
                        break
                    else:
                        break

    def hour_finder(hour_counter):
        nonlocal loop_count_hours
        nonlocal final_am_pm
        nonlocal final_hour
        nonlocal hours_counter
        nonlocal days
        hour_counter = hours_counter
        start_hour_index = hours_in_day.index(int(start_hours))
        for j in hours_in_day[start_hour_index:]:
            if hour_counter > 0:
                hour_counter -= 1
                if hour_counter == 0:
                    end_hour = hours_in_day[j]+1
                    final_hour = end_hour
                    if final_hour > 24:
                        final_am_pm = 'AM'
            elif hour_counter == 0:
                end_hour = hours_in_day[j]
                if end_hour > 12:
                    final_am_pm = 'PM'
                    final_hour = end_hour
                    break
                else:
                    final_hour = end_hour
                    final_am_pm = 'AM'
                    break
                break
            if j == hours_in_day[-1]:
                loop_count_hours += 1
                days += 1

        if hour_counter > 0:
            for z in range(len(hours_in_day)):
                if hour_counter > 0:
                    hour_counter -= 1
                elif hour_counter == 0:
                    end_hour = hours_in_day[z]+1
                    if end_hour > 12:
                        final_am_pm = 'PM'
                        final_hour = end_hour
                        break
                    else:
                        final_am_pm = 'AM'
                        final_hour = end_hour
                        break
                else:
                    break
                if z == hours_in_day[-1]:
                    loop_count_hours += 1

    split_first = start.split(':')
    start_hours = split_first[0]
    split_second = split_first[1].split()
    start_minutes = int(split_second[0])
    if split_second[1] == 'PM':
        start_hours = int(start_hours)+12
    split_d = duration.split(':')
    split_d_hours = int(split_d[0])
    split_d_minutes = int(split_d[1])
    if split_d_hours > len(range(24)):
        days = int(split_d_hours // 24)
        extra_hours = int(split_d_hours % 24)
        real_duration = extra_hours
    else:
        real_duration = int(split_d_hours)

    hours_counter = int(real_duration)
    days_counter = int(days)

    total_minutes = start_minutes + split_d_minutes
    hour_finder(hours_counter)

    if total_minutes > 60:
        final_minutes = total_minutes - 60
        int(final_hour)
        final_hour += 1
        if final_hour >= 12:
            final_am_pm = 'PM'
        if final_hour == 24:
            final_am_pm = 'AM'
            days += 1
        if final_hour > 12:
            final_hour -= 12
            if final_hour > 12:
                final_hour -= 12
    else:
        final_minutes = total_minutes
        if final_hour == 0:
            final_hour = 12
        if final_hour > 12:
            final_hour -= 12
            if final_hour > 12:
                final_hour -= 12
    if final_minutes <= len(range(9)):
        final_time = '{}:0{}'

    if start_day != '':
        day_finder(days_counter)
        new_time = str(final_time.format(final_hour, final_minutes)) + ' ' + str(final_am_pm) + ',' + ' ' + end_day.capitalize() + ' ' + n_days_later.format(
            days)
        if days == 1 and loop_count_hours == 1:
            new_time = str(final_time.format(final_hour, final_minutes)) + ' ' + \
                str(final_am_pm) + ',' + ' ' + end_day.capitalize() + ' ' + '(next day)'
        elif days == 0 and loop_count_hours == 0:
            new_time = new_time = str(final_time.format(final_hour, final_minutes)) + \
                ' ' + str(final_am_pm) + ',' + ' ' + end_day.capitalize()
    elif start_day == '':
        if days < 1:
            new_time = str(final_time.format(final_hour, final_minutes)) + ' ' + str(final_am_pm)
        elif days > 1:
            new_time = str(final_time.format(final_hour, final_minutes)) + ' ' + str(final_am_pm) + ' ' + n_days_later.format(
                days)
        if days == 1:
            new_time = str(final_time.format(final_hour, final_minutes)) + \
                ' ' + str(final_am_pm) + ' ' + '(next day)'
    return new_time
