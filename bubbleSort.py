# write your bubble sort algorithm below
def bubble_sort(lst):
      for i in range(len(lst)-1):
          for j in range(len(lst) - 1):
              if lst[j] > lst[j+1]:
                  lst[j], lst[j+1] = lst[j+1], lst[j]
      
      return lst

    # 'lst" is short for list, not first.  it's just a name for an argument
    # line 3 is the outer loop. This loop will run as many times as there are
        # elements in the list (one less than the length of the list)
    # line 4 is the inner loop.  This loop will compare all the values in the
        # list for each pass.
    # line 5 is the conditional statement for the inner FOR loop.  It is checking
        # if the element on the LEFT > element on the RIGHT
    # line 6 is what to do if the condition is met on line 5.  If condition is
        # met then swap the places of the elements of the list
    # line 8 returns the new value of 'lst'

# test data

sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")

