def calc_avg(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)

number_list = [2,5,6,4,3,1,7]
for i in range(len(number_list)):
    sublist = number_list[:i+1]
    average = calc_avg(sublist)
    print("The average of ",sublist, "is",average)