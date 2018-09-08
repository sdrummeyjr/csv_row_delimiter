"""
This function takes a csv file that has various data sets that are split up by a row of some character(s). The function
returns a list of lists made up of the separated data sets. From there, the data can be cleaned further, turned into a
pandas dataframe, or whatever. The key is that the data is now identified and in an easy, basic format to work with and
manage.

There are other methods to iterate through a csv file by row to separate data, including pandas functionality. I built
my own in an attempt to utilize basic Python data structures. The only import used is the csv library.
"""
import csv


def row_delim(file, row_delimiter, csv_delimiter=','):

    try:
        with open(file) as csv_file:

            # import data from csv as a list to utilize indexes
            # row_delim can take a custom character for csv.reader to delimit but defaults to ',' which is most common
            data = list(csv.reader(csv_file, delimiter=csv_delimiter))

            # identify the location of the beginning and the end of each data set
            count = 0
            locations = []
            for row in data:
                count += 1
                if row_delimiter in row:
                    locations.append(count)
            file_range = []
            ind = 0
            for index, loc in enumerate(locations):
                if index == 0:
                    file_range.append((index, loc))
                else:
                    file_range.append((locations[ind]+1, loc))
                    ind += 1

            # iterate through the list of data sets in the csv and separate them into a list of lists
            new_rows = []
            for item in file_range:
                if item[0] == 0:
                    row = data[:item[1]-1]
                    new_rows.append(row)
                else:
                    row = data[item[0]-1:item[1]-1]
                    new_rows.append(row)

            return new_rows

    # handle FileNotFoundError with custom direction for user
    except FileNotFoundError as err:
        print(f"The following error occurred: {err}\n"
              "Confirm that the file exists or that the location provided is correct")
