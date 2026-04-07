def bubble_sort(scores):
    n = len(scores)
    Rank_changes = 0
    for i in range(n-1):
        for j in range(n-1-i):
            if scores[j] < scores[j+1]:
                scores[j] , scores[j+1] = scores[j+1], scores[j]
                Rank_changes +=1
    return scores  , Rank_changes
scores = [500, 100, 400, 200, 300]
print (bubble_sort(scores))       