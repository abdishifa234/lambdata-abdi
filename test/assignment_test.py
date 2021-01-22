import unittest
from lambdata-abdi.helper_functions.py import add_state_names_column

# from lambdata-abdi.my_mode.py import enlarge

class Testhelper(unittest.TestCase):

    def test_add_state_names_column(self):
        
        df = DataFrame({"abrev": ["CA", "CO", "CT", "DC", "TX"]})
        self.assertEqual(len(df.columns),1)
        self.assertEqual(list(df.columns),['abbrev'])
        self.assertEqual(list(df.iloc[0],'CA')

        

        mapped_df=add_state_names_column(df)

        
        self.assertEqual(len(df.columns),2)
        self.assertEqual(list(mapped_df.columns),['abbrev','name'])
        self.assertEqual(list(df.iloc[0],'CA')
        self.assertEqual(list(df.iloc[0]['name'],'Cali')

        # add_state_names_column(my_df)
        # print(mapped_df.head())

        

if __name__ == '__main__':
    unittest.main() #invoking all of our class's methods
    