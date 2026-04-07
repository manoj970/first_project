def bubble_sort(grades):
    n= len(grades)
    swaps = 0 
    for i in range(n-1):
        for j in range(n-1-i):
            if grades[j]>grades[j+1]:
                grades[j] , grades[j+1] = grades[j+1] , grades[j]
                swaps +=1
    return grades , swaps
grades = [90, 85, 80, 75, 70]

print(bubble_sort(grades))       