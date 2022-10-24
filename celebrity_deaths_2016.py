#!/usr/bin/env python
# coding: utf-8

# # Data Analysis - Celebrity Deaths in 2016
# 
# Source: [Wikipedia - Deaths in 2016](https://en.wikipedia.org/wiki/Deaths_in_2016)
# 
# #### Structure of dataset:
# - File: "celebrity_deaths_2016.xlsx"
# - Contains 2 sheets:
#  - "celeb_death": contains records of deaths of famous humans and non-humans
#  - "cause_of_death": contains the causes of the deaths (you'll need to merge it with the "celeb_death" sheet)
# 
# #### Other information about the dataset:
# - The cause of death was not reported for all individuals
# - The dataset might include deaths that took place in other years (you'll need to ignore these records)
# - The dataset might contain duplicate records (you'll need to remove them)
# 
# #### The goals of the exercise:
# - Load, merge, and clean the data
# - Explore the data and answer some simple questions
# - Run some basic analysis
# - Visualize your results

# In[489]:


get_ipython().run_cell_magic('capture', '', '###########################################################\n### EXECUTE THIS CELL BEFORE YOU TO TEST YOUR SOLUTIONS ###\n###########################################################\nimport imp, os, sys\nimport importlib\nsol = imp.load_compiled("sol", "./sol.py")\nfrom nose.tools import assert_equal\nfrom pandas.util.testing import assert_frame_equal, assert_series_equal')


# In[490]:


"""
We're providing most of the import statements you need for the entire exercise
"""

import pandas as pd
import matplotlib.pyplot as plt 

get_ipython().run_line_magic('matplotlib', 'inline')


# ### Load, merge, and clean the data

# In[491]:


""" 1.
1. Load the "celebrity_deaths_2016.xlsx" data file in the name "xl". (This file is saved in the same directory as this notebook.)
2. Print the sheet names
"""

# YOUR CODE HERE  (pass)

xl = pd.ExcelFile("celebrity_deaths_2016.xlsx")
df = pd.DataFrame(xl.parse("celeb_death"))
df


# In[492]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(xl.sheet_names, sol.xl.sheet_names)


# In[493]:


""" 2.
1. Read the "celeb_death" sheet into a dataframe named "df"
2. Take a look at the top 5 rows. Save it in a variable called 'top5', then print it
"""
# YOUR CODE HERE  (pass)
top5 = df.head(5)
#print(top5)


# In[494]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_frame_equal(top5, sol.top5)


# In[495]:


""" 3.
1. Take a look at the data types stored in each column in df. Store these in a variable called 'df_dtypes'
2. Get the shape of df. Store this in a variable called 'df_shape'
3. Print these
"""
# YOUR CODE HERE (pass)
df_dtypes=top5.dtypes
df_shape = df.shape


# In[496]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_series_equal(df_dtypes, sol.df_dtypes)
assert_equal(df_shape, sol.df_shape)


# In[497]:


""" 4.
Drop the duplicates (based on all columns) from df
"""
# YOUR CODE HERE (pass)
df = df.drop_duplicates()


# In[498]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_frame_equal(df, sol.df2)


# In[499]:


""" 5.
1. Read the "cause_of_death" sheet into a DataFrame named "cause_of_death"
2. Take a look at the top 5 rows. Store this in a variable named cause_top5, then print it
"""
# YOUR CODE HERE

# YOUR CODE HERE (pass)
cause_of_death = pd.read_excel(xl, 'cause_of_death')
cause_top5 = cause_of_death.head(5)
print(cause_top5)
 


# In[500]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_frame_equal(cause_top5, sol.cause_top5)


# In[501]:


""" 6.
Drop the duplicates (based on the "cause_id" column) from the cause_of_death DataFrame

Hint: There is a single DataFrame method that does this
Use the "subset" argument to specify the "cause_id" column

Reference: https://pandas.pydata.org/pandas-docs/stable/reference/frame.html
"""
# YOUR CODE HERE (pass)
cause_of_death = cause_of_death.drop_duplicates(subset='cause_id', keep='first')



# In[502]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_frame_equal(cause_of_death, sol.cause_of_death)


# In[503]:


""" 7.
1. Merge the cause_of_death DataFrame with the df DataFrame and name the new DataFrame as "df"
2. Take a look at the top 5 rows in df. Save these in a variable called df_top5, then print it

Note: There are records in df (left DataFrame) that do not have a matching record in cause_of_death (right DataFrame)
We want to see ALL records in df despite the missing matches in cause_of_death, so you DON'T want to use an "inner join"
"""
# YOUR CODE HERE  (pass)
df = pd.merge(df, cause_of_death, how = 'left', on='cause_id') 
df_top5 = df.head() 
df_top5




# In[504]:


##########################
### TEST YOUR SOLUTION ###
##########################
assert_frame_equal(df_top5, sol.df_top5)


# ### Querying data
# 
# For the following questions, all the operations are on the Dataframe df.

# In[505]:


""" 8.
We'll be doing some calculations with the age column, but it was loaded from the data file as dtype "object"
So first, we need to cast DataFrame df to a numeric value
"""
# YOUR CODE HERE (pass)
df['age'] = pd.to_numeric(df['age'], errors='coerce')


# In[506]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_series_equal(df['age'], sol.df3['age'])


# In[507]:


""" 9.
What was the average age of death? Store this value in a variable called 'avg_age', then print it
"""
# YOUR CODE HERE    (passed! must be 77.03194103194103)


avg_age = df["age"].mean()

print(avg_age)
 


# In[508]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(avg_age, sol.avg_age)


# In[509]:


""" 10.
How many people died after the age of 70?
-- Store the result count in a variable named "count" and print it
"""
# YOUR CODE HERE (pass)

count = 0

for i in range(0,len(df)):
    if(df['age'][i] > 70):
        count+=1

print(count)


# In[510]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(count, sol.count)


# In[511]:


""" 11.
Who died the youngest and what was the cause of death?
-- Store the name in a variable named "youngest_name" and print it
-- Store the cause in a variable named "youngest_cause" and print it

Hint: Get the min age and find the record that has that value
"""
# YOUR CODE HERE (pass)

youngest_name = df['name'][df[['age']].idxmin()]

youngest_cause = df['cause of death'][df[['age']].idxmin()]

print(youngest_name)
print(youngest_cause) 


# In[512]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_series_equal(youngest_name, sol.youngest_name)
assert_series_equal(youngest_cause, sol.youngest_cause)


# In[513]:


""" 12.
We'll be running some queries based on the "bio" column, 
but it was loaded from the data file as an object.  So first, cast this column to a string.
"""
# YOUR CODE HERE (pass)
df['bio'] = df['bio'].astype('str')
df['cause of death'] = df['cause of death'].astype('str')


# In[514]:


print(df.dtypes)


# In[515]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_series_equal(df['bio'], sol.df['bio'])


# In[516]:


""" 13.
How many American celebrities died?
-- Store the result count in a variable named "count_american" and print it

Hint: Search the bio for "American"
"""
# YOUR CODE HERE        (pass)
count_american = df['bio'].str.contains('American').sum()


# In[517]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_equal(count_american, sol.count_american)


# In[518]:


""" 14.
What was one known cause of death for celebrities who died at age 50?
-- Name the result as "rand_cause"
-- Print the result using "print("Age 50. Cause of Death:", rand_cause)"

Hint: 
Get all the celebrity death records for celebrities who died at 50  
Ignore the ones where the cause of death is unknown, or NaN
import random and randomly select one of the death records 
Extract the cause of death and store in a variable "rand_cause"
"""

#############################################################################################
### DO NOT MODIFY THIS! WE NEED TO SEED THE RANDOM VALUE TO ACCURATELY TEST YOUR SOLUTION ###
import random
random.seed(0)
#############################################################################################

rand_cause = random.choice(list(df[df["age"] == 50]["cause of death"]))    #(pass)
print("Age 50. Cause of Death:", rand_cause)



# In[519]:


##########################
### TEST YOUR SOLUTION ###
##########################

from nose.tools import assert_in
assert_in(rand_cause, sol.possible_causes.values)


# In[520]:


""" 15.
What was the mean age for each cause of death?

Hint: import numpy and group by 'cause of death', then get the mean age and store the 
resulting DataFrame in a variable named 'df_grouped_cause', then print it
"""
# YOUR CODE HERE
df_grouped_cause = df.groupby('cause of death').agg({'age':['mean']})

df_grouped_cause


# In[535]:


##########################
### TEST YOUR SOLUTION ###
##########################
assert_frame_equal(df_grouped_cause, sol.df_grouped_cause)


# ### Count the number of people who died in each month of 2016
# 1. Create new columns that shows which month and year each person died in
# 2. Group all the entries based on the month they appeared in

# In[522]:


""" 16.
Make a new column in the DataFrame df with the numeric month of death

Hint:
Use the apply() method to run a function against the "date of death" column,
and return the numeric month (get the value by using ".month")
"""


def get_month(date):                                     #(pass)
    m = pd.to_datetime(date)
    return m.month
df["month"] = df["date of death"].apply(get_month)


# In[523]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_series_equal(df['month'], sol.df['month'])


# In[524]:


""" 17.
Make a new column in the DataFrame df with the year of death

Hint: Apply a function to get the year from the "date of death" column
"""

df['year of death'] = df['date of death'].dt.year
df.head(5)
    


# In[525]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_series_equal(df['year'], sol.df['year'])


# In[526]:


""" 18.
There could be a small number of deaths that didn’t take place in 2016.  Just in case, 
filter out the deaths that didn’t take place in 2016.
-- Name the new DataFrame as “df_2016”
Hint: Query the df DataFrame for deaths where the “year” == 2016.
"""
# YOUR CODE HERE
df_2016 = df[df['year of death'] == 2016]
df_2016.head(5)


# In[527]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_frame_equal(df_2016, sol.df_2016)


# In[551]:


""" 19.
Using a pivot table, obtain a list that contains the number of people that died in each month
-- Use the new DataFrame "df_2016"
-- Name the result as "df_per_month"
"""
# YOUR CODE HERE
df_per_month = pd.pivot_table(df, index="month", values="name",aggfunc="count")

#df_per_month = df_2016.pivot_table(index="month",values="name", aggfunc="count")

df_per_month


# In[529]:


##########################
### TEST YOUR SOLUTION ###
##########################

df_sub = df_per_month
df_sol = sol.df_per_month

df_sub.columns = ['namelen']
df_sol.columns = ['namelen'] 

assert_frame_equal(df_sub, df_sol)


# In[541]:


df_sol


# ### Data Visualization

# In[530]:


""" 20. 
Visualize the number of deaths per month as a bar chart

Hint: A DataFrame has a simple .plot() method you can use.  

The x axis should show the individual number of the month and the y axis should show the death counts
Don't forget to add a title and labels for the x and y axes
"""

# YOUR CODE HERE
ax = df['month of death'].value_counts().plot(kind='bar',figsize=(14,8),title="Deaths per month") 
ax.set_xlabel("Month") 
ax.set_ylabel("Deaths")


###########################
### DO NOT MODIFY THIS! ###
plt.show()
###########################


# ### Make a bar chart that plots the number of deaths per nationality
# 1. Create a new column that identifies the nationality of each celebrity, extracting the first word from the bio
# 2. Make a bar chart that plots the number of deaths per nationality

# In[531]:


""" 21.
Create a new column in the DataFrame df that identifies the nationality of each celebrity, 
extracting the first word from the bio

Hint:
To get the nationality from the bio, use the method split() on the column "bio" 
and use the first element in the split result as the nationality.

For simplicity purposes, don't worry about nationalities containing more than 1 word.  For example, 
when getting the nationality from "bio", it's OK to get "New" for New Zealand or "Costa" for Costa Rican.
"""

def get_nationality(bio):   #(pass)
    return bio.split()[0]

df["nationality"] = df["bio"].apply(get_nationality)


# In[532]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_series_equal(df['nationality'], sol.df['nationality'])


# In[539]:


""" 22.
Make a bar chart that plots the number of deaths per nationality
Only include nationalities with more than 50 deaths
-- Name the resulting Series as "unlucky_countries"
Hint(s):
Get the count of unique values in the 'nationality' column using the value_counts() method.
Filter the resulting Series to only include those nationalities with a count of more than 50.
Plot the final Series.  Note, a Series has a simple .plot() method you can use.
The x axis should show the individual nationalities and the y axis should show the death counts
Don't forget to add a title and labels for the x and y axis
"""
# YOUR CODE HERE
CountStatus = pd.value_counts(df['nationality'].values, sort=True)
unlucky_countries = CountStatus.loc[lambda x: x > 50] 
ax = unlucky_countries.plot(kind='bar',figsize=(14,8),title="Deaths per country")
ax.set_xlabel("Country") 
ax.set_ylabel("Deaths")









###########################
### DO NOT MODIFY THIS! ###
plt.show()
###########################


# In[540]:


##########################
### TEST YOUR SOLUTION ###
##########################

assert_series_equal(unlucky_countries, sol.unlucky_countries)


# In[ ]:




