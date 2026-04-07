def binary_search(seats, prefered_seat):
 n=len(seats)
 left=0
 right=n-1
 comparisons=0
 while left<=right:
  mid=(left+right)//2
  comparisons+=1
  if seats[mid]==prefered_seat:
   return f" seat:{seats[mid]} \n is available position in list:{mid} \n comparison made:{comparisons} "

  elif seats[mid]<prefered_seat:
   left=mid+1
  else:
   right=mid-1
 return f"{prefered_seat} is not in stock,\ncomparison:{comparisons}"
seats=["Aspirin","Cetirizine","Dolo650","Ibuprofen","Metformin", "Omeprazole", "Paracetamol","Ranitidine"]

print(binary_search(seats,"Dolo650"))