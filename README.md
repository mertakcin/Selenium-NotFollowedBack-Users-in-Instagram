# Selenium-NotFollowedBack-Users-in-Instagram

Using Selenium to see notfollowedback users on Instagram (Learn-by-doing mini project)

You need to install;
  * FireFox Web Browser
  * Gecko Driver (https://github.com/mozilla/geckodriver/releases)
  * Selenium (pip install selenium)
  * Python
  
In addition, you need to add the directory of geckodriver.exe(comes from the extraction of zip file) to PATH variable. Otherwise, It won't work.

+ loginInfo.py = You need to enter your username and password like;

  username = "jonathan"
  
  password = "livingston"
  
+ get_all_subscribers.py = This script will create a txt file that contains all of your followers on Instagram
+ get_all_followings.py = This script will create a txt file that contains all of your followings on Instagram

+ comparison.py = This script will compare txt files generated by the scripts above, and print the users who do not follow back.

