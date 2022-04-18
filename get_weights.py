from kruskal import union_find_kruskal
from kruskal import naive_kruskal
from kruskal import Graph as KruskalGraph
from prim import prim
from prim import Graph as PrimGraph
import xlsxwriter
import os

if __name__ == '__main__':

    dir_name = 'mst_dataset'
    num_calls = 100000
    num_instances = 4
    graph_sizes = []
    run_times = []
    row = 0

    directory = os.fsencode(dir_name)
    # OPEN EXCEL FILE TO REPORT THE TREE WEIGHT FOR EACH PROBLEM
    workbook = xlsxwriter.Workbook('results/mst_weights.xlsx')
    worksheet = workbook.add_worksheet()

    for file in sorted(os.listdir(directory)):
        filename = os.fsdecode(file)
        if filename.endswith('.txt'):
            # WRTIE INPUT NAME IN EXCEL
            row += 1
            worksheet.write('A' + str(row), filename)
            # READ GRAPH INFORMATION
            f = open(dir_name + '/' + filename)
            line = f.readline().split()
            edges = f.read().splitlines()
            f.close()
            # BUILD GRAPH FOR KRUSKAL ALGORITHMS
            kruskal_g = KruskalGraph(int(line[0]), int(line[1]))
            kruskal_g.add_edges(edges)
            # BUILD GRAPH FOR PRIM ALGORITHM
            prim_g = PrimGraph(int(line[0]), int(line[1]))
            prim_g.add_edges(edges)
            # GET MST WEIGHT FROM EACH ALGORITHM
            naive_kruskal_weights = naive_kruskal(kruskal_g)
            union_find_kruskal_weights = union_find_kruskal(kruskal_g)
            prim_weights = prim(prim_g)
            # WRITE WEIGHTS INTO EXCEL FILE
            worksheet.write('B' + str(row), naive_kruskal_weights)
            worksheet.write('C' + str(row), union_find_kruskal_weights)
            worksheet.write('D' + str(row), prim_weights)
            # TO TEST ONLY FIRST 30 EXAMPLES
            if row == 30:
                break

    workbook.close()

