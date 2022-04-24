
import os
import gc
from time import perf_counter_ns
import matplotlib.pyplot as plt
from kruskal import naive_kruskal
from prim import prim
from prim import Graph


def measure_run_times(g, num_calls, num_instances):
    sum_times = 0.0
    for k in range(num_instances):
        gc.disable()
        start_time = perf_counter_ns()
        for j in range(num_calls):
            prim(g)
        end_time = perf_counter_ns()
        gc.enable()
        sum_times += (end_time - start_time) / num_calls
    avg_time = int(round(sum_times / num_instances))
    # return average time in nanoseconds
    return avg_time


if __name__ == '__main__':

    dir_name = 'mst_dataset'
    num_calls = 100000
    num_instances = 4
    graph_sizes = []
    run_times = []

    directory = os.fsencode(dir_name)
    for file in sorted(os.listdir(directory)):
        filename = os.fsdecode(file)

        if filename.endswith('.txt'):
            f = open(dir_name + '/' + filename)
            line = f.readline().split()
            g = Graph(int(line[0]), int(line[1]))
            edges = f.read().splitlines()
            g.add_edges(edges)
            f.close()
            graph_sizes.append(g.num_vertex)
            run_times.append(measure_run_times(g, num_calls, num_instances))

    with open('../results/prim_results.txt', 'w+') as f:
        f.write("Sizes\tTimes")
        for i in range(len(graph_sizes)):
            f.write("%s\t%s\n" % (graph_sizes[i], run_times[i]))

    plt.plot(graph_sizes, run_times)
    plt.legend(['Measured times'])
    plt.xlabel('Number of vertices')
    plt.ylabel('Run times (ns)')
    plt.show()
