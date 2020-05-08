

def enlarge(n):
    return n * 100

def check_nulls(df):
    total = df.isna().sum()
    total = total.sum()
    string = f"There are {total} null values in your dataframe"
    return string


if __name__ == "__main__":
    #only runs the code below if executing this script from the command line
    #otherwise don't run it

    
    x = 6 
    print(enlarge(x))

    y = int(input("Please choose an integer like 5: "))
    print(enlarge(y))


    #New Dataframe tot test 'check_nulls'
    df1 = DataFrame({"a":[1,2,3], "b":[4,5,6]})
    check_nulls(df1)

