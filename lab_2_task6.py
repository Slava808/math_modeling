

'''for i in range(1, 10, 1):
    print(i * 1,i * 2,i * 3,i * 4,i * 5,i * 6,i * 7,i * 8,i * 9)'''

for i in range(1,10):
   for p in range(1,10):
      print(i*p, end=" ")
      if p % 9 == 0:
         print()
         
    