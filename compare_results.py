import matplotlib.pyplot as plt


if __name__ == '__main__':
    # READ RESULTS FROM .txt FILE
    f = open('results/kruskal_naive_results.txt')
    f.readline()
    sizes = []
    naive_kruskal_time = []
    current_size = 0
    current_time = 0
    chunk_size = 10
    for line in f:
        result = line.split()
        #sizes.append(int(result[0]))
        if int(result[0]) == current_size:
            current_time += int(result[1])
            chunk_size += 1
        else:
            sizes.append(current_size)
            naive_kruskal_time.append(current_time/chunk_size)
            current_size = int(result[0])
            chunk_size = 0
            current_time = int(result[1])
    f.close()

    f = open('results/kruskal_union_find_results.txt')
    f.readline()
    union_find_kruskal_time = []
    current_size = 0
    current_time = 0
    chunk_size = 10
    for line in f:
        result = line.split()
        if int(result[0]) == current_size:
            current_time += int(result[1])
            chunk_size += 1
        else:
            union_find_kruskal_time.append(current_time/chunk_size)
            current_size = int(result[0])
            chunk_size = 0
            current_time = int(result[1])
        #union_find_kruskal_time.append(int(result[1]))
        # prim_time.append(int())
    f.close()

    '''f = open('results/prim_results.txt')
    f.readline()
    prim_time = []
    for line in f:
        result = line.split()
        prim_time.append(int(result[1]))
    f.close()'''


    plt.plot(sizes, naive_kruskal_time, label='Naive Kruskal')

    plt.plot(sizes, union_find_kruskal_time, label='Union Find Kruskal')
    #plt.plot(sizes, prim_time)
    #plt.legend(['Measured times'])
    plt.legend()
    plt.xlabel('Number of vertices')
    plt.ylabel('Run times (ns)')
    plt.show()
