from bridge import sum_of_inputs


def clear_last(x):
    sum_of_inputs.remove(sum_of_inputs[-1])
    return x

