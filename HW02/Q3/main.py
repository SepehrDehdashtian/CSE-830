import bisect


def find_median(my_array):
    n = len(my_array)
    if n % 2 != 0:
        return int(my_array[n//2])
    else:
        median = 0.5 * (my_array[n//2-1] + my_array[n//2])
        if median.is_integer():
            return int(median)
        else:
            return round(median, 1)

 
N = int(input())


sorted_list = [ ]   
for _ in range(N):    
    inst, val = input().split()
    val = int(val)

    if inst == 'r':
        if val in sorted_list:
            sorted_list.remove(val)
            if len(sorted_list) != 0 :
                print(find_median(sorted_list))
            else:
                print("Wrong!")  
        else:
            print("Wrong!") 
            
                    
    elif inst == 'a':
        bisect.insort(sorted_list, int(val))
        print(find_median(sorted_list))