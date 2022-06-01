from selenium import webdriver
from selenium.webdriver import ChromeOptions, Remote
##

1234567
ds = {'platform': 'ANY',
      'browserName': "chrome",
      'version': '',
      'javascriptEnabled': True
      }

chromeOptions = webdriver.ChromeOptions() 
chromeOptions.add_argument("--headless")

#dr = webdriver.Remote('http://192.168.226.128:4444/wd/hub', desired_capabilities=ds)
dr = webdriver.Remote('http://192.168.226.128:4444/wd/hub', options=chromeOptions)
dr.get("https://www.google.com")
dr.save_screenshot('chrome.png')
print(dr.name)

'''
driver = webdriver.Remote(
    command_executor='http://localhost:4444/wd/hub',
    options=webdriver.ChromeOptions()
)

driver.get('http://www.google.com/')
'''
