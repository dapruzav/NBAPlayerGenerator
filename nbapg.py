# NBA Player Generator Created By © 2023 Anthony D'Apruzzo

# Import Statements
import selenium
from selenium import webdriver
import random
from selenium.webdriver.common.by import By

# Create Driver
driver = webdriver.Chrome()
driver.get("http://www.nba.com/players")


# Create Player Class
class Player:
    def __init__(self, pname, pinfo):
        self.pName = pname
        self.pInfo = pinfo


# Create Important Variables
dropDown = driver.find_element(By.XPATH, "//*[@id=\"__next\"]/div[2]/div[2]/main/div[2]/section/div/div[2]/div[1]/div[7]/div/div[3]/div/label/div/select")
players = []
flag = True

# Flip Page '1' To 'All'
for option in dropDown.find_elements(By.TAG_NAME, "option"):
    if option.text == 'All':
        option.click()
        break

# Get Content and Then Raw Info
content = driver.find_element(By.CLASS_NAME, 'players-list')
rawInfo = content.text.splitlines()

# Go through rawInfo and add player name (first + last) and player info into a Player object
for j in range(1, len(rawInfo), 3):
    pName = rawInfo[j] + ' ' + rawInfo[j + 1]
    pInfo = rawInfo[j + 2]
    p = Player(pName, pInfo)
    players.append(p)

# Close Driver
driver.quit()

# Main Program
while flag:
    userInput = int(input('How many players would you like to generate? (Maximum: 30) '))
    print()

    if userInput > 30:
        userInput = 30
    elif userInput < 1:
        userInput = 1

    for i in range(0, userInput):
        num = random.randint(0, len(players) - 1)
        print(players[num].pName)

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
