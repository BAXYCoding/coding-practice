file = input('Please input a file: ')
ofile = open(file)
result_dict = dict()
result_list = list()


for x in ofile:
    file_list = x.split()  # splits every line in the file (gets rid of all spaces)
    for y in range(len(file_list)):  # iterates over every string in the resulting list of strings from file_list
        for z in file_list[y]:  # iterates over every letter in the string that y represents
            if z.isalpha() == True:  # checks to see if the character represented by z is part of the alphabet
                z = z.lower()  # If it is part of the alphabet, makes it lowercase
                result_dict[z] = result_dict.get(z, 0)+1  # idiom used to add things to a dictionary

for m, n in result_dict.items():  # .items() returns every key:value pairs
    tup_item = (n, m)  # reverse the key:value pairs
    result_list.append(tup_item)  # add the reversed key:value pairs to a list
    result_list = sorted(result_list, reverse=True)  # Sorts the new list in reverse order
print(result_list)
