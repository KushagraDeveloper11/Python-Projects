# with open("Day 15+\Day 25 Sporcle\weather_data.csv") as data_file:
#     data= data_file.readlines()
#     print(data)

# import csv
# with open("Day 15+\Day 25 Sporcle\weather_data.csv") as data_file:
#     data= csv.reader(data_file)
#     temperatures= []
#     for row in data:
#         if row[1]!= "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data= pandas.read_csv("Day 15+\Day 25 Sporcle\weather_data.csv")
print(data)
# temp_list= data["temp"].to_list()

# average= sum(temp_list)/len(temp_list)
# print(f"Average temp of {temp_list} is {average}")

# maxi= data["temp"].max()
# print(maxi)

# data_row= data[data.temp==maxi]
# print(data_row)

# monday= data[data.day=="Monday"]
# monday_temp= data[(data.temp-32)*9/5]
# print(monday)
# import pandas

# data_dict= {
#     'name': ['John', 'Mary'],
#     'age': [40,67],
# }

# data= pandas.DataFrame(data_dict)
# data.to_csv("new_sheet.csv")

# import pandas

# squirrel_data= pandas.read_csv("Day 15+\Day 25 Sporcle\Squirrel_Data.csv")
# gray_sq_cnt= len(squirrel_data[squirrel_data["Primary Fur Color"]== "Gray"])
# black_sq_cnt= len(squirrel_data[squirrel_data["Primary Fur Color"]== "Black"])
# red_sq_cnt= len(squirrel_data[squirrel_data["Primary Fur Color"]== "Cinnamon"])

# sq_dict={
#     "Fur color": ["Gray", "Cinnamon", "Black"],
#     "count": [gray_sq_cnt, red_sq_cnt, black_sq_cnt]
# }

# data = pandas.DataFrame(sq_dict)
# data.to_csv("Day 15+\Day 25 Sporcle\Squirrel_color_Data.csv")

# Alabama,139,-77
# Alaska,-204,-170
# Arizona,-203,-40
# Arkansas,57,-53
# California,-297,13
# Colorado,-112,20
# Connecticut,297,96
# Delaware,275,42
# Florida,220,-145
# Georgia,182,-75
# Hawaii,-317,-143
# Idaho,-216,122
# Illinois,95,37
# Indiana,133,39
# Iowa,38,65
# Kansas,-17,5
# Kentucky,149,1
# Louisiana,59,-114
# Maine,319,164
# Maryland,288,27
# Massachusetts,312,112
# Michigan,148,101
# Minnesota,23,135
# Mississippi,94,-78
# Missouri,49,6
# Montana,-141,150
# Nebraska,-61,66
# Nevada,-257,56
# New Hampshire,302,127
# New Jersey,282,65
# New Mexico,-128,-43
# New York,236,104
# North Carolina,239,-22
# North Dakota,-44,158
# Ohio,176,52
# Oklahoma,-8,-41
# Oregon,-278,138
# Pennsylvania,238,72
# Rhode Island,318,94
# South Carolina,218,-51
# South Dakota,-44,109
# Tennessee,131,-34
# Texas,-38,-106
# Utah,-189,34
# Vermont,282,154
# Virginia,234,12
# Washington,-257,193
# West Virginia,200,20
# Wisconsin,83,113
# Wyoming,-134,90