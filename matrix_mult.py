
def matmul(a, b):
    c = []
    for i in range(0, len(a)):
        c.append([])
        for k in range(0, len(b[0])):
            num = 0
            for j in range(0, len(a[0])):
                num += a[i][j]*b[j][k]
            c[i].append(num)
    return c

def main():
    a = [[1,2],[3,4],[5,6]]
    b = [[3,2,1],[4,1,3]]
    d = matmul(a,b)
    print(a)
    print(b)
    print(d)


if __name__ == '__main__':
    main()
