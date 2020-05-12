# Convert State abbreviations to state names
from pandas import DataFrame

class DataProcessor():
    def __init__(self, my_df): # constructor
        self.df = my_df

    def add_state_names(self):
    # add a column of corresponding state names
    # dict with abbrev/name mappings
        names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}
        self.df["name"] = self.df["abbrev"].map(names_map)
        return self.df

if __name__ == "__main__":
    df = DataFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(df.head())

    processor = DataProcessor(df)
    print(processor.df.head())

    processor.add_state_names()
    print(processor.df.head())
