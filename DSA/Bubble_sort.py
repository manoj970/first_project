def Liberary(pages):
    n = len(pages)
    for i in range(n-1):
        for j in range(n-1-i):
            if pages[j] > pages[j+1]:
                pages[j] , pages[j+1] = pages[j+1] , pages[j]
    return pages
pages = [250 , 100 ,350 , 550 , 150 ,50 , 200]     
print(Liberary(pages))     