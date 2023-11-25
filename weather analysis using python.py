#!/usr/bin/env python
# coding: utf-8

# WORKING ON A REAL PROJECT WITH PYTHON
# 
# Exploring Seattle's Weather Data
# 
# I'm diving into a practical project using Python to analyze the Seattle Weather dataset, a collection of time-stamped information on precipitation, temperature (both high and low), wind speed, and weather conditions. The data, sourced from Kaggle in a CSV format, will be  examined using Pandas DataFrame. The goal is to uncover meaningful insights and patterns in Seattle's weather over time, making this a hands-on exploration of real-world data.

# In[1]:


import pandas as pd


# In[2]:


a=pd.read_csv("/kaggle/input/weather-prediction/seattle-weather.csv")
a


# In[3]:


a.head(2)


# In[4]:


a.index


# **Columns     # It shows the name of each column**

# In[5]:


a.columns


# **dtypes   #It shows the data-type of each column**

# In[6]:


a.dtypes


# **unique()   #it is used to display the unique values ,it can be used on single column only not on all the dataframe.**

# In[7]:


a['weather'].unique()


# **nunique()      #it shows the total no of unique values in each column , it can be applied to single column  as well as on a whole dataframe**

# In[8]:


a.nunique()


# **count    #It shows the total no of non null in each column,it can be applied to single column  as well as on a whole dataframe****

# In[9]:


a.count()


# **value_counts      #In a column it shows all the unique values with their count.It can be applied on single column only**

# In[10]:


a['weather'].value_counts()


# **info()   #Provides the basic information about the dataframe**

# In[11]:


a.info()


# 

# **Describe()   #is used to desribe the count,mean std,max etc of all the columns** (used to generate descriptive statistics of a DataFrame or Series)

# In[12]:


a.describe()


# **Question 1)          Find all the unique "wind" values in the data**

# In[13]:


a.head(2)
a["wind"].unique()


# or

# In[14]:


a.nunique()


# or

# In[15]:


a['wind'].nunique()


# **Question 2)   Find the number of times when the weather is raining **

# In[16]:


#value_counts()
a['weather'].value_counts()


# In[17]:


#filtering
a[a.weather=='rain']


# In[18]:


#groupby()
a.groupby('weather').get_group('rain')


# **Question 3)  Find the number of times when the wind speed was exactly 2**

# In[19]:


a[a['wind']== 2]


# or

# In[20]:


a[a.wind==2]


# **Question 4) Find out all the null values in data.**

# In[21]:


a.isnull().sum()


# In[22]:


a.notnull().sum()


# **Question 5) Rename the column name weather to weather condition**

# In[23]:


a.rename(columns= {'weather':'weather_condition'})


# In[24]:


a.rename(columns={"weather" :"weather condition"},inplace=True)


# In[25]:


a.head()


# **Question 6) What is the  mean of 'precipitation'?**

# In[26]:


a['precipitation'].mean()


# OR

# In[27]:


a.precipitation.mean()


# **Question 7) What is the standard deviation of 'wind' in this data?**

# In[28]:


a.wind.std()


# **Question 8) What is the variance of 'wind' in this data?**

# In[29]:


a.wind.var()


# **Question 9) Find all the instance where the weather is 'fog'?**

# In[30]:


#value_counts
a['weather condition'].value_counts()


# In[31]:


#Filtering
a[a['weather condition']== 'fog']


# In[32]:


#Groupby
a.groupby('weather condition').get_group('fog')


# In[33]:


#str.contains
a[a['weather condition'].str.contains('fog')]


# **Question 10) Find all the instance where temp_max greater than 8 and temp_min is 10?**

# In[34]:


a[(a['temp_max']>8) & (a['temp_min'] ==10)]


# **Question 11) What is the mean value of each column against each 'Weather Condition'?**

# In[35]:


a.groupby('weather condition').mean(numeric_only=True)


# **Question 12) What is the Minimum & Maximum value of each column against each 'weather condition'?**

# In[36]:


a.groupby('weather condition').min()


# In[37]:


a.groupby('weather condition').max()


# **Question 13) Show all the record where weather condition is snow**

# In[38]:


a[a['weather condition']=='snow']


# **Question 14)Find all instances when weather is fog or  precipitation is  above 10?**

# In[39]:


a[((a['weather condition']=="fog") |  (a['precipitation']>10))]


# 

# **Question 15) Find all the instance a)Weather is snow and wind is greater than 6  or
#                                    b)temp_min is above 5 ****

# In[40]:


a[(a['weather condition']=='snow') & (a['wind']>6) | (a['temp_min']>15)]


# In[41]:


# Data Visualization   using Matplotlib 


# In[42]:


import matplotlib.pyplot as plt


# In[43]:


df=pd.DataFrame(a)
df['date'] = pd.to_datetime(df['date'])
plt.bar(df['date'], df['temp_max'], color='blue')
plt.xlabel('Date')
plt.ylabel('Max Temperature')
plt.title('Max Temperature over Time')
plt.show()


# In[44]:


x=a['date']
y=a['precipitation']
plt.figure(figsize=(30,10))
plt.plot(x,y,'r')
plt.title('Precipitation based on dates')
plt.show()


# In[45]:


df=pd.DataFrame(a)
weather=df['weather condition'].value_counts()
plt.bar(weather.index, weather.values, color='green')
plt.xlabel('Weather Condition')
plt.ylabel('Frequency')
plt.title('Frequency of Weather Conditions')


# In[46]:


df=pd.DataFrame(a)
df['wind'].value_counts()
plt.bar(df['date'],df['wind'],color='pink')
plt.xlabel('DATE')
plt.ylabel('WIND')
plt.title('DATE and WIND')



# In[47]:


df = pd.DataFrame(a)

# Count the frequency of each weather condition
weather = df['weather condition'].value_counts()

# Plot the pie chart
plt.pie(weather, labels=weather.index, autopct='%d%%', startangle=45, colors=['blue', 'lightgreen','pink','yellow','red'])
plt.title('Weather Condition Distribution')

