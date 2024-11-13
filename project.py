#!/usr/bin/env python
# coding: utf-8

# In[23]:


import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots


# In[24]:


def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    stock_data_specific = stock_data[stock_data.Date <= '2021--06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data_specific.Date, infer_datetime_format=True), y=stock_data_specific.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data_specific.Date, infer_datetime_format=True), y=revenue_data_specific.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()


# Question 1: Use yfinance to Extract Stock Data

# In[25]:


tesla=yf.Ticker("TSLA")
tesla=yf.Ticker("TSLA")
tesla_data.reset_index(inplace=True)
tesla_data.head(5)


# Question 2: Use Webscraping to Extract Tesla Revenue Data

# In[26]:


url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text


# In[27]:


soup = BeautifulSoup(html_data)


# In[28]:


data = []
for table in soup.find_all("table"):
    
    if any(["Tesla Quarterly Revenue".lower() in th.text.lower() for th in table.find_all("th")]):
        for row in table.find("tbody").find_all("tr"):
            date_col, rev_col = [col for col in row.find_all("td")]
            data.append({
                "Date": date_col.text,
                "Revenue": rev_col.text
            })

tesla_revenue = pd.DataFrame(data)


# In[29]:


tesla_revenue.tail(5)


# Question 3: Use yfinance to Extract Stock Data

# In[30]:


gme = yf.Ticker("GME")
gme_data = gme.history(period="max")
gme_data.reset_index(inplace=True)
gme_data.head()


# Question 4: Use Webscraping to Extract GME Revenue Data

# In[31]:


url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"
html_data = requests.get(url).text


# In[32]:


soup = BeautifulSoup(html_data)


# In[33]:


data = []
for table in soup.find_all("table"):
    
    if any(["GameStop Quarterly Revenue".lower() in th.text.lower() for th in table.find_all("th")]):
        for row in table.find("tbody").find_all("tr"):
            date_col, rev_col = [col for col in row.find_all("td")]
            data.append({
                "Date": date_col.text,
                "Revenue": rev_col.text.replace("$", "").replace(",", "")
            })

gme_revenue = pd.DataFrame(data)


# In[34]:


gme_revenue.tail()


# Question 5: Plot Tesla Stock Graph

# In[35]:


import yfinance as yf
import plotly.graph_objs as go

# Fetch Tesla stock data using yfinance
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="1y")  # Get 1 year of stock data

# Define the make_graph function
def make_graph(data, title="Stock Data"):
    # Create a line graph for the 'Close' price
    trace = go.Scatter(
        x=data.index,
        y=data['Close'],
        mode='lines',
        name='Tesla Close Price'
    )
    
    # Define the layout with a title
    layout = go.Layout(
        title=title,
        xaxis={'title': 'Date'},
        yaxis={'title': 'Price (USD)'}
    )
    
    # Create the figure with the data and layout
    fig = go.Figure(data=[trace], layout=layout)
    
    # Display the graph
    fig.show()

# Call the make_graph function to plot the Tesla stock data with a title
make_graph(tesla_data, title="Tesla Stock Price Over the Last Year")


# Question 6: Plot GameStop Stock Graph

# In[36]:


import yfinance as yf
import plotly.graph_objs as go

# Fetch GameStop stock data using yfinance
gamestop = yf.Ticker("GME")
gamestop_data = gamestop.history(period="1y")  # Get 1 year of stock data

# Define the make_graph function
def make_graph(data, title="Stock Data"):
    # Create a line graph for the 'Close' price
    trace = go.Scatter(
        x=data.index,
        y=data['Close'],
        mode='lines',
        name='GameStop Close Price'
    )
    
    # Define the layout with a title
    layout = go.Layout(
        title=title,
        xaxis={'title': 'Date'},
        yaxis={'title': 'Price (USD)'}
    )
    
    # Create the figure with the data and layout
    fig = go.Figure(data=[trace], layout=layout)
    
    # Display the graph
    fig.show()

# Call the make_graph function to plot the GameStop stock data with a title
make_graph(gamestop_data, title="GameStop Stock Price Over the Last Year")


# In[ ]:




