print ('    ', end = '')
for i in range(-180, 181):
    print(i, end='  ')
print(' ')
print('  ')
# looping through valid coordinates range
for j in range (-90 , -87):

    for i in range(-182, 181):
        if i >= -180:
            #adds some padding for | | | rows
            if i == -180:
                print ('    ', end = '')
            #aligns | | | rows to longitude row
            if len(str(i)) == 4:
                print('  | ', end='  ')
            if len(str(i)) == 3:
                print(' | ', end='  ')
            if len(str(i)) == 2:
                print(' |', end='  ')
            if len(str(i)) == 1:
                print('|', end='  ')

        elif i == -182:
            #adds latitude column
            print(j , end =' ')
            print()

    print()




