

# Python program to print odd Numbers in given range 
  
start = int(input("enter the starting range: "))
end = int(input("enter the ending range: "))
for num in range(start, end + 1):
    if num % 2 != 0:
        print(num, end ="")
