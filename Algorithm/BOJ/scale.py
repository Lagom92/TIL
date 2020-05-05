# 백준 2920번 음계

def scale(num_list):
    asc_flag = True
    desc_flag = True

    for i in range(7):
        if num_list[i] + 1 != num_list[i+1]:
            asc_flag = False
            
        if num_list[i] - 1 != num_list[i+1]:
            desc_flag = False
            
    if asc_flag:
        return "ascending"
    elif desc_flag:
        return "descending"
    else:
        return "mixed"


num_list = list(map(int, input().split()))
res = scale(num_list)
print(res)
