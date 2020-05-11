from selenium import webdriver
import loginInfo
import time


#If the code does not work, make sure that you uploaded xpaths 

browser = webdriver.Firefox()

browser.get("https://www.instagram.com/")

time.sleep(2)



username = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input")
password = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

time.sleep(1)

giris_yap = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]")

giris_yap.click()

time.sleep(6)

kapat_bildirim = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]")

kapat_bildirim.click()

time.sleep(5)

profileButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a")

profileButton.click()

time.sleep(5)

followersButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")

followersButton.click()

time.sleep(5)


# FOLLOWERS List SCROLL Process

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


followersList = []

followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa")

for follower in followers:

    followersList.append(follower.text)

with open("followers.txt","w",encoding = "UTF-8") as file:

    for follower in followersList:
        file.write(follower + "\n")
        
    
    
time.sleep(1)


browser.close()

