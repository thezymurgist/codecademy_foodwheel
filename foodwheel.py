
# coding: utf-8

# # Project: Board Slides for FoodWheel
# 
# FoodWheel is a startup delivery service that takes away the struggle of deciding where to eat! FoodWheel picks you an amazing local restaurant and lets you order through the app. Senior leadership is getting ready for a big board meeting, and as the resident Data Analyst, you have been enlisted to help decipher data and create a presentation to answer several key questions:
# 
# What cuisines does FoodWheel offer? Which areas should the company search for more restaurants to partner with?
# How has the average order amount changed over time? What does this say about the trajectory of the company?
# How much has each customer on FoodWheel spent over the past six months? What can this tell us about the average FoodWheel customer?
# 
# Over this project, you will analyze several DataFrames and create several visualizations to help answer these questions.

# We're going to use `pandas` and `matplotlib` for this project.  Import both libraries, under their normal names (`pd` and `plt`).

# In[18]:


import pandas as pd
from matplotlib import pyplot as plt


# ## Task 1: What cuisines does FoodWheel offer?
# The board wants to make sure that FoodWheel offers a wide variety of restaurants.  Having many different options makes customers more likely to come back.  Let's create pie chart showing the different types of cuisines available on FoodWheel.

# Start by loading `restaurants.csv` into a DataFrame called `restaurants`.

# In[19]:


restaurants = pd.read_csv("restaurants.csv")


# Inspect `restaurants` using `head`

# In[50]:


restaurants.head()


# How many different types of cuisine does FoodWheel offer?
# (hint: use `.nunique`)

# In[51]:


restaurants.cuisine.nunique()


# Let's count the number of restautants of each `cuisine`.  Use `groupby` and `count`.  Save your results to `cuisine_counts`.

# In[52]:


cuisine_counts = restaurants.groupby('cuisine').id.count().reset_index()
cuisine_counts.rename(columns={
                'id': 'count'},
                inplace=True)
cuisine_counts


# Let's use this information to create a pie chart.  Make sure that your pie chart includes:
# - Labels for each cuisine (i.e, "American", "Chinese", etc.)
# - Percent labels using `autopct`
# - A title
# - Use `plt.axis` to make the pie chart a perfect circle
# - `plt.show()` to display your chart

# In[53]:


plt.pie(cuisine_counts['count'], labels=cuisine_counts.cuisine, autopct="%0.1f%%")
plt.axis('equal')
plt.title("Cuisines Offerd by FoodWheel")
plt.show()


# ## Task 2: Orders over time
# FoodWheel is a relatively new start up.  They launched in April, and have grown more popular since them.  Management suspects that the average order size has increased over time.
# 
# Start by loading the data from `orders.csv` into the DataFrame `orders`.

# In[26]:


orders = pd.read_csv("orders.csv")


# Examine the first few rows of `orders` using `head`.

# In[54]:


orders.head()


# Create a new column in `order` called `month` that contains the month that the order was placed.
# 
# Hint: The function `split` will split a string on a character.  For instance, if `mydate` is the string `9-26-2017`, then `mydate.split('-')` would return the list `['9', '26', '2017']`.  `mydate.split('-')[0]` would return `'9'`.

# In[55]:


get_month = lambda x: x.split('-')[0]
orders['month'] = orders.date.apply(get_month)
orders.head()


# Group `orders` by `month` and get the average order amount in each `month`.  Save your answer to `avg_order`.

# In[56]:


avg_order = orders.groupby('month').price.mean().reset_index()
avg_order


# It looks like the average order is increasing each month.  Great!  We're eventually going to make a bar chart with this information.  It would be nice if our bar chart had error bars.  Calculate the standard deviation for each month using `std`.  Save this to `std_order`.

# In[57]:


std_order = orders.groupby('month').price.std().reset_index()
std_order


# Create a bar chart to share this data.
# - The height of each bar should come from `avg_price`
# - Use the standard deviations in `std_order` as the `yerr`
# - The error capsize should be 5
# - Make sure that you label each bar with the name of the month (i.e., 4 = April).
# - Also be sure to label the y-axis
# - Give your plot a descriptive title

# In[58]:


ax = plt.subplot()
plt.bar(range(len(avg_order.month)), avg_order.price, yerr=std_order.price, capsize=5)

ax.set_xticks(range(len(avg_order)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel("Average Order")
plt.title("Average Order by Month")

plt.show()


# ## Task 3: Customer types
# There is a range of amounts that customers spend at FoodWheel.  We'd like to create a histogram of the amount spent by each customer over the past six months.
# 
# Start by grouping `orders` by `customer_id` and calculating the total amount spent by each customer.  Save your results to `customer_amount`.

# In[59]:


customer_amount = orders.groupby('customer_id').price.sum().reset_index()
customer_amount.head()


# Create a histogram of this data.
# - The range should be from 0 to 200
# - The number of bins should be 40
# - Label the x-axis `Total Spent`
# - Label the y-axis `Number of Customers`
# - Add a titel

# In[61]:


plt.hist(customer_amount.price, range=(0, 200), bins=40)
plt.xlabel("Total Spent")
plt.ylabel("Number of Customers")
plt.title("Total Spent by Customers")
plt.show()

