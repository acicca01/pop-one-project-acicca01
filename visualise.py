map_dic = dict()
latitudes = []
longitudes = []
#load list in dictionary
for i in range(len(amap)):
    map_dic[(int(amap[i][2]),int(amap[i][3]))] = i
    latitudes.append(int(amap[i][2]))
    longitudes.append(int(amap[i][3]))
    # load latitude-longitude ranges into tuple
    lat_range = (min(latitudes),max(latitudes)+1)
    long_range = (min(longitudes),max(longitudes)+1)

print ('      ', end = '')
for i in range(*long_range):
    if len(str(i)) == 4:
        print(i, end='  ')
    elif len(str(i)) == 3:
        print(i, end='   ')
    elif len(str(i)) == 2:
        print(i, end='    ')
    elif len(str(i)) == 1:
        print(i, end='     ')
print()

# looping through valid coordinates range
for j in range (*lat_range):
    if len(str(j)) == 3:
        print('   ', end='')
    if len(str(j)) == 2:
        print('  ', end='')
    for i in range(*long_range):
        print('  ', ' ', sep='|', end='  ')
    print()
    for i in range(*long_range):
        if i == long_range[0]:
            print(j,end='   ')
        #print(f"{'-':^6}", end='')

        if (j , i) in map_dic:
            tmp = str(map_dic[(j,i)])
            if len(tmp) == 1:
                print('  ', ' ', sep=tmp, end='  ')
            if len(tmp) == 2:
                print(' ', ' ', sep=tmp, end='  ')
            if len(tmp) == 3:
                print('', ' ', sep=tmp, end='  ')
            if len(tmp) == 4:
                print('', '', sep=tmp, end='  ')
        else:
            print(f"{'-':^6}", end='')
    print()
















