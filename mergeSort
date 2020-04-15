def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    middle = int (len(lst)/2)

    left = merge_sort(lst[ :middle])#左边
    right = merge_sort(lst[middle: ])#右边
    merged = []
    while left and right:
        merged.append(left.pop(0) if left [0] <= right[0] else right.pop(0))
    merged.extend(right if right else left)  #该方法没有返回值，但会在已存在的列表中添加新的列表内容
    return merged
data_lst = [6,202,100,301,38,8,1]
print(merge_sort(data_lst))
