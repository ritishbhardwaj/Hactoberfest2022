'''
problem statement:  finding the majority element in the given array means when an element occurs in an array more than
                    (n/2) times where n is the length of an array
'''''' Using Moore Voting Algorithm
and getting candidate key
'''

def majority_element(arr):   # finding candidate key for majority element
    size=len(arr)
    count=1
    majorityIndex=0
    majorityElement=arr[majorityIndex]
    for i in range(1,size):
        if arr[i]==majorityElement:
            count+=1

        else:
            count-=1
        if count==0:
            majorityIndex=i
            majorityElement=arr[majorityIndex]
            count=1
    return [majorityElement]

def IsMajority_element(arr_majority,arr):
    count=0
    size=len(arr)
    for i in range(size):
        if arr[i]==arr_majority[0]:
            count+=1
    if count>(size//2):
        print("majority element is :",arr_majority[0])
        return True


arr = [1, 2, 4, 8, 4, 4]
arr_majority=majority_element(arr)
print(IsMajority_element(arr_majority,arr))
