#!/usr/bin/env python
# coding: utf-8

# In[31]:


import os
import csv


# In[53]:


PyBankcsv = os.path.join("budget_data.csv")


# In[54]:


profit = []
monthly_changes = []
date = []


# In[55]:


count = 0
total_profit = 0
total_change_profits = 0
initial_profit = 0


# In[35]:


with open(PyBankcsv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)



# In[56]:


import csv

# Open the CSV file
with open('budget_data.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)

    # Conducting the task
    count = 0
    for row in csvreader:
        count += 1



# In[57]:


date.append(row[0])


# In[58]:


profit.append(row[1])
total_profit = total_profit + int(row[1])


# In[59]:


final_profit = int(row[1])
monthly_change_profits = final_profit - initial_profit


# In[60]:


monthly_changes.append(monthly_change_profits)


# In[61]:


total_change_profits = total_change_profits + monthly_change_profits
initial_profit = final_profit


# In[62]:


average_change_profits = (total_change_profits/count)


# In[63]:


greatest_increase_profits = max(monthly_changes)
greatest_decrease_profits = min(monthly_changes)


# In[64]:


increase_date = date[monthly_changes.index(greatest_increase_profits)]
decrease_date = date[monthly_changes.index(greatest_decrease_profits)]


# In[65]:


print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print("Total Months: " + str(count))
print("Total Profits: " + "$" + str(total_profit))
print("Average Change: " + "$" + str(int(average_change_profits)))
print("Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")")
print("Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits)+ ")")
print("----------------------------------------------------------")


# In[66]:


with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(count) + "\n")
    text.write("    Total Profits: " + "$" + str(total_profit) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_change_profits)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(increase_date) + " ($" + str(greatest_increase_profits) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(decrease_date) + " ($" + str(greatest_decrease_profits) + ")\n")
    text.write("----------------------------------------------------------\n")


# In[ ]:




