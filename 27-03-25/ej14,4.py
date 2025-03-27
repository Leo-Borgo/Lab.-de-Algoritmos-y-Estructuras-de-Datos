import os, time, random
os.system("cls")

nums = []
orden = ["1ero", "2do", "3ro", "4to", "5to", "6to", "7mo", "8vo", "9no"]
menu = True

for num in range(1, 10):
    nums.append(num)

while menu == True:
    if nums[0] == 1:
        print(orden[0]), time.sleep(1)
    if nums[1] == 2:
        print(orden[1]), time.sleep(1)
    if nums[2] == 3:
        print(orden[2]), time.sleep(1)
    if nums[3] == 4:
        print(orden[3]), time.sleep(1)
    if nums[4] == 5:
        print(orden[4]), time.sleep(1)
    if nums[5] == 6:
        print(orden[5]), time.sleep(1)
    if nums[6] == 7:
        print(orden[6]), time.sleep(1)
    if nums[7] == 8:
        print(orden[7]), time.sleep(1)
    if nums[8] == 9:
        print(orden[8]), time.sleep(1)
    menu = False