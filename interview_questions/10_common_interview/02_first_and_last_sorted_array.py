'''
Given a sorted Array and a target, return the first position and last position in which this occurs


example input


0,1,1,2,3,3,3,3,3,3,4

Target = 3


algorithm


First use the first pointer to find the target number, if it's not found, return [-1,-1].

Keep the counter there and set the last counter to the same position



'''

def first_and_last_my_solution(arr,target):


    first = 0
    last = 0

    while first <= len(arr) -1 :

        if arr[first] == target and arr[first] == len(arr) -1: # first base case no repeats and at end
            return[first, first]
        
        if arr[first] == target: #check to see if the counter at thecurrent check is a mathc
             

             if arr[first + 1]  == target: # if the next one is also a match,we know weve started the logier for the mini loop
                 
                 last = first + 1 # assign a pointer so the  "last" is pointed to the one ahead

                 while last <= len(arr) -1:
                     
                     if arr[last]  == target:# if the current "last" is the target, increment, else return that we've found it
                         last = last + 1

                     else:
                         return [first, last - 1]
        else:
            first += 1 
                     


def first_and_last_official(target, array):

    '''
    
        This uses 3 functions to solve this equation
    
    '''



    def first_and_last(arr, target): # This runs in O(n-k)
        '''
            This is the  function that takes an array and matches the start to the end
            You'll need a variables one start that determines the start of finding the sublist
        '''

        for i in range(len(arr)):# interate through the list

            if arr[i] == target: # If matched

                start = i # Declare the start variable that we'll return as the index of the start

                while i + 1 < len(arr) and arr[i+1] == i: # While we're still traversing the array and the next number still matches

                    i += 1 # Increase the interation and keep going

                return [start, i]
                
        return [-1, -1]
    
    def find_start(array, target):
        '''
        
        '''
        if array[0] == target:
            return 0
        
        first , last = 0, len(array) - 1 # declare the frist and last variables

        while first <= last:

            midpoint = (first + last) // 2

            '''
                If the value of the array at the midpoint is equal to the target, and the number after that midpoint is less that the 
                target, this means that weve found our starting point
            '''
            if array[midpoint] == target and array[midpoint + 1] < target: 
                return midpoint
            
            # '''
            #     If the value of the current midpoint is less than the target,
            #     we know that the value is somewhere in the later half of the array
            # '''
            elif array[midpoint] < target:
            
                first = midpoint + 1
            
            else:

                last = midpoint - 1

        return -1 # if we cant find it at all, return -1 as the index


def find_end(array,target):




if __name__ == '__main__':
    print( first_and_last_my_solution([0, 1, 1, 2, 3, 3, 3, 3, 3, 3, 4], 3) )




