import sort_counter


def merge(left, right):
    array_of_sorted_numbers = []
    left_index, right_index = 0, 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index].max_number_of_concurrent_visitors > right[
            right_index].max_number_of_concurrent_visitors:
            array_of_sorted_numbers.append(left[left_index])
            left_index += 1
            sort_counter.merge_comp_counter += 1
        else:
            array_of_sorted_numbers.append(right[right_index])
            right_index += 1
            sort_counter.merge_comp_counter += 1

        sort_counter.merge_swap_counter += 1
    if left_index == len(left):
        array_of_sorted_numbers.extend(right[right_index:])

    else:
        array_of_sorted_numbers.extend(left[left_index:])
    sort_counter.merge_comp_counter += 1

    return array_of_sorted_numbers


def merge_sort_by_visitors(pools):
    if len(pools) <= 1:
        return pools

    left, right = merge_sort_by_visitors(
        pools[:len(pools) // 2]), merge_sort_by_visitors(
        pools[len(pools) // 2:])

    return merge(left, right)
