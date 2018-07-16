
# coding: utf-8

# # Project: Board Slides for FoodWheel
# 
# FoodWheel is a startup delivery service that takes away the struggle of deciding where to eat!
# FoodWheel picks you an amazing local restaurant and lets you order through the app.
# Below is an analysis of the company's data and a presentation to answer several key questions:
# 
# What cuisines does FoodWheel offer? Which areas should the company search for more restaurants to partner with?
# How has the average order amount changed over time? What does this say about the trajectory of the company?
# How much has each customer on FoodWheel spent over the past six months? What can this tell us about the average FoodWheel customer?
#


# In[18]:


import pandas as pd
from matplotlib import pyplot as plt


# ## Task 1: What cuisines does FoodWheel offer?
# The board wants to make sure that FoodWheel offers a wide variety of restaurants.  Having many different options makes customers more likely to come back.


# In[19]:


restaurants = pd.read_csv("restaurants.csv")


# Inspect `restaurants` using `head`

# In[50]:


restaurants.head()


# How many different types of cuisine does FoodWheel offer?

# In[51]:


restaurants.cuisine.nunique()


# How many restaurants offer each cuisine?

# In[52]:


cuisine_counts = restaurants.groupby('cuisine').id.count().reset_index()
cuisine_counts.rename(columns={
                'id': 'count'},
                inplace=True)
cuisine_counts


# Make sure that the pie chart includes:
# - Labels for each cuisine (i.e, "American", "Chinese", etc.)
# - Percent labels using `autopct`
# - A title
# - Use `plt.axis` to make the pie chart a perfect circle
# - `plt.show()` to display the chart

# In[53]:


plt.pie(cuisine_counts['count'], labels=cuisine_counts.cuisine, autopct="%0.1f%%")
plt.axis('equal')
plt.title("Cuisines Offerd by FoodWheel")
plt.show()


# ## Task 2: Orders over time
# FoodWheel is a relatively new start up.  They launched in April, and have grown more popular since them.  Management suspects that the average order size has increased over time.
#

# In[26]:


orders = pd.read_csv("orders.csv")



# In[54]:


orders.head()


# Create a new column in `order` called `month` that contains the month that the order was placed.
#

# In[55]:


get_month = lambda x: x.split('-')[0]
orders['month'] = orders.date.apply(get_month)
orders.head()


# Group `orders` by `month` and get the average order amount in each `month`.  Answer saved to `avg_order`.

# In[56]:


avg_order = orders.groupby('month').price.mean().reset_index()
avg_order


# It looks like the average order is increasing each month. Calculate the standard deviation for each month using `std`.  Save this to `std_order`.

# In[57]:


std_order = orders.groupby('month').price.std().reset_index()
std_order


# Create a bar chart to share this data.
# - The height of each bar should come from `avg_price`
# - Use the standard deviations in `std_order` as the `yerr`
# - The error capsize should be 5
# - Make sure that each bar is labeled with the name of the month (i.e., 4 = April).
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
# There is a range of amounts that customers spend at FoodWheel.  Create a histogram of the amount spent by each customer over the past six months.
#

# In[59]:


customer_amount = orders.groupby('customer_id').price.sum().reset_index()
customer_amount.head()


# Create a histogram of this data.
# - The range should be from 0 to 200
# - The number of bins should be 40
# - Label the x-axis `Total Spent`
# - Label the y-axis `Number of Customers`
# - Add a title

# In[61]:


plt.hist(customer_amount.price, range=(0, 200), bins=40)
plt.xlabel("Total Spent")
plt.ylabel("Number of Customers")
plt.title("Total Spent by Customers")
plt.show()

