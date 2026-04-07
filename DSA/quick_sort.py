def quick_sort(pages):

    if len(pages)<=1:
        return pages
    pivot = pages[len(pages)//2]
    key = [x for x in pages if x == pivot]
    left = [x for x in pages if x < pivot ]
    right = [x for x in pages if x > pivot]
    return quick_sort(left)+key+quick_sort(right)
pages = [400,50,300,200]
print(quick_sort(pages))

def quick_sort(scores):
    n = len(scores)
    if n<=1:
        return scores
    pivot = scores[0]
    left = []
    right = []
    for i in range(1 , n):
        if scores[i][1]>=pivot[1]:
            left.append(scores[i])
        else:
            right.append(scores[i])
    return quick_sort(left)+[pivot]+quick_sort(right)
scores = [ ("Rohit", 85), ("Virat", 120), ("Dhoni", 60), ("Hardik", 95), ("Rahul", 110) ] 
print(quick_sort(scores)) 