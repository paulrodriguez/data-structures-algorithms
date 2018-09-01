class MergeSort:
    def sort(self,arr):
        start = 0
        end = len(arr)-1
        
        self.merge_sort(arr,start, end)
        return arr
    
    def merge_sort(self, arr,start,end):
        if start < end:
            # using python 2
            middle = (start+end)/2
            self.merge_sort(arr,start,middle)
            self.merge_sort(arr,middle+1,end)
            self.merge(arr,start,middle,end)

    def merge(self,arr,start,middle,end):
        # add 1 to end since its exclusive
        left = arr[start:middle+1]
        right = arr[middle+1:end+1]

        l_counter = 0
        r_counter = 0
        counter = start

        while l_counter<len(left) and r_counter <len(right):
            if left[l_counter]<right[r_counter]:
                arr[counter] = left[l_counter]
                l_counter += 1
            else:
                arr[counter] = right[r_counter]
                r_counter += 1

            counter += 1

        while l_counter < len(left):
            arr[counter] = left[l_counter]
            l_counter += 1
            counter += 1

        while r_counter < len(right):
            arr[counter] = right[r_counter]
            r_counter += 1
            counter += 1
        
        
