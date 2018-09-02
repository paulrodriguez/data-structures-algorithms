class QuickSort:
    def sort(self,arr):
        start = 0
        end = len(arr) - 1
        self.quick_sort(arr,start,end)

    def quick_sort(self,arr,start,end):
        if start < end:
            pivot = self.partition(arr, start,end)
            self.quick_sort(arr,start,pivot-1)
            self.quick_sort(arr,pivot+1,end)

    def partition(self,arr,start,end):
        pivot = arr[end]
        i = start - 1
        for j in range(start,end):
            if arr[j] <= pivot:
                i += 1
                tmp = arr[j]
                arr[j] = arr[i]
                arr[i] = tmp

        tmp = arr[i+1]
        arr[end] = tmp
        arr[i+1] = pivot

        return i + 1
