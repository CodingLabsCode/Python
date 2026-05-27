nums = ["8", "4","3","1","6","2","1","7","4","8","5","1"]
def sort():
    sorted_nums = sorted(nums, reverse=False)
    for num in sorted_nums:
        print(f"{num} | ",end="")
def remove():
    remove_dupes = sorted(set(nums))
    for num in remove_dupes:
        print(f"{num} | ",end="")
print("Number List")
for num in nums:
    print(f"{num} | ",end="")
while True:
    user = input("\n=== Numbers ===\n" 
           "(1)Sort Numbers\n" 
           "(2)Remove Duped Numbers\n" 
           "(3)Exit\n" 
           "Enter Options: ")
    match user:
        case "1":
            sort()
        case "2":
            remove()
        case "3":
            print("GoodBye")
            exit()
        case _:
            print("1-3 Only")
