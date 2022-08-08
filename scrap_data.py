import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

option = webdriver.ChromeOptions()
option.add_argument('headless')
DRIVER = webdriver.Chrome(ChromeDriverManager().install(), options=option)

def scrap_data():
    DRIVER.get('https://www.worlddata.info/richest-countries.php')

    countries = DRIVER.find_elements(By.XPATH, "//*[@id='tabsort']/tbody/tr/td[2]/a")
    adjust_gdp_capita = DRIVER.find_elements(By.XPATH, "//*[@id='tabsort']/tbody/tr/td[3]")

    countries_gdp = []
    for i in range(len(countries)):
        temporary_data = {
            'Country': countries[i].text,
            'Adjusted GDP/capita': adjust_gdp_capita[i].text,
        }
        countries_gdp.append(temporary_data)

    data = pd.DataFrame(countries_gdp)
    data['Adjusted GDP/capita'] = data['Adjusted GDP/capita'].astype(str).str.replace('$', '-', regex=True)
    data['Adjusted GDP/capita'] = data['Adjusted GDP/capita'].astype(str).str.replace(' -', '', regex=True)

    data.to_csv('Data/data.csv')

    print('\n\n[INFO]------SCRAPING DONE')

