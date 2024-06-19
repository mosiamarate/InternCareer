# web_scraping.py - A Python script to scrape data from a website and automate the browser using Selenium.
#  Task 1: Web Scraping and Browser Automation

"""Importing libraries for web scraping"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pandas as pd
import time
# import matplotlib.pyplot as plt


"""Function to scrape the data from the website"""
def web_scraping():
    # URL of the website
    url = 'https://www.worldometers.info/coronavirus/'

    # Error handling
    retries = 5
    while retries > 0:
        try:
            # Sending request to the website
            response = requests.get(url, timeout=10)
            response.raise_for_status() # Raise an HTTPError for bad status codes
            break
        except Exception as e:
            print(f'Request failed: {e}. Retrying in 5 seconds...')
            retries -= 1
            time.sleep(5)
    else:
        print('Failed to retrieve the webpage after multiple attempts. Exiting the program...')
        return

    # Sending request to the website
    response = requests.get(url)

    # Parsing the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting the data from the website
    data = soup.find_all('div', class_='maincounter-number')

    if len(data) < 3:
        print('Failed to extract the data from the webpage. Exiting the program...')
        return
    
    # # Printing the data
    # print("COVID-19 Data")
    # print("-------------")
    # print('Total Cases:', data[0].text.strip())
    # print('Total Deaths:', data[1].text.strip())
    # print('Total Recovered:', data[2].text.strip())

    # Storing the data in a dictionary
    data_dict = {
        'Total Cases': data[0].text.strip(),
        'Total Deaths': data[1].text.strip(),
        'Total Recovered': data[2].text.strip()
    }

    # Converting the dictionary to a pandas DataFrame
    df = pd.DataFrame([data_dict])

    # Cleaning the data (removing commas and converting to integers)
    df['Total Cases'] = df['Total Cases'].str.replace(',', '').astype(int)
    df['Total Deaths'] = df['Total Deaths'].str.replace(',', '').astype(int)
    df['Total Recovered'] = df['Total Recovered'].str.replace(',', '').astype(int)
    
    # Formatting the numbers with spaces as thousands separators
    formatted_df = df.applymap(lambda x: f"{x:,}".replace(",", " "))

    # Printing the cleaned DataFrame with formatted numbers
    print('\nCleaned Dataframe:')
    print("\nCOVID-19 Data")
    print(formatted_df.to_string(index=False))

"""Function to automate the browser"""
def browser_automation():
    # URL of the website
    url = 'https://www.worldometers.info/coronavirus/'

    # Path to the chromedriver
    path = 'C:\chromedriver.exe'
    service = Service(path)
    driver = webdriver.Chrome(service=service)

    # Opening the website
    driver.get(url)
    
    try:
        # Extracting the data from the website
        total_cases = driver.find_element(By.XPATH, '//*[@id="maincounter-wrap"]/div/span[1]').text
        total_deaths = driver.find_element(By.XPATH, '//*[@id="maincounter-wrap"]/div/span[2]').text
        total_recovered = driver.find_element(By.XPATH, '//*[@id="maincounter-wrap"]/div/span[3]').text

        # # Printing the data
        # print('Total Cases:', total_cases.text)
        # print('Total Deaths:', total_deaths.text)
        # print('Total Recovered:', total_recovered.text)

        # Storing the data in a dictionary
        data_dict = {
            'Total Cases': total_cases,
            'Total Deaths': total_deaths,
            'Total Recovered': total_recovered
        }

        # Converting the dictionary to a pandas DataFrame
        df = pd.DataFrame([data_dict])
        df['Total Cases'] = df['Total Cases'].str.replace(',', '').astype(int)
        df['Total Deaths'] = df['Total Deaths'].str.replace(',', '').astype(int)
        df['Total Recovered'] = df['Total Recovered'].str.replace(',', '').astype(int)

        # Formatting the numbers with spaces as thousands separators
        formatted_df = df.applymap(lambda x: f"{x:,}".replace(",", " "))

        print('\nCleaned Dataframe:')
        print("\nCOVID-19 Data")
        print(formatted_df.to_string(index=False))
    
    except Exception as e:
        print(f'An error occurred: {e}')
    
    finally:
        # Closing the browser
        driver.quit()

"""Main function"""
if __name__ == '__main__':
    # Calling the function to scrape the data from the website
    web_scraping()

    # Calling the function to automate the browser
    browser_automation()

# """Function to visualize the data"""

# def visualize_data(df):
#     # Plotting the data
#     plt.figure(figsize=(10, 6))
#     plt.bar(df.columns, df.iloc[0])
#     plt.title('COVID-19 Data')
#     plt.xlabel('Categories')
#     plt.ylabel('Counts')
#     plt.show()

# # # Converting the dictionary to a pandas DataFrame
# # df = pd.DataFrame([data_dict])

# # Calling the function to visualize the data
# visualize_data(df)


# End of script