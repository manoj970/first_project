def insert_books(pages):
    n=len(pages)
    shift = 0
    for i in range(1 , n):
        key = pages[i]
        j = i -1
        while j>=0 and pages[j]>key:
            pages[j+1] = pages[j]
            shift +=1
            j-=1
        pages[j+1] = key
    return pages , shift       
pages = [300, 150, 400, 250, 100]
print(insert_books(pages))



