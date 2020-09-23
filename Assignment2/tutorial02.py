# All decimal 3 places

# Function to sort the list
def sorting(first_list):
    n = len(first_list)
    for i in range(0, n):
        for j in range(0, n-1):
            try:
                first_list[j] = float(first_list[j])
                first_list[j+1] = float(first_list[j+1])
                if first_list[j] > first_list[j+1]:
                    temp = first_list[j]
                    first_list[j] = first_list[j+1]
                    first_list[j+1] = temp
            except ValueError:
                return 0
    return first_list


# Function to compute sum. You cant use Python functions
def summation(first_list):
    summation_value = 0
    for i in first_list:
        try:
            i = float(i)
            summation_value += i
        except ValueError:
            return 0
    return summation_value

# Function to compute mean


def mean(first_list):

    sum_value = summation(first_list)
    total_elements = len(first_list)
    mean_value = round(sum_value/total_elements, 3)
    return mean_value


# Function to compute median. You cant use Python functions
def median(first_list):

    first_list = sorting(first_list)

    n = len(first_list)
    if n % 2 == 0:
        j = int(n/2)
        median_value = (first_list[j]+first_list[j-1])/2

    else:
        j = int(n/2)
        median_value = first_list[j]
    return round(median_value, 3)

# Function to compute variance. You cant use Python functions


def variance(first_list):
    mean_value = mean(first_list)
    variance_value = 0
    n = len(first_list)
    for i in range(0, n):
        try:
            first_list[i] = float(first_list[i])
            variance_value += (mean_value -
                               first_list[i])*(mean_value-first_list[i])
        except ValueError:
            return 0
    variance_value /= n
    return round(variance_value, 3)


# Function to compute Standard deviation. You cant use Python functions
# def standard_deviation(first_list):
#     # Standard deviation Logic
#     # return standard_deviation_value


# Function to compute RMSE. You cant use Python functions
# def rmse(first_list, second_list):
#     # RMSE Logic
#     # return rmse_value

#     # Function to compute mse. You cant use Python functions


# def mse(first_list, second_list):
#     # mse Logic
#     # return mse_value

#     # Function to compute mae. You cant use Python functions


# def mae(first_list, second_list):
#     # mae Logic
#     # return mae_value

#     # Function to compute NSE. You cant use Python functions


# def nse(first_list, second_list):
#     # nse Logic
#     # return nse_value

#     # Function to compute Pearson correlation coefficient. You cant use Python functions


# def pcc(first_list, second_list):
#     # nse Logic
#     # return pcc_value

#     # Function to compute Skewness. You cant use Python functions


# def skewness(first_list):
#     # Skewness Logic
#     # return skewness_value


# Function to compute Kurtosis. You cant use Python functions
# def kurtosis(first_list):
#     # Kurtosis Logic
#     # return kurtosis_value


# x = [1, 2, 3, 'yay', 5]
# print(variance(x))
