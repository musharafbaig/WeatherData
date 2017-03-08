"""

This project will display the results from weather data file

which are stored in project directory.

"""

import csv
import glob

max_temp_dict = {}  # Monthly maximum temp will store e.g 1996:45
min_temp_dict = {}  # Monthly minimum temp will store e.g 1996:3
min_humidity_dict = {}  # Monthly minimum humidity will store e.g 1996:31
max_humidity_dict = {}  # Monthly maximum temp will store e.g 1996:100
complete_date_dict = {}  # Complete date will store e.g 1996:1996-2-3


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
    for i in complete_date_dict.keys():
        print(str(i).rjust(6),
              str(max_temp_dict[i]).rjust(6),
              str(min_temp_dict[i]).rjust(6),
              str(max_humidity_dict[i]).rjust(8),
              str(min_humidity_dict[i]).rjust(9)
              )


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
    for i in complete_date_dict.keys():
        print(str(i).rjust(4),
              str(complete_date_dict[i]).rjust(12),
              str(max_temp_dict[i]).rjust(8)
              )


def max_temp_func(temp_list, date_list):
    """
    This func will return the Monthly Maximum Temperature and Date
    :param temp_list: one month temperatures
    :param date_list: temperatures with complete date
    :return: maximum temperature with complete date in list
    """
    # MAX TEMPERATURE
    if len(temp_list) == 0:
        return 0
    if len(temp_list) == 1:
        return list(zip(temp_list, date_list))
    return list(max(zip(temp_list, date_list)))


def min_func(list_1):
    """
    :param list_1: list to apply minimum function
    :return: string minimum number
    """
    if len(list_1) == 0:
        return 100
    if len(list_1) == 1:
        return list_1
    minimum = min(map(int,list_1))
    return str(minimum)


def max_finder_func(list_1):
    """

    :param list_1: list to apply max function
    :return: string minimum number
    """
    if len(list_1) == 0:
        return 0
    if len(list_1) == 1:
        return list_1
    maximum = max(map(int, list_1))
    return str(maximum)


def main_function():
    """
    This is Main function

    """
    files = glob.glob("*.txt")
    for file in files:
        MAXTemp = []
        MAXTempDate = []
        MINTemp = []
        MAXHumidity = []
        MINHumidity = []

        with open(file) as f:
            # skip first and last line in file
            read = csv.DictReader(f.readlines()[1:-1])
            # iterate over a file lines
            for row in read:
                if row:
                    # if row is not empty
                    if row['Max TemperatureC']:
                        MAXTemp.append(row['Max TemperatureC'])
                        MINTemp.append(row['Min TemperatureC'])
                        MAXHumidity.append(row['Max Humidity'])
                        MINHumidity.append(row[' Min Humidity'])
                        # if date format is PKT or PKST
                        if 'PKT' in row.keys():
                            MAXTempDate.append(row['PKT'])
                        else:
                            MAXTempDate.append(row['PKST'])
        # if file is empty iterate over next file
        if not MAXTemp:
            continue
        # these functions will return required results
        max_list = max_temp_func(MAXTemp, MAXTempDate)
        min_list = min_func(MINTemp)
        min_humidity = min_func(MINHumidity)
        max_humidity = max_finder_func(MAXHumidity)
        # max_list = [32,1996-12-1]
        max_temp = max_list[0]
        date = max_list[1]
        # Split the date so that we can use Year e.g 1996 as a key
        year = str(date)[:4]

        if year in complete_date_dict.keys():
            # If key:Year is already store in dictionary. So data of month is already stored

            if int(max_temp) > int(max_temp_dict[year]):
                # Compare the NewTemp with existed Temp
                # If Temp is greater than existed Temp.
                # Replace it with Temp and Date in both dictionaries
                # Remember: Year will be the key in all dictionaries
                max_temp_dict[year] = max_temp
                complete_date_dict[year] = date

            if int(min_list) < int(min_temp_dict[year]):
                # Compare the NewTemp with existed Temp
                # If NewTemp is less than existed Temp.
                # Replace it with NewTemp
                min_temp_dict[year] = min_list

            if int(max_humidity) > int(max_humidity_dict[year]):
                # Compare the NewHumidity with existed Humidity
                # If NewHumidity is greater than existed Humidity.
                # Replace it with NewHumidity
                max_humidity_dict[year] = max_humidity

            if int(min_humidity) < int(min_humidity_dict[year]):
                # Compare the NewHumidity with existed Humidity
                # If NewHumidity is less than existed Humidity.
                # Replace it with NewHumidity
                min_humidity_dict[year] = min_humidity

            # after all the condition continue
            continue

        else:
            # If key is not already exists.Add it in dictionary with Year as a key
            max_temp_dict[year] = max_temp
            complete_date_dict[year] = date
            min_temp_dict[year] = str(min_list)
            max_humidity_dict[year] = str(max_humidity)
            min_humidity_dict[year] = str(min_humidity)


report_type = str(input("For Annual Report :1\n"
                        "For Hottest Days Report:2\n"
                        "Enter Report Type: "
                        )
                  )

# Take input from user. What type of report to display
if int(report_type) == 2:
    main_function()
    year_hottest_days()

elif int(report_type) == 1:
    main_function()
    annual_report()

else:
    print("Usage:weatherman[report# ][data_dir]")
