for i in range(-180, 181):
    print(i, end='  ')
print()

# looping through valid coordinates range
for j in range (-92 , 91):
        for i in range(-182, 181):
            if i >= -180:
                if len(str(i)) == 4:
                    print('  | ', end='  ')
                if len(str(i)) == 3:
                    print(' | ', end='  ')
                if len(str(i)) == 2:
                    print(' |', end='  ')
                if len(str(i)) == 1:
                    print('|', end='  ')
            elif i == -182:
                print(j)
        print()
        



