def main():
 x = int(input(""))

 factorial = 1

 if x == 0:
   print("The factorial of 0 is 1")
 elif x>0:
   for i in range(1,x + 1):
       factorial = factorial*i
   print(factorial)

if __name__ == '__main__':
    main()
