# 0,    0,  672,  378 |  640,    0, 1312,  378 | 1280,    0, 1920,  378 
# 0,  360,  672,  738 |  640,  360, 1312,  738 | 1280,  360, 1920,  738
# 0,  720,  672, 1080 |  640,  720, 1312, 1080 | 1280,  720, 1920, 1080

# 0, 0,  a+32, 1b+18 | a,  0, 2a+32, 1b+18 | 2a,  0, 3a, 1b+18
# 0, 1b, a+32, 2b+18 | a, 1b, 2a+32, 2b+18 | 2a, 1b, 3a, 2b+18
# 0, 2b, a+32, 3b    | a, 2b, 2a+32, 3b    | 2a, 2b, 3a, 3b

a = 640 #width
b = 480 #height
s = 32  #shift
tiles = 3 #tiles

def threeDimensionalArray(a, b, c):
    x = [[[0 for _ in range(a)] for _ in range(b)] for _ in range(c)]
    return x

m = threeDimensionalArray(4,2,3)
print(m)

for i in range(tiles): # columns
    for j in range(tiles): # rows
        m[i][j][0] = a*j
        m[i][j][1] = b*i
        a = a*(j+1)
        m[i][j][2] = a+s
        m[i][j][3] = b+(s/2)