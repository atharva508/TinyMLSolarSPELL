#This class helps in searching through an excel file for relevant files for farmers in Rwanda, based on the intermediate search phrases that are generated!
import pandas as pd


class searchPhraseGenerator:

    #returns the row in database with the respective crop name
    
    def find_row(crop_name):

      crop_name = crop_name.lower()
      crop_data = pd.read_excel('/content/Crop_Data.xlsx')
      column_name = 'Crop Name'
      search_result = crop_data.loc[crop_data[column_name] == crop_name]
      return search_result

    

   #compares the readings of the given attribute with the ideal readings

    def compare_attribute(attribute_name, attribute_value, crop_values):

      # finds the corresponding column index for the attribute
      column1_index = 1
      column2_index = 2
      if attribute_name == 'pH':
        column1_index = 1
        column2_index = 2
      elif attribute_name == 'Temperature':
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
        return("LOW " + attribute_name)

      elif(attribute_value > attribute_upper_value):
        return("HIGH " + attribute_name)
      else :
        return("PERFECT "+ attribute_name)
    
    #combines the helper functions to generate an intermediate function
    def generate_intermediate_search_phrase(crop_name, ph_value, temp_value, vmc_value):
      crop_ideal_reading = find_row(crop_name)
      searchPhrase = []
      searchPhrase.append(compare_attribute('pH',ph_value,crop_ideal_reading)) #compares the pH readings
      searchPhrase.append(compare_attribute('Temperature',temp_value,crop_ideal_reading)) #compares the temperature readings
      searchPhrase.append(compare_attribute('VMC',vmc_value,crop_ideal_reading)) #compares the vmc readings
      searchPhrase.append(compare_attribute('moisture',vmc_value,crop_ideal_reading)) #compares the moisture readings
      return searchPhrase

    #searches through the keyword attribute in excel file for the given phrase
    def searchDB(phrase):
      keyword_data = pd.read_excel('/content/keyword3.xlsx')
      keyword_data.dropna()
      column_name = 'Keywords'
      subset_data = keyword_data[keyword_data[column_name].str.contains(phrase, na=False,case=False)]
      return subset_data
      
    #MAIN FUNCTION
    #returns all the file names (in a list) that have relevant articles
    def getFiles(crop,ph,temp,vmc):
      list_of_phrases = generate_intermediate_search_phrase(crop,ph,temp,vmc)
      list_of_phrases.append(crop)
      files = pd.DataFrame()
    # for each search phrase it returns rows that have those keywords
      for curr_phrase in list_of_phrases:
        db=searchDB(curr_phrase)
        files = pd.concat([files, db], ignore_index=True)

    #gets the count of each file in the list
      counts = files['FileName'].value_counts()

    #adds the files to the result list in descending order
      list_of_files = []
      for attribute, count in counts.items():
          #print(f"{attribute}: {count}")
          list_of_files.append(f"{attribute}")

      return list_of_files


