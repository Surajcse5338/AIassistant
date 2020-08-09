from bs4 import BeautifulSoup
from selenium import webdriver
import json

def getAllStateCovidData():

    driver = webdriver.Chrome('D:/chromedriver')
    driver.get('https://www.mohfw.gov.in/')
    r = driver.execute_script("return document.documentElement.outerHTML")
    driver.quit()

    soup = BeautifulSoup(r, 'html.parser')
    tableparentDiv = soup.find('div', {'class':'data-table table-responsive'})
    tableElement = tableparentDiv.find('table', {'class':'statetable table table-striped'})
    tableAllData = tableparentDiv.find('tbody', {})
    allStateRows = tableAllData.findAll('tr', {})

    # Iterate through each row and get each state data convert it to JSON and add to Array
    allStateData = {}
    for stateRow in allStateRows:
        allColumns = stateRow.findAll('td', {})
        dynamicShiftData = stateRow.findAll('span', {})
        if len(allColumns) == 8:
            allStateData.__setitem__(allColumns[1].text, {
                'activeCases': {
                    'total': int(allColumns[2].text),
                    'changeSinceYesterday': int(dynamicShiftData[0].text)
                },
                'cured/discharged/migrated': {
                    'cumulative': int(allColumns[4].text),
                    'changeSinceYesterday': int(dynamicShiftData[1].text)
                },
                'deaths': {
                    'cumulative': int(allColumns[6].text),
                    'changeSinceYesterday': dynamicShiftData[2].text
                }
            })

    return allStateData
