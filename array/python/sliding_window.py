#find k largest array 

def sliding_window(arr,k):
    ms = 0
    for i in range(k):
        ms += arr[i]
    #print(ms)
    s = ms
    for j in range(k,len(arr)):
        s += -arr[j-k] + arr[j]
        #1print(j,s)
        if s > ms:
            ms = s

    return ms

arr = [1,4,2,10,23,3,1,0,20]

print(sliding_window(arr,3))
