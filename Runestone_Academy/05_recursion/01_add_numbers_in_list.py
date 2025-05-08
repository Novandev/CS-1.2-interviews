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



def simplified_solution(arr):
    '''
        We need to study the call stack stuff mostly from runestone
    
        
        How this works is that for recursive calls, it has to reach the base state as the end of the call stack, it then 
        comes back up the call stack and ads it

        [1,2,3,4,5]

        Step 1:

            returns 1 + [2,3,4,5]
        
        Step 2:

            returns 2 + [3,4,5]
        Step 3:

            returns 3 + [4,5]
        Step 4:

            returns 4 + [5]

        Step 5:
            The length of the list is now just 1 , [5]

            returns 5 and now must go back up the call stack
        
        Step 6:

            returns 4 + 5 # Returned from the base case of step 5

            so it actually:

            returns 9

        Step 7:

            returns 3 + 9 # Returned from the base case of step 6

        Step 8:

            returns 2 + 12 # Returned from the base case of step 7
        Step 9:

            returns 1 + 14 # Returned from the base case of step 7

        Step 9:

            returns [15]

            the length of the list is now 1
    '''

    if len(arr) == 1:
        return arr[0]
    
    else:
        return arr[0] + simplified_solution(arr[1:])


if __name__ == "__main__":
