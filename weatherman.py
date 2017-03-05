
"""

This project will display the results from weather data file

which are stored in project directory.

"""


import csv
import glob


# Initializing the lists and dictionaries

max_temp_dict = {} # Year is key and MAXTemp is value e.g 1996 : 46
min_temp_dict = {} # Year is key and MINTemp is value e.g 1996 : 4
min_humidity_dict = {} # Year is key and MAXHumidity is value e.g 1996 : 74
max_humidity_dict = {} # Year is key and MINHumidity is value e.g 1996 : 14
complete_date_dict = {} # Year is key and Complete Date is value e.g 1996 : 1996-12-2


def max_temp(temp):
    """
    This func will return the Monthly Maximum Temperature and Date
    :param temp: list from which we will extract MAXTemp value and Date
    :return: MAXTemp with it's Date in a list
    """
    # MAX TEMPERATURE

    month_max_temp = []
    max_list = []

    # iterate over list and access the sublist's MAXTemp element and store it in separate list
    for i in range(len(temp)):
        max_list.append(temp[i][1])
    # convert the list into Integer
    max_list = list(map(int,set(filter(None, max_list))))
    if not max_list:
        # if there is no MAXtemp value in list then return 0
         return 0
    else:
        # find maximum value in list
        maximum_num = max(max_list)
        temp_max = str(maximum_num)
        # maximum temperature we get is of one month.
        # append the maximum temp and it's date in month_max_list and return list
        for item in range(len(temp)):
            if temp[item][1] == temp_max:
                month_max_temp.append(temp[item][0])
                month_max_temp.append(temp_max)
                break
        return month_max_temp


def min_temp(temp):
    """
    This func will return the Monthly Minimum Temperature and it's Date
    :param temp: list from which we will extract MINTemp value and Date
    :return: MINTemp with it's Date in a list
    """

    # MIN TEMPERATURE

    month_min_temp = []
    min_list = []
    # iterate over list and access the sublist's MINTemp element and store it in separate list
    for i in range(len(temp)):
        min_list.append(temp[i][3])
    # convert the list into Integer
    min_list = list(map(int,set(filter(None, min_list))))
    if not min_list:
        # if there is no MINTemp value in list then return 1000
        return 1000
    else:
        # find minimum value in list
        minimum_num = min(min_list)
        temp_min = str(minimum_num)
        # minimum temperature we get is of one month.
        # append the minimum temp and it's date in month_min_list and return list
        for item in range(len(temp)):
            if temp[item][3] == temp_min:
                month_min_temp.append(temp[item][0])
                month_min_temp.append(temp_min)
                break
        return month_min_temp


def max_humidity(humidity):
    """
    This func will return the Monthly Maximum Humidity and Date
    :param humidity:list from which we will extract MAXHumidity value and Date
    :return: MAXHumidity with it's Date in a list

    """
    month_max_humidity = []
    max_list = []
    for i in range(len(humidity)):
        # iterate over list and access the sublist's MAXHumidity element and store it in separate list
        max_list.append(humidity[i][7])
        # convert the list into Integer
    max_list = list(map(int,set(filter(None, max_list))))
    if not max_list:
        # if there is no MAXHumidity value in list then return 0
        return 0
    else:
        # find maximum value in list
        maximum_num = max(max_list)
        temp_min = str(maximum_num)
        # maximum temperature we get is of one month.
        # append the maximum humidity and it's date in month_max_list and return list
        for item in range(len(humidity)):
            if humidity[item][7] == temp_min:
                month_max_humidity.append(humidity[item][0])
                month_max_humidity.append(temp_min)
                break
        return month_max_humidity


def min_humidity(humidity):
    """
    This func will return the Monthly Minimum Humidity and Date

    :param humidity: list from which we will extract MAXHumidity value and Date
    :return: MINHumidity with it's Date in a list
    """
    # MIN HUMIDITY

    month_min_humidity = []
    min_list = []

    for i in range(len(humidity)):
        # iterate over list and access the sublist's MAXHumidity element and store it in separate list
        min_list.append(humidity[i][9])
        # convert the list into Integer
    min_list = list(map(int, set(filter(None, min_list))))

    if not min_list:
        # if there is no MINHumidity value in list then return 1000
        return 10000
    else:
        # find minimum value in list
        minimum_num = min(min_list )
        temp_min = str(minimum_num)
        # minimum temperature we get is of one month.
        # append the minimum humidity and it's date in month_min_list and return list
        for item in range(len(humidity)):
            if humidity[item][9] == temp_min:
                month_min_humidity.append(humidity[item][0])
                month_min_humidity.append(temp_min)
                break
        return month_min_humidity


def year_hottest_days():
    """
    it will show the the Hottest days with year and complete date

    """
    print(str("Year").rjust(4),
          str("Date").rjust(10),
          str("Temp").rjust(11),
          "[Report#2][Hottest Days Report]".rjust(8)
          )
    print("-"*80)
    # iterate over dictionary key @Year e.g 1996 and display it's value.Uses same key for two dictionaries
    # e.g 1996:1996-12-1 and 1996:49
    for i in max_temp_dict.keys():
        print(str(i).rjust(4),
              str(complete_date_dict[i]).rjust(12),
              str(max_temp_dict[i]).rjust(8)
              )


def annual_report():
    """
    It will show the annual report to the user

    """

    print(str("Year").rjust(7),
          str("MAXTemp").rjust(7),
          str("MINTemp").rjust(7),
          str("MAXHumidity").rjust(7),
          str("MINHumidity").rjust(7),
          "[Report#1][Annual Report]".rjust(8)
          )
    print("-"*80)
    # iterate over dictionary key @Year e.g 1996 and display it's value.Uses same key for all dictionaries
    for i in max_temp_dict.keys():
        print(str(i).rjust(6),
              str(max_temp_dict[i]).rjust(6),
              str(min_temp_dict[i]).rjust(6),
              str(max_humidity_dict[i]).rjust(8),
              str(min_humidity_dict[i]).rjust(9)
              )


def main_function(path):
    """
    Performing as a Main Function which will call all the other functions
    :param path: default directory of the Project where all weather files are located

    """

    # Fetch all files in directory
    files = glob.glob(path)
    for file in files:
        # iterate over all files
        lines = []
        L = []
        with open(file) as f:
            # Skip the first two lines
            f.__next__()
            f.__next__()
            # Read all from a file and store it in List @lines
            lines = csv.reader(f)
            # Iterate over each line in a file. Append each line in List @L
            for row in lines:
                L.append(row)
            # Emit the last line
            L = L[:-1]
        # Send this List @L to all function to get the required result.
        res_from_max_temp = max_temp(L)
        res_from_min_temp = min_temp(L)
        res_from_min_humidity = min_humidity(L)
        res_from_max_humidity = max_humidity(L)

        # If result from function is not 0
        if res_from_max_temp != 0:
            # e.g result = [1996-12-1,32]
            date = res_from_max_temp[0]
            # Split the date so that we can use Year e.g 1996 as a key
            year = str(date)[:4]
            # Store the MAXTemp per month
            month_max_temp = res_from_max_temp[1]
            if year in max_temp_dict.keys():
                # If key:Year is already store in dictionary
                i = int(month_max_temp)
                j = int(max_temp_dict[year])
                # Compare the Temp with existed Temp
                if i > j:
                    # If Temp is greater than existed Temp.
                    # Replace it with Temp and Date in both dictionaries
                    # Year will be the key in both dictionaries
                    max_temp_dict[year] = month_max_temp
                    complete_date_dict[year] = date
                else:
                    # If Temp is less than existed Temp.
                    pass
            else:
                # If key is not already exist.Add it in both dictionaries with Year as a key
                max_temp_dict[year] = month_max_temp
                complete_date_dict[year] = date
        else:
            # If the result get from function is 0
            pass

        # If result from function is not None
        if res_from_min_temp != 1000:
            # e.g result = [1996-12-1,32]
            date = res_from_min_temp[0]
            # Split the date so that we can use Year e.g 1996 as a key
            year = str(date)[:4]
            # Store the MINTemp per month
            month_min_temp = res_from_min_temp[1]
            if year in min_temp_dict.keys():
                # If key(Year) is already store in dictionary
                i = int(month_min_temp)
                j = int(min_temp_dict[year])
                # Compare the NewTemp with existed Temp
                if i < j:
                    # If NewTemp is less than existed Temp.
                    # Replace it with NewTemp
                    min_temp_dict[year] = month_min_temp
                else:
                    # If Temp is greater than existed Temp.
                    pass
            else:
                # If key is not already exist.Add it in dictionary with Year as a key
                min_temp_dict[year] = month_min_temp
        else:
            # If the result get from function is None
            pass

        # If result from function is not None
        if res_from_min_humidity != 10000:
            # e.g result = [1996-12-1,32]
            date = res_from_min_humidity[0]
            # Split the date so that we can use Year e.g 1996 as a key
            year = str(date)[:4]
            # Store the MINHumidity per month
            month_min_humidity = res_from_min_humidity[1]
            if year in min_humidity_dict.keys():
                # If key(Year) is already store in dictionary
                i = int(month_min_humidity)
                j = int(min_humidity_dict[year])
                # Compare the NewHumidity with existed Humidity
                if i < j:
                    # If NewHumidity is less than existed Humidity.
                    # Replace it with NewHumidity
                    min_humidity_dict[year] = month_min_humidity
                else:
                    # If NewHumidity is greater than existed Humidity.
                    pass
            else:
                # If key is not already exist.Add it in dictionary with Year as a key
                min_humidity_dict[year] = month_min_humidity
        else:
            # If result from function is None
            pass

        # If result from function is not 0
        if res_from_max_humidity != 0:
            # e.g result = [1996-12-1,32]
            date = res_from_max_humidity[0]
            # Split the date so that we can use Year e.g 1996 as a key
            year = str(date)[:4]
            # Store the MAXHumidity per month
            month_max_humidity = res_from_max_humidity[1]
            if year in max_humidity_dict.keys():
                # If key(Year) is already store in dictionary
                i = int(month_max_humidity)
                j = int(max_humidity_dict[year])
                # Compare the NewHumidity with existed Humidity
                if i < j:
                    # If NewHumidity is greater than existed Humidity.
                    # Replace it with NewHumidity
                    max_humidity_dict[year] = month_max_humidity
                else:
                    # If NewHumidity is less than existed Humidity.
                    pass
            else:
                # If key is not already exist.Add it in dictionary with Year as a key
                max_humidity_dict[year] = month_max_humidity
        else:
            # If result from function is None
            pass

# MAIN PROGRAM

report_type = str(input("For Annual Report :1\n"
                        "For Hottest Days Report:2\n"
                        "Enter Report Type: "
                        )
                  )
# Take input from user. What type of report to display
path = "*.txt"
if int(report_type) == 2:
    main_function(path)
    year_hottest_days()

elif int(report_type) == 1:
    main_function(path)
    annual_report()

else:
    print("weatherman[report# ][data_dir]")



