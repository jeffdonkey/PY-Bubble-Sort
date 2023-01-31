def bubble_sort(lst):

  for i in range(len(lst)):
      swapped = False
      print(f"iteration ")
      for j in range(len(lst) - 1):
          print(f"comparing {lst[j], lst[j+1]}")
          if lst[j] > lst[j+1]:
              lst[j], lst[j+1] = lst[j+1], lst[j]
              swapped = True

      if not swapped:
          return
      
  return lst


    # True and False are added to stop the loops as soon as it has been sorted
    # In "bubbleSort.py" and "bSort_optimized.py" the FOR loop runs as many times
    # as the length of the list.  With this T/F check the loop stops when a correct
    # sort is completed.

    # ---Create a variable called swapped and set equal to False. Declare this variable
    #  inside of the outer loop and before the first print() function. We will use this
    #  variable to determine if items in the list have been swapped. In other words, we
    #  will use this variable to determine if the elements are swapped in the pass through
    #  the list. If they are not, then the list is sorted and we want the function to stop.

    # ---Set swapped equal to True if elements were swapped during a pass of the inner loop.
    #  In other words, if a swap occurs, set the variable equal to True.

    # ---Add a conditional statement in the outer FOR loop and below the inner FOR loop.
    #  The conditional statement should check if swapped is False and if it is, return.
    #  In other words, if elements have not been swapped in the iteration of the outer loop, return.

sample_list = [1, 5, 2, 6, 7]
print(f"Unsorted list: {sample_list}")
bubble_sort(sample_list)
print(f"Sorted list: {sample_list}")
