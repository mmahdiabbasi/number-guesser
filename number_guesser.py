min = 1
max = 0
while(min > max):
    min = int(input("please enter minimum number pussible: "))
    max = int(input("please enter maximum number pussible: "))
    if min > max:
        print("you game me wronge inputs, try again:")
steps = 0
while min <= max:
    steps += 1
    mid = int((min + max) /2)
    result = input("my guess is {}, is your number 'higher', 'lower' or equal to that? ".format(mid))
    if result == 'equal':
        print("i guessed your number with trying {} times!".format(steps))
        break
    elif result == 'lower':
        max = mid -1
    elif result == 'higher':
        min = mid + 1 
    else:
        print("wrong input! please try again!")
    if min > max :
        print("you game me incorrect response! i can't guess your number")
        break
import urllib.parse
link = urllib.parse.quote('github.com/mmahdiabbasi')
print("please view my other repos on github:")
print('https://'+link)