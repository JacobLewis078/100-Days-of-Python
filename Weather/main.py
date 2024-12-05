# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             degree = int(row[1])
#             temperatures.append(degree)
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # temp_max = data["temp"].max()
# # print(temp_max)
# #
# # print(data[data.temp == temp_max])
# monday = data[data.day == "Monday"]
# temp = (monday.temp * (9/5)) + 32
# print(temp)
# print(monday)

squirrel_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
new_data = squirrel_data[["Primary Fur Color", "Unique Squirrel ID"]].groupby("Primary Fur Color").count()
print(new_data)

## Alternative Method
grey_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("Squirrel_fur.csv")
print(data_dict)
