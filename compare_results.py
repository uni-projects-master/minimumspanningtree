import matplotlib.pyplot as plt
import math


if __name__ == '__main__':
    # --------------------------------------READ RESULTS FROM .txt FILE------------------------------------------------
    f = open('results/kruskal_naive_results.txt')
    f.readline()
    sizes = []
    naive_kruskal_time = []

    for line in f:
        result = line.split()
        sizes.append(int(result[0]))
        naive_kruskal_time.append(int(result[1]))
    f.close()

    f = open('results/kruskal_union_find_results.txt')
    f.readline()
    union_find_kruskal_time = []
    for line in f:
        result = line.split()
        union_find_kruskal_time.append(int(result[1]))
    f.close()

    f = open('results/prim_results.txt')
    f.readline()
    prim_time = []
    for line in f:
        result = line.split()
        prim_time.append(int(result[1]))
    f.close()

    # --------------------------------------FIRST FIGURE: KRUSKAL NAIVE------------------------------------------------
    plt.plot(sizes, naive_kruskal_time, label='Naive Kruskal')

    c_estimates_naive = [naive_kruskal_time[i] / sizes[i] for i in range(len(sizes)-1)]
    with open('results/c_estimates_naive.txt', 'w+') as f:
        f.write("Constant Estimations\n")
        for i in range(len(c_estimates_naive)):
            f.write(str(c_estimates_naive[i]) + "\n")

    # CONSTANT SELECTED FOR NAIVE KRUSKAL ALGORITHM
    reference_naive = [12582136 * size for size in sizes]
    plt.plot(sizes, reference_naive, label='Constant for naive')
    plt.legend()
    plt.xlabel('Number of vertices')
    plt.ylabel('Run times (ns)')

    # ---------------------------------------SECOND FIGURE: KRUSKAL UNION FIND------------------------------------------
    plt.figure()
    plt.plot(sizes, union_find_kruskal_time, label='Union Find Kruskal')

    c_estimates_union = [union_find_kruskal_time[i] / sizes[i] for i in range(len(sizes)-1)]
    with open('results/c_estimates_union_find.txt', 'w+') as f:
        f.write("Constant Estimations\n")
        for i in range(len(c_estimates_union)):
            f.write(str(c_estimates_union[i]) + "\n")

    # CONSTANT SELECTED FOR UNION FIND ALGORITHM
    reference_union = [10185090 * size for size in sizes]
    plt.plot(sizes, reference_union, label='Constant for union')
    plt.legend()
    plt.xlabel('Number of vertices')
    plt.ylabel('Run times (ns)')
    
    # ---------------------------------------THIRD FIGURE: PRIM-------------------------------------------------------
    plt.figure()
    plt.plot(sizes, prim_time, label='Prim')

    c_estimates_prim = [prim_time[i] / sizes[i] for i in range(len(sizes)-1)]
    with open('results/c_estimates_prim.txt', 'w+') as f:
        f.write("Constant Estimates\n")
        for i in range(len(c_estimates_prim)):
            f.write(str(c_estimates_prim[i]) + "\n")

    # CONTSTANT SELECTED FOR PRIM ALGORITHM
    reference_prim = [10392495 * size for size in sizes]
    plt.plot(sizes, reference_prim, label='Constant for prim')
    plt.legend()
    plt.xlabel('Number of vertices')
    plt.ylabel('Run times (ns)')

    # -------------------------------------FOURTH FIGURE: THREE ALGORITHMS TOGETHER----------------------------------
    plt.figure()
    plt.plot(sizes, naive_kruskal_time, label='Kruskal Naive')
    plt.plot(sizes, union_find_kruskal_time, label='Kruskal Union Find')
    plt.plot(sizes, prim_time, label='Prim')
    plt.legend()
    plt.xlabel('Number of vertices')
    plt.ylabel('Run times (ns)')

    #--------------------------------------FIFTH FIGURE: THREE ALGORITHMS TOGETHER WITH THREE CONSTANTS--------------
    plt.figure()
    plt.plot(sizes, naive_kruskal_time, label='Kruskal Naive')
    plt.plot(sizes, reference_naive, label='Constant for naive')
    plt.plot(sizes, union_find_kruskal_time, label='Kruskal Union Find')
    plt.plot(sizes, reference_union, label='Constant for union')
    plt.plot(sizes, prim_time, label='Prim')
    plt.plot(sizes, reference_prim, label='Constant for prim')
    plt.legend()
    plt.xlabel('Number of vertices')
    plt.ylabel('Run times (ns)')

    plt.show()

    # ===========================================================================
