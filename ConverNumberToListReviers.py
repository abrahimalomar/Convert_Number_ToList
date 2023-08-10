
number =123456789
def ConvertNumberToList(n3):
    return [int(i) for i in str(n3)[::-1]]

print(ConvertNumberToList(number))