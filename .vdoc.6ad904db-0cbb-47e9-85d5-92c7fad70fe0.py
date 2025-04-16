# type: ignore
# flake8: noqa
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#
#
#
#
#
#claire path
df1 = pd.read_csv('Data/catapult season 1.csv')
df2 = pd.read_csv('Data/catapult season 2.csv')
#df1 = pd.read_csv("./season1.csv")
#df2 = pd.read_csv("./season2.csv")
#
#
#
#
#
#
#
df1 = df1[['Date', 'About', 'Position', 'Period Number', 'Period', 'Total Player Load', 'Player Load Per Minute', 'IMA Accel Total', 
           'IMA Decel Total', 'IMA Jump Count Low Band', 'IMA Jump Count Med Band', 'IMA Jump Count High Band', 'Explosive Efforts']]

df2 = df2[['Date', 'About', 'Position', 'Period Number', 'Period', 'Total Player Load', 'Player Load Per Minute', 'IMA Accel Total', 
           'IMA Decel Total', 'IMA Jump Count Low Band', 'IMA Jump Count Med Band', 'IMA Jump Count High Band', 'Explosive Efforts']]

# make sure columns dropped properly
print("df1:", df1.columns)
print("df2:", df2.columns)
#
#
#
#
#
#
#
print("Season1 Missings:")
for col in df1.columns:
    total = len(df1)
    missing = df1[col].isnull().sum()
    percent = (missing / total) * 100
    print(col , ":", round(percent, 2))

print("\nSeason2 Missings:")
for col in df2.columns:
    total = len(df2)
    missing = df2[col].isnull().sum()
    percent = (missing / total) * 100
    print(col , ":", round(percent, 2))
#
#
#
#
#
#
#
# print(df1['Date'].unique() , "\n", df1['Date'].dtype) # -> all objects, no duplicates
# print(df1['About'].unique() , "\n", df1['About'].dtype) # -> all objects, no duplicates
print(df1['Position'].unique() , "\n", df1['Position'].dtype) # -> all objects, no duplicates
#
#
#
#
#
# Warm Up, Period 1, Period 2, Mvmt Prep, Movement Prep
krows = []

for i in range(len(df1)):
    value = str(df1.loc[i, 'Period'])
    if 'Warm Up' in value or 'Period 1' in value or 'Period 2' in value or 'Mvmt Prep' in value or 'Movement Prep' in value:
        krows.append(i)
df1 = df1.loc[krows].reset_index(drop=True)
df1['Period'] = df1['Period'].replace("Mvmt Prep", "Movement Prep")
#
#
#
#
#
# delete rows with "Scrimmage"
drows = []

for i in range(len(df1)):
    value = str(df1.loc[i, 'Period'])
    if 'Scrimmage' in value:
        drows.append(i)
    if 'Drill' in value:
        drows.append(i)

df1.drop(index=drows, inplace=True)
df1.reset_index(drop=True, inplace=True)

df1['Period'].value_counts()
#
#
#
#
#
# Warm Up = 1 , Period 1 = 2, Period 2 = 3, Movement Prep = 4
# cleaning Warm Up
if "1. Warm Up" in df1['Period'].values:
    df1['Period'] = df1['Period'].replace("1. Warm Up", "Warm Up")
if "2. Warm Up" in df1['Period'].values:
    df1['Period'] = df1['Period'].replace("2. Warm Up", "Warm Up")
    df1['Period Number'] = df1['Period Number'].replace(2, 1)
if "7. Warm Up" in df1['Period'].values:
    df1['Period'] = df1['Period'].replace("7. Warm Up", "Warm Up")
    df1['Period Number'] = df1['Period Number'].replace(7, 1)

# cleaning Period 1
if "2. Period 1" in df1['Period'].values:
    df1['Period'] = df1['Period'].replace("2. Period 1", "Period 1")
if "3. Period 1" in df1['Period'].values:
    df1['Period'] = df1['Period'].replace("3. Period 1", "Period 1")
    df1['Period Number'] =df1['Period Number'].replace(3, 2)

# cleaning Period 2
if "2. Period 2" in df1['Period'].values:
    df1['Period'] = df1['Period'].replace("2. Period 2", "Period 2")
    df1['Period Number'] = df1['Period Number'].replace(2, 3)
if "4. Period 2" in df1['Period'].values:
    df1['Period'] = df1['Period'].replace("4. Period 2", "Period 2")
    df1['Period Number'] = df1['Period Number'].replace(4, 3)
if "3. Period 2" in df1['Period'].values:
    df1['Period'] = df1['Period'].replace("3. Period 2", "Period 2")
    
# cleaning Movement Prep
if "1. Mvmt Prep" in df1['Period'].values:
    df1['Period'] = df1['Period'].replace("1. Mvmt Prep", "Movement Prep")
    df1['Period Number'] = df1['Period Number'].replace(1, 4)
if "2. Mvmt Prep" in df1['Period'].values:
    df1['Period'] = df1['Period'].replace("2. Mvmt Prep", "Movement Prep")
    df1['Period Number'] = df1['Period Number'].replace(2, 4)
if "1. Movement Prep" in df1['Period'].values:
    df1['Period'] = df1['Period'].replace("1. Movement Prep", "Movement Prep")
    df1['Period Number'] = df1['Period Number'].replace(1, 4) 
if "2. Movement Prep" in df1['Period'].values:
    df1['Period'] = df1['Period'].replace("2. Movement Prep", "Movement Prep")
    df1['Period Number'] = df1['Period Number'].replace(2,4)
else:
    df1['Period'] = df1['Period']

print(df1['Period'].value_counts())
#
#
#
#
#
# # print(df1['Total Player Load'].value_counts(), "\n", df1['Total Player Load'].dtype) # -> all floats
# # print(df1['Player Load Per Minute'].unique(), "\n", df1['Player Load Per Minute'].dtype) # -> all floats w/ one decimal place
# # print(df1['IMA Accel Total'].unique(), "\n", df1['IMA Accel Total'].dtype) # -> all ints, no duplicates
# # print(df1['IMA Decel Total'].unique(), "\n", df1['IMA Decel Total'].dtype) # -> all ints, no duplicates 
# print(df1['IMA Jump Count Low Band'].unique(), "\n", df1['IMA Jump Count Low Band'].dtype) # -> all ints, no duplicates
# print(df1['IMA Jump Count Med Band'].unique(), "\n", df1['IMA Jump Count Med Band'].dtype) # -> all ints, no duplicates
# print(df1['IMA Jump Count High Band'].unique(), "\n", df1['IMA Jump Count High Band'].dtype) # -> all ints, no duplicates
print(df1['Explosive Efforts'].unique(), "\n", df1['Explosive Efforts'].dtype) # -> all ints, no duplicates
#
#
#
#
#
#
#
# print(df2['Date'].unique() , "\n", df2['Date'].dtype) # -> all objects, no duplicates
# print(df2['About'].unique() , "\n", df2['About'].dtype) # -> all objects, no duplicates
print(df2['Position'].unique() , "\n", df2['Position'].dtype) # -> all objects, no duplicates
#
#
#
#
#
# Warm Up, Period 1, Period 2, Mvmt Prep, Movement Prep
krows = []

for i in range(len(df2)):
    value = str(df2.loc[i, 'Period'])
    if 'Warm Up' in value or 'Period 1' in value or 'Period 2' in value or 'Mvmt Prep' in value or 'Movement Prep' in value:
        krows.append(i)
df2 = df2.loc[krows].reset_index(drop=True)
df2['Period'] = df2['Period'].replace("Mvmt Prep", "Movement Prep")
#
#
#
#
#
# delete rows with "Scrimmage"
drows = []

for i in range(len(df2)):
    value = str(df2.loc[i, 'Period'])
    if 'Scrimmage' in value:
        drows.append(i)
    if 'Drill' in value:
        drows.append(i)

df2.drop(index=drows, inplace=True)
df2.reset_index(drop=True, inplace=True)

df2['Period'].value_counts()
#
#
#
#
#
# Warm Up = 1 , Period 1 = 2, Period 2 = 3, Movement Prep = 4
# cleaning Warm Up
if "1. Warm Up" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("1. Warm Up", "Warm Up")
if "2. Warm Up" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("2. Warm Up", "Warm Up")
    df2['Period Number'] = df2['Period Number'].replace(2, 1)
if "4. Warm Up" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("4. Warm Up", "Warm Up")
    df2['Period Number'] = df2['Period Number'].replace(4, 1)
if "3. Warm Up" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("3. Warm Up", "Warm Up")
    df2['Period Number'] = df2['Period Number'].replace(3, 1)

# cleaning Period 1
if "2. Period 1" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("2. Period 1", "Period 1")
if "3. Period 1" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("3. Period 1", "Period 1")
    df2['Period Number'] =df2['Period Number'].replace(3, 2)
if "1. Period 1" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("1. Period 1", "Period 1")
    df2['Period Number'] =df2['Period Number'].replace(1, 2)
if "8. Period 1" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("8. Period 1", "Period 1")
    df2['Period Number'] =df2['Period Number'].replace(8, 2)

# cleaning Period 2
if "2. Period 2" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("2. Period 2", "Period 2")
    df2['Period Number'] = df2['Period Number'].replace(2, 3)
if "4. Period 2" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("4. Period 2", "Period 2")
    df2['Period Number'] = df2['Period Number'].replace(4, 3)
if "3. Period 2" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("3. Period 2", "Period 2")
if "5. Period 2" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("5. Period 2", "Period 2")
    df2['Period Number'] = df2['Period Number'].replace(5, 3)
if "9. Period 2" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("9. Period 2", "Period 2")
    df2['Period Number'] = df2['Period Number'].replace(9, 3)
    
# cleaning Movement Prep
if "1. Movement Prep" in df2['Period'].values:
    df2['Period'] = df2['Period'].replace("1. Movement Prep", "Movement Prep")
    df2['Period Number'] = df2['Period Number'].replace(1, 4)

else:
    df2['Period'] = df2['Period']

print(df2['Period'].value_counts())
#
#
#
#
#
# print(df2['Total Player Load'].value_counts(), "\n", df2['Total Player Load'].dtype) # -> all floats
# print(df2['Player Load Per Minute'].unique(), "\n", df2['Player Load Per Minute'].dtype) # -> all floats w/ one decimal place
# print(df2['IMA Accel Total'].unique(), "\n", df2['IMA Accel Total'].dtype) # -> all ints, no duplicates
# print(df2['IMA Decel Total'].unique(), "\n", df2['IMA Decel Total'].dtype) # -> all ints, no duplicates 
# print(df2['IMA Jump Count Low Band'].unique(), "\n", df2['IMA Jump Count Low Band'].dtype) # -> all ints, no duplicates
# print(df2['IMA Jump Count Med Band'].unique(), "\n", df2['IMA Jump Count Med Band'].dtype) # -> all ints, no duplicates
# print(df2['IMA Jump Count High Band'].unique(), "\n", df2['IMA Jump Count High Band'].dtype) # -> all ints, no duplicates
print(df2['Explosive Efforts'].unique(), "\n", df2['Explosive Efforts'].dtype) # -> all ints, no duplicates
#
#
#
#
#
def hist_stat(col, seasondf):
    # season/column specific:
    color = ''
    season = ''
    if seasondf.equals(df1):
        season = 'Season 1'
        color = 'purple'
    elif seasondf.equals(df2):
        season = 'Season 2'
        color = 'green'
    else:
        season = 'Unknown Season'
        color = 'blue'

    # plot variable statistics
    plt.hist(col, bins=30, color=color, alpha=0.5, edgecolor='black')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    title = season + " " + col.name + " " + 'Distribution'
    plt.title(title)
    plt.xlabel(col.name)
    plt.show()

    # print numerical statistics
    mean = np.mean(col)
    std = np.std(col)
    min = np.min(col)
    max = np.max(col)
    percentiles = np.percentile(col, [25, 50, 75])
    print("mean:", mean, "\nstd:", std, "\nmin:", min, "\nmax:", max, "\nPercentiles:", percentiles)

def categorical_stats(col, dataframe):
    color = ''
    season = ''
    if dataframe.equals(df1):
        season = 'Season 1'
        color = 'purple'
    elif dataframe.equals(df2):
        season = 'Season 2'
        color = 'green'
    else:
        season = 'Unknown Season'
        color = 'blue'

    plt.hist(col, color=color, edgecolor='black')
    plt.gca().spines['top'].set_visible(False)
    plt.gca().spines['right'].set_visible(False)
    title = season + " " + col.name
    plt.title(title)
    plt.show()
#
#
#
#
hist_stat(df1['Total Player Load'], df1)
hist_stat(df2['Total Player Load'], df2)
#
#
#
#
#
#
#
#
#
#
#
#
#
hist_stat(df1['Player Load Per Minute'], df1)
hist_stat(df2['Player Load Per Minute'], df2)
#
#
#
#
#
#
hist_stat(df1['IMA Accel Total'], df1)
hist_stat(df2['IMA Accel Total'], df2)
#
#
#
#
hist_stat(df1['IMA Decel Total'], df1)
hist_stat(df2['IMA Decel Total'], df2)
#
#
#
#
#
#
#
#
hist_stat(df1['IMA Jump Count Low Band'], df1)
hist_stat(df2['IMA Jump Count Low Band'], df2)
#
#
#
#
hist_stat(df1['IMA Jump Count Med Band'], df1)
hist_stat(df2['IMA Jump Count Med Band'], df2)
#
#
#
#
hist_stat(df1['IMA Jump Count High Band'], df1)
hist_stat(df2['IMA Jump Count High Band'], df2)
#
#
#
#
#
#
#
#
#
#
hist_stat(df1['Explosive Efforts'], df1)
hist_stat(df2['Explosive Efforts'], df2)
#
#
#
#
#
#
#
#
#
#
categorical_stats(df1['Position'], df1)
categorical_stats(df2['Position'], df2)

print(df1['Position'].unique())
#
#
#
#
#
#
categorical_stats(df1['Period'], df1)
categorical_stats(df2['Period'], df2)

print(df1['Period'].unique())
#
#
#
#
#
#
#
#
sns.pairplot(df1[['Total Player Load', 'Player Load Per Minute', 'IMA Accel Total',
       'IMA Decel Total', 'IMA Jump Count Low Band', 'IMA Jump Count Med Band',
       'IMA Jump Count High Band', 'Explosive Efforts']], plot_kws={'alpha': 0.5})
plt.show()
correlation = df1[['Total Player Load', 'Player Load Per Minute', 'IMA Accel Total',
        'IMA Decel Total', 'IMA Jump Count Low Band', 'IMA Jump Count Med Band',
        'IMA Jump Count High Band', 'Explosive Efforts']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation between 3 continuous chosen variables')
plt.show()
#
#
#
#
#
#
#
#
#
#
#
sns.pairplot(df2[['Total Player Load', 'Player Load Per Minute', 'IMA Accel Total',
       'IMA Decel Total', 'IMA Jump Count Low Band', 'IMA Jump Count Med Band',
       'IMA Jump Count High Band', 'Explosive Efforts']], plot_kws={'alpha': 0.5})
plt.show()
correlation = df2[['Total Player Load', 'Player Load Per Minute', 'IMA Accel Total',
        'IMA Decel Total', 'IMA Jump Count Low Band', 'IMA Jump Count Med Band',
        'IMA Jump Count High Band', 'Explosive Efforts']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation, annot=True, cmap='coolwarm', center=0)
plt.title('Correlation between 3 continuous chosen variables')
plt.show()
```
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(df1['IMA Accel Total'], df1['Total Player Load'], marker='o', linestyle='-', color='b', label='Total Player Load(0.86)')

# Add labels, title, and legend
plt.xlabel('IMA Accel Total')
plt.ylabel('Total Player Load (0.86)')
plt.title('IMA Accel Total vs Total Player Load')
plt.legend()
plt.grid(True)

# Show the plot
plt.show()
#
#
#
#
#
#
#
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

sns.scatterplot(data=df1, x='IMA Accel Total', y='Total Player Load', ax=axes[0], color='blue')
axes[0].set_title('Season 1 IMA Accel Total vs Total Player Load')
axes[0].set_xlabel('IMA Accel Total')
axes[0].set_ylabel('Total Player Load')

sns.scatterplot(data=df2, x='IMA Accel Total', y='Total Player Load', ax=axes[1], color='green')
axes[1].set_title('Season 2 IMA Accel Total vs Total Player Load')
axes[1].set_xlabel('IMA Accel Total')
axes[1].set_ylabel('Total Player Load')

plt.tight_layout()
plt.show()
#
#
#
#
#
