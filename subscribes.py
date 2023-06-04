import time
from selenium import webdriver

path = r'C:\chrome drive\chromedriver_win32.zip'
driver = webdriver.Chrome(path)
driver.get('https://www.youtube.com/channel/UCaRQVqYeQJALjKQPO6JWWsg')

time.sleep(1)

#for like button (works fine):
#like_btn = driver.find_element_by_xpath('//div[@id="info"]//ytd-toggle-button-renderer[1]//a[1]//yt-icon-button[1]//button[1]//yt-icon[1]')
#like_btn.click()

#for subscribe button (didn't work):
driver.execute_script("window.scrollTo(0, 300)") #scrolling down 300px to make subscribe button visible
subs_btn = driver.find_element_by_class_name('style-scope tp-yt-paper-button')
subs_btn.click()
