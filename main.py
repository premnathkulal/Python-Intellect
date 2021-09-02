def jollyJumper(li1):
    flag_1 = 0
    flag_2 = 0
    flag_3 = 0
    result = 0
    n = len(li1)
    temp2 = 0

    for i in range(0,n-1):

        temp1 = li1[i]
        temp3 = li1[i+1]

        if temp1 > temp3:
            temp4 = temp1 - temp3
        else:
            temp4 = temp3 - temp1

        if i == 0:
            temp2 = temp4
            continue
        else:
            if i == 1:

                if temp2 == temp4 + 1 and flag_1 == 0:
                    flag_1 = 1

                elif temp2 == temp4 - 1 and flag_3 == 0:
                    flag_3 = 1

            if temp2 != temp4+1 and flag_1 == 1:
                flag_2 = 1

            elif temp2 != temp4-1 and flag_3 == 1:
                result = 1

            temp2 = temp4

    if flag_1 == 1 and flag_2 == 0:
        return  1
    elif flag_3 == 1 and result == 0:
        return  1
    else:
        return 0


print("Enter a numbers :")
inputList = list(map(int, input().split()))

result = jollyJumper(inputList)

if result == 1:
    print("Jolly")
else:
    print("Not Jolly")
