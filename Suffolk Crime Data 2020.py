# %%
# 2020 Data


# importing essential library
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from IPython import display 

months = ["Jan","Feb","Mar","Apr","May","Jun","Jul", "Aug", "Sept"]

# %%
#for i in range(2,7): # make it so that i dont have to repeat constantly

DATA_PATH_Apr = Path('2020-04', '2020-04-suffolk-street.csv')
dfraw_Apr = pd.read_csv(DATA_PATH_Apr)

DATA_PATH_May = Path('2020-05', '2020-05-suffolk-street.csv')
dfraw_May = pd.read_csv(DATA_PATH_May)

DATA_PATH_Jun = Path('2020-06', '2020-06-suffolk-street.csv')
dfraw_Jun = pd.read_csv(DATA_PATH_Jun)

DATA_PATH_Jul = Path('2020-07', '2020-07-suffolk-street.csv')
dfraw_Jul = pd.read_csv(DATA_PATH_Jul)

DATA_PATH_Aug = Path('2020-08', '2020-08-suffolk-street.csv')
dfraw_Aug = pd.read_csv(DATA_PATH_Aug)

DATA_PATH_Sept = Path('2020-09', '2020-09-suffolk-street.csv')
dfraw_Sept = pd.read_csv(DATA_PATH_Sept)


# %%
print('number of incidents recorded in April = ', len(dfraw_Apr))
print('number of incidents recorded in May = ', len(dfraw_May))
print('number of incidents recorded in June = ', len(dfraw_Jun))
print('number of incidents recorded in July = ', len(dfraw_Jul))
print('number of incidents recorded in August = ', len(dfraw_Aug))
print('number of incidents recorded in September = ', len(dfraw_Sept))

# %%
dfraw_Apr = pd.read_csv(DATA_PATH_Apr)
dfraw_Apr.head()

# %%
dfraw_Apr.describe()

# %%
dfraw_Apr.info()

# %%
DATA_PATH = Path('2020-04', '2020-04-suffolk-street.csv')
Apr = pd.read_csv(DATA_PATH)
len(Apr) # displays how many crimes was committed 

# %%
DATA_PATH = Path('2020-05', '2020-05-suffolk-street.csv')
May = pd.read_csv(DATA_PATH)
len(May) # Displays how many crimes committed

# %%
total_incidents_apr_may = len(Apr)+len(May)
print('Total recorded incidents for April and May combined (2020) = '+ str(total_incidents_apr_may))

# %% [markdown]
# # ==============================================================================

# %%
# N.B. files stored in current directory
months = np.array(['2020-04-suffolk-street.csv', 
                    '2020-05-suffolk-street.csv',
                    '2020-06-suffolk-street.csv',
                    '2020-07-suffolk-street.csv',
                    '2020-08-suffolk-street.csv',
                    '2020-09-suffolk-street.csv'])
months

# %%
file = np.array(['2020-04',
                 '2020-05',
                 '2020-06',
                 '2020-07',
                 '2020-08',
                 '2020-09'])

# %%
# using the 'Path' method imported from 'pathlib'

months_added = pd.DataFrame() # an empty dataframe

for m in range(len(months)):
    x = file[m]
    y = months[m]
    
    DATA_PATH = Path(f'{x}', f'{y}')
    
    file_1 = pd.read_csv(DATA_PATH)

    #months_added = months_added.append(file_1, ignore_index=True)
    months_added = pd.concat([months_added,file_1], ignore_index=True)
months_added
print('Total recorded incidents for April to September combined (2020) = '+ str(len(months_added)))

# %%
# create df with columns 'Year' & 'Month_Number'
df_Split_Month = months_added['Month'].str.split("-", n = 1, expand = True) 
df_Split_Month = df_Split_Month.rename(columns={0:'Year', 1:'Month_Number'})
type(df_Split_Month['Month_Number'][0])

# %%
months_added['Year'] = df_Split_Month['Year']
months_added['Month_Number'] = df_Split_Month['Month_Number']
months_added.head()

# %%
months_added_grouped = months_added.groupby(["Crime type", "Month"]).agg(
    count=pd.NamedAgg(column="Crime type", aggfunc="count"))

months_added_grouped

# %%
months_added_pivot = months_added.groupby(['Crime type', 'Month_Number'])\
                                        .Month.agg('count').to_frame('count').reset_index()

months_added_pivot.head()

# %%
months_added_Pivot = months_added_pivot.pivot(index='Crime type', columns='Month_Number', values='count').fillna(0)
months_added_Pivot

# %%
months = months_added_Pivot
months = months.reset_index()
months.iloc[:,0]

# %%
labels = list(months.iloc[:,0])
labels

# %%
# using matplotlib - plt.subplots() is a function that returns a tuple 
# containing a figure and axes object(s).
# When using fig, ax = plt.subplots() you unpack this tuple into 
# the variables fig and ax. Having fig is useful if you want to change 
# figure-level attributes or save the figure as an image file later 
# (e.g. with fig.savefig('yourfilename.png')). 

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots(figsize=(8,6))
rects1 = ax.bar(x - width/2, months.iloc[:,1], width, label='Jan')
rects2 = ax.bar(x + width/2, months.iloc[:,2], width, label='Feb')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xticks(x)
ax.set_ylabel('Incidents reported count') # y axis labels
ax.set_title('Incident type')
ax.set_xticklabels(labels)
#ax.set_xticklabels(labels, rotation=90)

ax.legend()

fig.tight_layout()
plt.xticks(rotation=90)

plt.show()

# %%
# When the x axis is the labels

# using matplotlib - plt.subplots() is a function that returns a tuple 
# containing a figure and axes object(s).
# When using fig, ax = plt.subplots() you unpack this tuple into 
# the variables fig and ax. Having fig is useful if you want to change 
# figure-level attributes or save the figure as an image file later 
# (e.g. with fig.savefig('yourfilename.png')). 

x = np.arange(len(labels))  # the label locations

fig, ax = plt.subplots(figsize=(8,6))
plt.plot(labels, months.iloc[:,1], 'b-') 
plt.plot(labels, months.iloc[:,2], 'r-') 

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_xticks(x)
ax.set_ylabel('Incidents reported count')
ax.set_title('Incident type')
ax.set_xticklabels(labels)

fig.tight_layout()
plt.xticks(rotation=90)

plt.show()

# %%
# using matplotlib - plt.subplots() is a function that returns a tuple 
# containing a figure and axes object(s).
# When using fig, ax = plt.subplots() you unpack this tuple into 
# the variables fig and ax. Having fig is useful if you want to change 
# figure-level attributes or save the figure as an image file later 
# (e.g. with fig.savefig('yourfilename.png')). 

y = np.arange(len(labels))  # the label locations

fig, ax = plt.subplots(figsize=(8,6))
plt.plot(months.iloc[:,1], labels,'b-') 

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_yticks(y)
ax.set_xlabel('Incidents reported count')
ax.set_title('Incident type')

fig.tight_layout()
plt.xticks(rotation=0)

plt.show()

# %%
# aim for this graph is create a graph of TOTAL crimes a month over a time period

# %%
y = np.arange(len(labels))  # the label locations

#fig, ax = plt.subplots(figsize=(8,6))
#plt.plot(labels, months.iloc[1:],'b-') 

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_yticks(y)
ax.set_xlabel('April - September Crime Count')
ax.set_title('2020 Total Crime Rates')

#fig.tight_layout()
#plt.xticks(rotation=0)

plt.show()



# %%
months.iloc[13:14]

# %%
# violent_crime = violent_crime.pivot(index='Crime type', 
#                     columns='Month_Number', values='count').fillna(0)

# %%
months_added_pivot.pivot(index='Crime type', 
                    columns='Month_Number', values='count').fillna(0)


