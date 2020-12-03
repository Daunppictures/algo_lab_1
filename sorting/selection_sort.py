import sort_counter

def selection_sort(pools):
    indexing_length = range(0, len(pools)-1)

    for iterator in indexing_length:
        max_capacity_index = iterator

        for max_capacity_iterator in range(iterator+1, len(pools)):
            if pools[max_capacity_iterator].capacity_in_liters > pools[max_capacity_index].capacity_in_liters:
                max_capacity_index = max_capacity_iterator
            sort_counter.selection_comp_counter += 1


        pools[max_capacity_index], pools[iterator] = pools[iterator], pools[max_capacity_index]
        sort_counter.selection_swap_counter += 1


    return pools
