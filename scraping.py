# OpenDorseScrape.py

import os
import re
import itertools
import time
import json
import requests
import pandas as pd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set up selenium webdriver options
option = webdriver.ChromeOptions()
option.add_argument("headless")
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome('chromedriver', options=option)

# Retrieve environment variables
PROJECT_ID = os.getenv('PROJECT_ID')
TABLE_NAME = os.getenv('TABLE_NAME')

def urls():
    # Fetch the URLs from BigQuery Table
    query = f"Select * from `{TABLE_NAME}`"
    urls = pd.read_gbq(query, project_id=PROJECT_ID)

    master_urls = (
        urls["Link1"].to_list()
        + urls["Link2"].to_list()
        + urls["Link3"].to_list()
        + urls["Link4"].to_list()
    )
    return master_urls

# Rest of the code remains same...

# Append the data to the table in BigQuery
df.to_gbq(TABLE_NAME, project_id = PROJECT_ID, if_exists='append')

# Query and check the first 10 rows of the appended data
query = f"Select * from `{PROJECT_ID}.{TABLE_NAME}`"
checking = pd.read_gbq(query, project_id=PROJECT_ID)
print(checking.head(10))

# Rest of the code remains same...
