import math  

def main():
   a = int(input("What is the value of A?"))   
   b = int(input("What is te value of B?"))
   
   print("value of C is", pythag(a,b))
   #print("b squared is", pythag(b))

def pythag(A,B):
 
 c=math.sqrt((A**2)+(B**2))
 
 return c
 

 #TO DO  


main()
