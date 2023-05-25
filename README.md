# scrapingopendorse
# OpenDorse Scrape Script

This script uses Selenium WebDriver to scrape athlete data from OpenDorse URLs and stores the data into a pandas DataFrame.

## Dependencies

- Python 3
- selenium
- pandas
- webdriver_manager
- json
- time
- requests
- itertools
- os

## Environment Variables

The script uses the following environment variables:

- PROJECT_ID: The project ID for Google BigQuery.
- TABLE_NAME: The name of the table in the BigQuery database.

## Running the Script

1. Set the environment variables PROJECT_ID and TABLE_NAME.
2. Run the script using the command `python OpenDorseScrape.py`.

The script will scrape data from OpenDorse URLs, store the data in a DataFrame, append it to a BigQuery table, and print out the first 10 rows of the appended data.
