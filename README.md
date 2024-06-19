# InternCareer

# Task 1: Python Script for Web Scraping and Automation

Web Scraping and Browser Automation Script Documentation

Overview
This script performs two main tasks:

Web scraping to extract COVID-19 data from the Worldometers website.
Browser automation to extract the same data using Selenium WebDriver.
Libraries Used

1. requests: For sending HTTP requests to the website.
2. BeautifulSoup: For parsing HTML content.
3. selenium: For browser automation.
4. pandas: For data manipulation and cleaning.

Script Structure

1. Importing Libraries
    The script imports necessary libraries for web scraping, HTML parsing, browser automation, and data manipulation.

    python
        import requests
        from bs4 import BeautifulSoup
        from selenium import webdriver
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.common.by import By
        import pandas as pd

2. Web Scraping Function
    The web_scraping function performs the following steps:

    Sends an HTTP request to the Worldometers COVID-19 page.
    Parses the HTML content using BeautifulSoup.
    Extracts COVID-19 data (total cases, total deaths, and total recovered) from the page.
    Stores the data in a dictionary and converts it to a pandas DataFrame.
    Cleans the data by removing commas and converting strings to integers.
    Formats the numbers with spaces as thousands separators.
    Prints the cleaned and formatted DataFrame.

    python
    def web_scraping():
        url = '<https://www.worldometers.info/coronavirus/>'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        data = soup.find_all('div', class_='maincounter-number')

        data_dict = {
            'Total Cases': data[0].text.strip(),
            'Total Deaths': data[1].text.strip(),
            'Total Recovered': data[2].text.strip()
        }

        df = pd.DataFrame([data_dict])
        df['Total Cases'] = df['Total Cases'].str.replace(',', '').astype(int)
        df['Total Deaths'] = df['Total Deaths'].str.replace(',', '').astype(int)
        df['Total Recovered'] = df['Total Recovered'].str.replace(',', '').astype(int)
        
        formatted_df = df.applymap(lambda x: f"{x:,}".replace(",", " "))

        print('\nCleaned Dataframe:')
        print(formatted_df.to_string(index=False))

3. Browser Automation Function
    The browser_automation function performs the following steps:

    Initializes a Selenium WebDriver instance.
    Opens the Worldometers COVID-19 page in the browser.
    Extracts COVID-19 data using XPath selectors.
    Prints the extracted data.
    Closes the browser.

    python
    def browser_automation():
        url = '<https://www.worldometers.info/coronavirus/>'
        driver = webdriver.Chrome(executable_path='chromedriver.exe')
        driver.get(url)

        total_cases = driver.find_element(By.XPATH, '//*[@id="maincounter-wrap"]/div/span[1]')
        total_deaths = driver.find_element(By.XPATH, '//*[@id="maincounter-wrap"]/div/span[2]')
        total_recovered = driver.find_element(By.XPATH, '//*[@id="maincounter-wrap"]/div/span[3]')

        print('Total Cases:', total_cases.text)
        print('Total Deaths:', total_deaths.text)
        print('Total Recovered:', total_recovered.text)

        driver.quit()

4. Main Function
    The main function calls both web_scraping and browser_automation functions sequentially.

    python
        if __name__ == '__main__':
            web_scraping()
            browser_automation()

5. How to Run the Script
    Ensure all required libraries are installed:
    - requests
    - BeautifulSoup (part of bs4)
    - selenium
    - pandas

    Download and install the appropriate version of chromedriver for your system. Make sure chromedriver.exe is in your system PATH or specify its path in the script.
    Run the script using a Python interpreter:

    bash
            python script_name.py

6. Expected Output:
        Cleaned Dataframe:
        Total Cases Total Deaths Total Recovered
        704 753 890    7 010 681     675 619 811

End of Documentation
