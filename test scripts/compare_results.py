import matplotlib.pyplot as plt
import math
if __name__ == '__main__':
    # READ RESULTS FROM .txt FILE
    f = open('../results/kruskal_naive_results.txt')
    f.readline()
    sizes = []
    naive_kruskal_time = []

    for line in f:
        result = line.split()
        sizes.append(int(result[0]))
        naive_kruskal_time.append(int(result[1]))
    f.close()

    f = open('../results/kruskal_union_find_results.txt')
    f.readline()
    union_find_kruskal_time = []
    for line in f:
        result = line.split()
        union_find_kruskal_time.append(int(result[1]))
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

    c_estimates_naive = [naive_kruskal_time[i] / sizes[i] for i in range(len(sizes))]
    constant_naive = naive_kruskal_time[len(c_estimates_naive) // 4]
    reference_naive = [constant_naive * size for size in sizes]
    #plt.plot(sizes, reference_naive, label='constant for naive')
    #reference_union = [constant_union * size for size in listsizes]
    #plt.plot(listsizes, reference_union, label='constant for union')


    plt.legend()
    plt.xlabel('Number of vertices')
    plt.ylabel('Run times (ns)')
    plt.show()

    # ===========================================================================
