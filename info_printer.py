from datetime import timedelta
import sort_counter

def print_algorithm_info(elapsed_time: timedelta, sort_type: str):
    if sort_type == 'SELECTION':
        print('comparison counter: ' + str(sort_counter.selection_comp_counter))
        print('swap counter: ' + str(sort_counter.selection_swap_counter))
    elif sort_type == 'MERGE':
        print('comparison counter: ' + str(sort_counter.merge_comp_counter))
        print('swap counter: ' + str(sort_counter.merge_swap_counter))
    print('execution time: ' + str(elapsed_time))

def print_list(elements):
    for element in elements:
        print(element)