'''
Given a sorted Array and a target, return the first position and last position in which this occurs


example input


0,1,1,2,3,3,3,3,3,3,4

Target = 3


algorithm


First use the first pointer to find the target number, if it's not found, return [-1,-1].

Keep the counter there and set the last counter to the same position



'''

def first_and_last(arr,target):


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
                     

if __name__ == '__main__':
    print( first_and_last([0, 1, 1, 2, 3, 3, 3, 3, 3, 3, 4], 3) )




