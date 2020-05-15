# Convert State abbreviations to state names
from pandas import DataFrame

class MyFrame(DataFrame):

    def add_state_names(self):
    '''
    add a column of corresponding state names
    dict with abbrev/name mappings
    '''
        names_map = {"CA": "Cali", "CO": "Colo", "CT": "Conn"}
        self["name"] = self["abbrev"].map(names_map)

if __name__ == "__main__":
    myframe = MyFrame({"abbrev": ["CA", "CO", "CT", "DC", "TX"]})
    print(myframe.head())
    print(myframe.columns)

    myframe.add_state_names()
    print(myframe.head())
