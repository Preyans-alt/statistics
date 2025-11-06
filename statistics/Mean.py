def linear_data(data):
    if len(data)>0:
        summation = sum(data)
        return summation/len(data)
    return "not valid data"


def group_data(data,freq):
    if len(data)>0:
        sum_freq = sum(freq)
        mul = 0
        for i in range(len(data)):
            mul += data[i]*freq[i]
        return mul/sum_freq
    return "not valid data"
def ungrouped_data():
    data_list = []
    freq_list = []
    while True:
        data = eval(input("enter interval(x,y) enter ('s') to stop:- "))
        if data=='s':
            break
        freq = int(input('enter frequence:- '))

        freq_list.append(freq)
        data_list.append((data[0]+data[1])/2)

    return group_data(data_list,freq_list)





