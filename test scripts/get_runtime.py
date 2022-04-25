import os
import gc
from time import perf_counter_ns
import matplotlib.pyplot as plt
from kruskal import naive_kruskal
from prim import prim
from prim import Graph
from multiprocessing import Process



def measure_run_times(g, num_calls, num_instances, parallel=False):
    sum_times = 0.0
    for k in range(num_instances):
        gc.disable()
        start_time = perf_counter_ns()
        proc = []
        for j in range(num_calls):
            if parallel:
                p = Process(target=prim, args=(g,))
                p.start()
                proc.append(p)
                for p in proc:
                    p.join()
            else:
                prim(g)
        end_time = perf_counter_ns()
        gc.enable()
        sum_times += (end_time - start_time) / num_calls
    avg_time = int(round(sum_times / num_instances))
    # return average time in nanoseconds
    return avg_time


if __name__ == '__main__':

    dir_name = 'mst_dataset'
    num_calls = 1
    num_instances = 1
    graph_sizes = []
    run_times = []
    row = 0
    par = False
    directory = os.fsencode(dir_name)
    output = open('results/prim_results.txt', 'w+')
    output.write("Sizes\tTimes\n")
    for file in sorted(os.listdir(directory)):
        filename = os.fsdecode(file)
        if filename.endswith('.txt'):
            row += 1
            print("doing the ", row, "th problem...")
            f = open(dir_name + '/' + filename)
            line = f.readline().split()
            g = Graph(int(line[0]), int(line[1]))
            edges = f.read().splitlines()
            g.add_edges(edges)
            f.close()
            g_size = g.num_vertex

            runtime = measure_run_times(g, num_calls, num_instances, par)
            graph_sizes.append(g_size)
            run_times.append(runtime)
            output.write("%s\t%s\n" % (g_size, runtime))



    plt.plot(graph_sizes, run_times)
    plt.legend(['Measured times'])
    plt.xlabel('Number of vertices')
    plt.ylabel('Run times (ns)')
    plt.show()