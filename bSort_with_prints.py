# write your bubble sort algorithm below

def bubble_sort(lst):

      for i in range(len(lst)-1):
        print(f"iteration ")
        for j in range(len(lst) - 1):
            print(f"comparing {lst[j], lst[j+1]}")
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
      
      return lst

# added print lines so you can see the comparisons   

# test data

sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")

