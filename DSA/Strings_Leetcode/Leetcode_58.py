def lastword(s):
  end = len(s) -1
  while s[end] == " ":
    end -=1
  start = end
  while start >= 0 and s[start] !=  " ":
    start -=1
  result = end - start
  print(result)
lastword("   fly me   to   the moon  ")  
