# to find maximum element of a list
n=int(input("Enter the number of elements: "))
print("Enter the elements: ")
a=[]
for i in range(0, n):
    a.append(int(input()))
print("The elements of list are:", a)
max=a[0]
for i in range(0, n):
    if a[i]>max:
        max=a[i]
print("The maximum element is: ",max)

# thanks for watching
# like, share & subscribe to
# Dream 2 code
