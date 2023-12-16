#Write a Python program to construct the following pattern, using a nested for loop.
h=5
for y in range(h):
    for z in range(y):
        print ('* ', end="")
    print('')

for y in range(h,0,-1):
    for z in range(y):
        print('* ', end="")
    print('')
