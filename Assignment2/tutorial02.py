# All decimal 3 places

# Function to sort the list
import math


def sorting(first_list):
    n = len(first_list)
    sorting_list = first_list.copy()
    for i in range(0, n):
        for j in range(0, n-1):
            try:
                sorting_list[j] = float(sorting_list[j])
                sorting_list[j+1] = float(sorting_list[j+1])
                if sorting_list[j] > sorting_list[j+1]:
                    temp = sorting_list[j]
                    sorting_list[j] = sorting_list[j+1]
                    sorting_list[j+1] = temp
            except ValueError:
                return 0
    return sorting_list


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

    median_list = sorting(first_list)

    n = len(first_list)
    if n % 2 == 0:
        j = int(n/2)
        median_value = (median_list[j]+median_list[j-1])/2

    else:
        j = int(n/2)
        median_value = median_list[j]
    return round(median_value, 3)

# Function to compute variance. You cant use Python functions


def variance(first_list):
    n = len(first_list)
    variance_list = []
    mean_value = summation(first_list)
    mean_value /= n
    for i in range(0, n):
        try:
            first_list[i] = float(first_list[i])
            variance_list.append((mean_value -
                                  first_list[i])*(mean_value-first_list[i]))
        except ValueError:
            return 0
    variance_value = summation(variance_list)
    variance_value /= n
    return round(variance_value, 3)


# Function to compute Standard deviation. You cant use Python functions
def standard_deviation(first_list):
    n = len(first_list)
    mean_value = summation(first_list)
    mean_value /= n
    standard_deviation_list = []
    for i in range(0, n):
        try:
            first_list[i] = float(first_list[i])
            standard_deviation_list.append((mean_value -
                                            first_list[i])*(mean_value-first_list[i]))
        except ValueError:
            return 0
    standard_deviation_value = summation(standard_deviation_list)
    standard_deviation_value /= n
    standard_deviation_value = math.sqrt(standard_deviation_value)
    return round(standard_deviation_value, 3)


# Function to compute RMSE. You cant use Python functions
def rmse(first_list, second_list):
    if len(first_list) == len(second_list):
        n = len(first_list)
        rmse_list = []
        for i in range(0, n):
            try:
                first_list[i] = float(first_list[i])
                second_list[i] = float(second_list[i])
                x = first_list[i]-second_list[i]
                rmse_list.append((x*x))
            except ValueError:
                return 0
        rmse_value = summation(rmse_list)
        rmse_value /= n
        rmse_value = math.sqrt(rmse_value)
        return round(rmse_value, 3)
    else:
        return 0


# Function to compute mse. You cant use Python functions
def mse(first_list, second_list):
    if len(first_list) == len(second_list):
        n = len(first_list)
        mse_list = []
        for i in range(0, n):
            try:
                first_list[i] = float(first_list[i])
                second_list[i] = float(second_list[i])
                x = first_list[i]-second_list[i]
                mse_list.append((x*x))
            except ValueError:
                return 0
        mse_value = summation(mse_list)
        mse_value /= n
        return round(mse_value, 3)
    else:
        return 0


# Function to compute mae. You cant use Python functions
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
