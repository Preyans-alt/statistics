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




