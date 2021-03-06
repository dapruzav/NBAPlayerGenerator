#======================================================================= Imports
import selenium
from selenium import webdriver

import random

#======================================================================= Path Set / Driver & URL set up
PATH = "C://Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
URL = 'https://www.nba.com/players'
driver.get(URL)

#======================================================================= Important variables for later use
pageInfo = driver.find_element_by_class_name('Pagination_content__30uR3').text
dropDown = driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[3]/section/div/div[2]/div[1]/div[7]/div/div[3]/div/label/div/select')
of = pageInfo.find('of')
pageCount = int(pageInfo[ of + 3 : ])
names = []
playerInfo = []

#======================================================================= Method used by flipping through all pages. About 5 seconds slower
#i = 1
#while i <= pageCount:
#    content = driver.find_element_by_class_name('players-list')
#    playerList = content.text.splitlines()
#    for j in range(1, len(playerList), 3):
#        names.append(playerList[j] + ' ' + playerList[j + 1])
#        info.append(playerList[j + 2])
#    i += 1
#    for option in dropDown.find_elements_by_tag_name('option'):
#        if option.text == str(i):
#            option.click()
#            break      

#======================================================================= Player names and info are pulled from the website and added to lists
for option in dropDown.find_elements_by_tag_name('option'):
    if option.text == 'All':
        option.click()
        break
content = driver.find_element_by_class_name('players-list')
rawInfo = content.text.splitlines()
for j in range(1, len(rawInfo), 3):
    names.append(rawInfo[j] + ' ' + rawInfo[j + 1])
    playerInfo.append(rawInfo[j + 2])

#======================================================================= Close the web page
driver.quit()

#======================================================================= Start of main menu
flag = True

while flag:
    userInput = int(input('How many players would you like to generate? (Maximum: 30) '))
    print()

    if userInput > 30:
        userInput = 30;
    elif userInput < 1:
        userInput = 1;

    for i in range(0, userInput):
        num = random.randint(0, len(names) - 1)
        print(names[num])
    
    print('\n# of players generated: ' + str(userInput) + '.\n')
    
    while True:
        willContinue = input('Would you like to continue? (yes/no): ').lower()
        if willContinue == 'no':
            flag = False
            break
        elif willContinue == 'yes':
            print('Okay, we\'ll continue.\n')
            break
        else:
            print('Sorry, didn\'t understand that.\n')
            continue
print('Thank you!')