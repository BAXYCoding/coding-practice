inputf = input('enter a file name:')
tfile = open(inputf)
try:
    for line in tfile:
        lineu = line.upper().rstrip()
        print(lineu)
except:
    print('error, there is no such file or incorrect syntax')
