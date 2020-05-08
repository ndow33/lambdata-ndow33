

#  Convert State abbreviations to state names
from pandas import DataFrame


def add_state_names(my_df):
    """
    Adds a column of state names to accompany a corresponding column of state abbreviation.

    Params:
        my_df (pandas.DataFrame) has a column called "abbrev" with state abbreviations

    Returns:
        Copy of the original dataframe with another column
    """
    #  add a column of corresponding state names
    #  dict with abbrev/name mappings
    #  new comment
    
    new_df = my_df.copy()cd
    names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}
    new_df["name"] = new_df["abbrev"].map(names_map)
    return new_df

if __name__ == "__main__":
    df = DataFrame({"abbrev":["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())

    df2 = add_state_names(df)
    print(df2)