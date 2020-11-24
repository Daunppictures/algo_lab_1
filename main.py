from timeit import default_timer as timer
import csv_reader
from sorting.merge_sort import *
from sorting.selection_sort import selection_sort
import copy

from datetime import timedelta
import info_printer

if __name__ == '__main__':
    list_of_pools = csv_reader.read_cvs_file('pool.csv')

    start_time = timer()
    sorted_list = merge_sort_by_visitors(copy.deepcopy(list_of_pools))
    elapsed_time = timedelta(seconds=timer() - start_time)

    print('-------------------- MERGE SORT --------------------')
    info_printer.print_algorithm_info(elapsed_time, 'MERGE')
    print('---------------------- RESULT ----------------------')
    info_printer.print_list(sorted_list)
    print('\n')

    start_time = timer()
    sorted_list = selection_sort(copy.deepcopy(list_of_pools))
    elapsed_time = timedelta(seconds=timer() - start_time)

    print('------------------ SELECTION SORT ------------------')
    info_printer.print_algorithm_info(elapsed_time, 'SELECTION')
    print('---------------------- RESULT ----------------------')
    info_printer.print_list(sorted_list)
    print('\n')
