days = 10
file_list = ['l', 'b', 'c', 'd', 'f', 't', 'd']
for y in range(len(file_list)):
    if days >= 0:
        days -= 1
        print(days)
        if days == 0:
            print([y])
