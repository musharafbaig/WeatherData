import glob

m = []
a = []
max_temp_dict = {}
min_temp_dict = {}
min_humidity_dict = {}
max_humidity_dict = {}
complete_date_dict = {}
lines = []



def max_temp(temp_ist=[]):  # This func will return the Monthly Maximum Temperature and Date              #MAX TEMPERATURE
    month_max_temp= []
    max_list = []

    for i in range(len(temp_ist)):
        max_list.append(temp_ist[i][1])
        max_list = list(set(filter(None, max_list)))
    if not max_list:
        return 0
    else:
        max_list = [int(i) for i in max_list]
        maximum_num = max(max_list)
        temp_max = str(maximum_num)
        for item in range(len(temp_ist)):
            if temp_ist[item][1] == temp_max:
                month_max_temp.append(temp_ist[item][0])
                month_max_temp.append(temp_max)
                break
        return month_max_temp


def min_temp(temp_ist=[]):  # This func will return the Monthly Minimum Temperature and Date           #MIN TEMPERATURE
    month_min_temp= []
    min_list = []
    for i in range(len(temp_ist)):
        min_list.append(temp_ist[i][3])
        min_list = list(set(filter(None, min_list )))
    if not min_list:
        return 1000
    else:
        min_list = [int(i) for i in min_list ]
        minimum_num = min(min_list )
        temp_min = str(minimum_num)
        for item in range(len(temp_ist)):
            if temp_ist[item][3] == temp_min:
                month_min_temp.append(temp_ist[item][0])
                month_min_temp.append(temp_min)
                break
        return month_min_temp


def max_humidity(humidity_ist=[]):  # This func will return the Monthly Maximum Humidity and Date                #MAX HUMIDITY
    month_min_temp= []
    min_list = []
    for i in range(len(humidity_ist)):
        min_list.append(humidity_ist[i][7])
        min_list = list(set(filter(None, min_list )))
    if not min_list:
        return 0
    else:
        min_list = [int(i) for i in min_list ]
        minimum_num = max(min_list )
        temp_min = str(minimum_num)
        for item in range(len(humidity_ist)):
            if humidity_ist[item][7] == temp_min:
                month_min_temp.append(humidity_ist[item][0])
                month_min_temp.append(temp_min)
                break
        return month_min_temp


def min_humidity(humidity_ist=[]):  # This func will return the Monthly Minimum Humidity and Date                #MIN HUMIDITY
    month_min_temp= []
    min_list = []

    for i in range(len(humidity_ist)):
        min_list.append(humidity_ist[i][9])
        min_list = list(set(filter(None, min_list )))

    if not min_list:
        return 10000
    else:
        min_list = [int(i) for i in min_list ]
        minimum_num = min(min_list )
        temp_min = str(minimum_num)
        for item in range(len(humidity_ist)):
            if humidity_ist[item][9] == temp_min:
                month_min_temp.append(humidity_ist[item][0])
                month_min_temp.append(temp_min)
                break
        return month_min_temp


def year_hottest_days():
    print("Year      Date       Temp       [Report#2][Hottest Days]")
    print("-"*80)
    for i in max_temp_dict.keys():
        print("{0}    {1}    {2}".format(i,complete_date_dict[i],max_temp_dict[i]))

def annual_report():
    print("Year    MAXTemp    MINTemp    MAXHumidity    MINHumidity       [Report#1][Annual Report]")
    print("-"*80)
    for i in max_temp_dict.keys():
        print("{0}        {1}       {2}            {3}           {4}".format(i,max_temp_dict[i],min_temp_dict[i],max_humidity_dict[i],min_humidity_dict[i]))

# path =r"C:\Users\User\PycharmProjects\WeatherData\*.txt"
def main_function(path):
    files = glob.glob(path)
    for file in files:
        with open(file) as f:
            f.__next__()
            f.__next__()
            lines = f.readlines()
            lines = lines[:-1]
            lines = [l.strip('\n') for l in lines]
            # print(lines)
            a = []
            for i in lines:
                a.append(i.split(','))
                lines = a

        res_from_max_temp = max_temp(lines)
        res_from_min_temp = min_temp(lines)
        res_from_min_humidity = min_humidity(lines)
        res_from_max_humidity = max_humidity(lines)

        lines = []
        if res_from_max_temp != 0:
            date = res_from_max_temp[0]
            year = str(date)[:4]  # year will be the key in both dictionary; 1996:max_temp, 1996:1996-2-1
            month_max_temp = res_from_max_temp[1]
            if year in max_temp_dict.keys():
                i = int(month_max_temp)
                j = int(max_temp_dict[year])
                if i > j:
                    max_temp_dict[year] = month_max_temp
                    complete_date_dict[year] = date
                else:
                    pass
            else:
                max_temp_dict[year] = month_max_temp
                complete_date_dict[year] = date
        else:
            pass

        if res_from_min_temp != 1000:
            date = res_from_min_temp[0]
            year = str(date)[:4]  # year will be the key in dictionary; 1996:min_temp
            month_min_temp = res_from_min_temp[1]
            if year in min_temp_dict.keys():
                i = int(month_min_temp)
                j = int(min_temp_dict[year])
                if i < j:
                    min_temp_dict[year] = month_min_temp
                else:
                    pass
            else:
                min_temp_dict[year] = month_min_temp
        else:
            pass

        if res_from_min_humidity != 10000:
            date = res_from_min_humidity[0]
            year = str(date)[:4]  # year will be the key in dictionary; 1996:min_humidity
            month_min_humifity = res_from_min_humidity[1]
            if year in min_humidity_dict.keys():
                i = int(month_min_humifity)
                j = int(min_humidity_dict[year])
                if i < j:
                    min_humidity_dict[year] = month_min_humifity
                else:
                    pass
            else:
                min_humidity_dict[year] = month_min_humifity
        else:
            pass

        if res_from_max_humidity != 0:
            date = res_from_max_humidity[0]
            year = str(date)[:4]  # year will be the key in dictionary; 1996:min_humidity
            month_max_humifity = res_from_max_humidity[1]
            if year in max_humidity_dict.keys():
                i = int(month_max_humifity)
                j = int(max_humidity_dict[year])
                if i < j:
                    max_humidity_dict[year] = month_max_humifity
                else:
                    pass
            else:
                max_humidity_dict[year] = month_max_humifity
        else:
            pass

# MAIN PROGRAM

#C:\Users\User\PycharmProjects\WeatherData\*.txt
report_type = str(input("For Annual Report :1\nFor Hottest Days Report:2\nEnter Report Type: "))

if int(report_type )== 2:
    path = input("Enter Dir: ")
    main_function(path)
    year_hottest_days()
elif int(report_type )== 1:
    path = input("Path Data_Dir: ")
    main_function(path)
    annual_report()
else:
    print("weatherman[report# ] [data_dir]")



