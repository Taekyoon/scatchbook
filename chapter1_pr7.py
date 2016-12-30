
def rotate_90_deg(w, h):
    cur_map = [[(x+1)+(y*w) for x in range(w)] for y in range(h)]
    new_map = [[0 for x in range(w)] for y in range(h)]

    print(cur_map)
    print(new_map)
    for i in range(w):
        for j in range(h):
            new_map[j][w-i-1] = cur_map[i][j]

    print(new_map)

rotate_90_deg(5,5)
