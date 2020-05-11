from selenium import webdriver

import loginInfo
import time




browser = webdriver.Firefox()

browser.get("https://www.instagram.com/")

time.sleep(2)

# XPATH of username and password fields. If code does not work, make sure that you update the xpath of the fields.

username = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
password = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")


username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

time.sleep(1)



signinButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")

signinButton.click()

time.sleep(6)

# In new version of Instagram web page, when you sign in, there is a notification that asks open notifications. This code block will click "not now" button.
# If code does not work, make sure that you update all xpaths.

close_notif = browser.find_element_by_xpath("/html/body/div[3]/div/div/div[3]/button[2]")

close_notif.click()

time.sleep(5)

#Clicking profile button that enables us going our profile

profileButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")

profileButton.click()

time.sleep(5)

# Clicking followings button that enables us seeing the list who we follow


followingButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a")

followingButton.click()

time.sleep(5)



# FOLLOWERS SCROLL Process. In there we need to scroll the followings list scroll bar, not the real window. 
# First you need to inspect the window. Then, you need to take the div that contains following list. In this case which is ".isgrP"

# These code block deals with that issue.
jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0,followers.scrollHeight);
var lenOfPage = followers.scrollHeight;
return lenOfPage;

"""

lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
        lastCount = lenOfPage
        time.sleep(1)
        lenOfPage = browser.execute_script(jscommand)
        if lastCount==lenOfPage:
            match=True

time.sleep(5)


followingsList = []

# In this case, div class of each follower is ".FPmhX.notranslate._0imsa".
# This code block will detect all followings add it in a list which is "followings" in that case

followings = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

for following in followings:

    followingsList.append(following.text)

with open("followings.txt","w",encoding = "UTF-8") as file:

    for following in followingsList:
        file.write(following + "\n")
        
    
    
time.sleep(1)


browser.close()

