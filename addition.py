import sys


def addition(*args, **kargs):
    sum = 0

    # if "nums" in kargs:
    #     for b in kargs["nums"]:
    #         sum += b

    for a in args:
        sum += a
    return sum


def main():
    sys.argv.pop(0)
    args = list(map(int, sys.argv))

    if(args):
        print(addition(nums=args))
    else:
        n = int(input("How many numbers you want to Sum: "))
        nums = []
        for i in range(n):
            nums.append(int(input(f"num {i+1}: ")))

        print(addition(nums=nums))


main()
