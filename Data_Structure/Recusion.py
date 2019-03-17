def listSum(listnum):
    if len(listnum) == 1:
        return listnum[0]
    else:
        return listnum[0] + listSum(listnum[1:])


num = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(listSum(num))