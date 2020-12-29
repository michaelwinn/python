

def all_index(array, num):
    indx = []
    for i in range(0,len(array)):
        for j in range(0,array[i].count(num)):
            if j == 0:
                indx.append([i, array[i].index(num)])
            else:
                indx.append([i, array[i].index(num,indx[j-1][1]+1)])

    return indx

tic = [[1,1,0],[0,2,1],[1,2,2]]

print(all_index(tic, 1))
