def noofSubarrays(arr,k,threshold):
        target = k * threshold
        current_sum = sum(arr[:k])
        count = 0
        if current_sum >= target:
            count += 1
        for i in range(k,len(arr)):
            current_sum = current_sum - arr[i-k] +arr[i]
            if current_sum >= target:
                count +=1
        print(count)       
noofSubarrays([2,2,2,2,5,5,5,8] , 3 , 4)            