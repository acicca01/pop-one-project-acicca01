#load latitude-longitude ranges into tuple
d = dict()
latitudes = []
longitudes = []
#load list in dictionary
for i in range(len(amap)):
    d[(int(amap[i][2]),int(amap[i][3]))] = i
    latitudes.append(int(amap[i][2]))
    longitudes.append(int(amap[i][3]))
    lat_range = (min(latitudes),max(latitudes)+1)
    long_range = (min(longitudes),max(longitudes)+1)

print ('      ', end = '')
for i in range(*long_range):
    print(i, end='  ')
print()

# looping through valid coordinates range
for j in range (*lat_range):
    print('   ', end='')
    for i in range(*long_range):
        print('  ', ' ', sep='|', end='  ')
    print()
    for i in range(*long_range):
        if i == long_range[0]:
            print(j,end='   ')
        #print(f"{'-':^6}", end='')
        if (i , j) == (-177 , -89):
            print('  ', ' ', sep='1', end='  ')
        else:
            print(f"{'-':^6}", end='')
    print()
















