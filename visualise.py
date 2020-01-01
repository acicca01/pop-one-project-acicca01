for i in range(-1,360,1):
    for j in range(-1,180):
        if j%2 == 0:
            print('-',end ='')
        else:
            print('|',end='')
    print()
    