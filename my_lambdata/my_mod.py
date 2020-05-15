from pandas import DataFrame
import pandas as pd


def enlarge(n):
    return n * 100


def check_nulls(df):
    '''
    Check a dataframe for nulls, print/report them in a nice "pretty" format
    '''
    total = df.isna().sum()
    total = total.sum()
    string = f"There are {total} null values in your dataframe"
    print(string)
    return string


def add_column(a_list, dataframe, feature):
'''
Single function to take a list, turn it into a series
and add it to a dataframe as a new column
'''
    a_list = pd.Series(a_list)
    dataframe[feature] = a_list
    print(dataframe)
    return dataframe


if __name__ == "__main__":
    # only runs the code below if executing this script from the command line
    # otherwise don't run it
    x = 6
    print(enlarge(x))

    y = int(input("Please choose an integer like 5: "))
    print(enlarge(y))

    # New Dataframe to test 'check_nulls'
    df1 = DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    check_nulls(df1)

    # add a column
    test = [1, 2, 9]
    add_column(test, df1, 'feature')
