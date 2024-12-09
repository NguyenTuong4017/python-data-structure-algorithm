# # Write a function named combine_lists that accepts two lists of integers as parameters. 
# # Consider that the two lists are already sorted (The numbers are already in order from smallest to biggest number).
# # Your function should return a list that combines the two lists and at the same time is itself also sorted. 
# # To be clear all elements of the input lists should be in the output list and len(input_list1)+len(input_list2) == len(output_list). 
# # Notice that your function should return the list, not print it.


def combine_lists(l1, l2):
    final_list = []
    while(len(l1) > 0 or len(l2) > 0):
        
        x = min(l1 + l2)        
        final_list.append(x)
        
        
        if x in l1:
            l1.remove(x)
        else:
            l2.remove(x)
        

    return final_list

l1 = [4,2,6,7,37,734,3,37,2,62,643,6,3,36,46,236,7,456885,236,3488,5648,568,458,5485,8,458,456,8,56845,35486,3,3,45]
l2 =[645,4,3,6,7,34,754,7,3547,4,78,8,37,3457,54,75,7,547,453,7543,869689,5,3,3,56,3,7,564,8,568,569,6759,76,9,67]
        
print(combine_lists(l1, l2))
