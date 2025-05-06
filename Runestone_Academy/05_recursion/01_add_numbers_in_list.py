'''

    https://runestone.academy/ns/books/published/pythonds/Recursion/pythondsCalculatingtheSumofaListofNumbers.html
'''

def add_numbers_of_list(arr, sum=0):
    '''
        This is an exercise to make sure that I can still do recursion just fine my own solution
        This runs in O(n) since every memeber of the list must be visited

        This is not ideal
    '''

    # Step 1 handle base cases

    # base case is that there is no members in the list
    if len(arr) == 0:
        return 0
    # Handle is there is only one member in the list
    if len(arr) == 1 and sum == 0:
        return arr[0]
    
    # is there is a sum, this means we've done this at least once
    if len(arr) == 1 and sum!=0:
        return sum
    
    # increment the sum on this step
    sum += arr[0]
    #make a recursive call while going down the next memeber of the list, without the return, this wont work and it wont return the results
    return add_numbers_of_list(arr[1:], sum)



def simplieifed_solution(arr):
    '''
        We need to study the call stack stuff mostly from runestone
    
        
        How this works is that for recursive calls, it has to reach the base state as the end of the call stack, it then 
        comes back up the call stack and ads it

        
    '''

    if len(arr) == 1:
        return arr[0]
    
    else:
        return arr[0] + simplieifed_solution(arr[1:])


if __name__ == "__main__":
