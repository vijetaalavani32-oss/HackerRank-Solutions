def average(array):
    distinct_heights =set(array)
    result=sum(distinct_heights) / len(distinct_heights)
    return round(result,3)

