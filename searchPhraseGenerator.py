import pandas as pd


class searchPhraseGenerator:

    #returns the row in database with the respective crop name
    def find_row(crop_name):
        
        crop_name = crop_name.lower()
        crop_data = pd.read_excel('Crop_Data.xlsx')
        column_name = 'Crop Name'
        search_result = crop_data.loc[crop_data[column_name] == crop_name]
        return search_result
    

    #compares the readings of the given attribute with the ideal readings

    def compare_attribute(attribute_name, attribute_value, crop_values):
        #stores generated search Phrases in an array 
        search_phrases = []
        # finds the corresponding column index for the attribute
        column1_index = 1
        column2_index = 2
        if attribute_name == 'pH':
            column1_index = 1
            column2_index = 2
        elif attribute_name == 'Temp':
            column1_index = 3
            column2_index = 4
        else :
            column1_index = 5
            column2_index = 6

        #assigns the lower and upper values for the ideal range
        attribute_lower_value = float(crop_values.iloc[:, column1_index])
        attribute_upper_value = float(crop_values.iloc[:, column2_index])

        # print the generate search phrase
        if(attribute_value < attribute_lower_value):
            search_phrases.append("LOW " + attribute_name)

        elif(attribute_value > attribute_upper_value):
            search_phrases.append("HIGH " + attribute_name)
        else :
            search_phrases.append("PERFECT "+ attribute_name)

        return search_phrases