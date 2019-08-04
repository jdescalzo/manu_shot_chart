"""

Manu Ginobili Shot Charts

"""

import matplotlib.pyplot as plt
import csv

filename = 'manu_shot_chart.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    for index, column_header in enumerate(header_row):
        print(index,column_header)

# FG% and 3P% by season
    seasons, field_goal_per, three_point_per = [], [], []
    field_attemps, three_attemps = [], []
    for row in reader:
        try:
            current_season = row[0]
            current_field_goal_per = int(float(row[10])*100)
            current_three_point_per = int(float(row[13])*100)
            current_field_attemps = int(row[9])
            current_three_attemps = int(row[12])
        except ValueError:
            print(current_season, 'missing data')
        else:
            seasons.append(current_season)
            field_goal_per.append(current_field_goal_per)
            three_point_per.append(current_three_point_per)
            field_attemps.append(current_field_attemps)
            three_attemps.append(current_three_attemps)

# Generate Carreer averages:
field_goal_avarage = field_goal_per.pop()
three_point_avarage = three_point_per.pop()

# Delete Carrer column from final data
del seasons[-1]
del field_attemps[-1]
del three_attemps[-1]

# Plot data
fig = plt.figure(dpi=128, figsize=(12, 6), tight_layout=True)
plt.scatter(seasons, field_goal_per, c='red', s=field_attemps)
plt.scatter(seasons, three_point_per, c='blue', s=three_attemps)
plt.axhline(field_goal_avarage, c='red', alpha=0.3, label='FG Career avg.', ls='--')
plt.axhline(three_point_avarage, c='blue', alpha=0.3, label='3P Career avg.', ls='--')

# Plot settings
plt.title("Manu Ginóbili Career FG% and 3P%", fontsize=28)
plt.xlabel('Season', fontsize=18)
plt.ylabel('Shot %', fontsize=18)
plt.tick_params(axis='x', labelsize=9)
plt.ylim(0, 60)
plt.legend(loc=4)
plt.text(0, 1, 'Data from basketball-reference.com', fontsize=8)
