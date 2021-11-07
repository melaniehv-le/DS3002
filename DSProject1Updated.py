import pandas as pd
import csv
import json
import time

#Operation 1: Retrieve a remote data file by URL, my data came from Data.gov, provided in the project instructions on the bottom page as a resource
df = pd.read_csv('https://query.data.world/s/tlvy3lwflzfeopkma3jpi5e5cubeb3')
#print(df)

#Removing "Region" column from CSV data file
#Operation Number 3: Modify number of columns, this reduces the columns by 1 after removing the Region column
#This data set included what region of New York the death counts came from, but removing this data would be useful if trying to look at counts from New York State as a whole
df.drop('Region', inplace=True, axis=1)
#print(df)

#Also imported the data files into a local file
csvFilePath = r'/Users/melaniele/Documents/DSProject1/vital-statistics-suicide-deaths-by-age-group-race-ethnicity-resident-county-region-and-gender-beginn-1.csv'
jsonFilePath = r'/Users/melaniele/Documents/DSProject1/vital-statistics-suicide-deaths-by-age-group-race-ethnicity-resident-county-region-and-gender-beginn-1.csv'

#Two methods to convert CSV to JSON file
#Operation Number 2: Converts the general format and data structure of the data source (from CSV to JSON)
newjson = df.to_json("/Users/melaniele/Documents/DSProject1/vital-statistics-suicide-deaths-by-age-group-race-ethnicity-resident-county-region-and-gender-beginn-1.csv")
#print(newjson)

#Defines a function that converts the CSV file to JSON
def csv_to_json(csvFilePath, jsonFilePath):
    jsonArray = []

    # read csv file
    with open(csvFilePath, encoding='utf-8') as csvf:
        # load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf)

        # convert each csv row into python dict
        for row in csvReader:
            # add this python dict to json array
            jsonArray.append(row)

    # convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonString = json.dumps(jsonArray, indent=4)
        jsonf.write(jsonString)

csv_to_json(csvFilePath, jsonFilePath)

#Operation Number 5: Generating summary of file including number of records and number of columns
#Row index starts at 0, column index starts at 1
rowcount=len(df.axes[0])
colcount=len(df.axes[1])
print("Number of Rows: "+str(rowcount))
print("Number of Columns: "+str(colcount))
print(df.columns)
