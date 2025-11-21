from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_service = Service("C:\\Program Files\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)

try:
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("https://cmrcet.ac.in/")
    search_box.send_keys(Keys.RETURN)
    time.sleep(20)
finally:
    driver.quit()



week 12 --- https://github.com/Srivaishnavi08/tests.git
week 7 --- https://github.com/docker/getting-started-app.git
FROM node:18-alpine
WORKDIR /app
COPY . .
RUN yarn install --production
CMD ["node", "src/index.js"]
EXPOSE 3000


index.html

<!DOCTYPE html>
<html>
    <body>
        <button id="btn" onclick="document.getElementById('msg').innerText=('HELLO')">
            CLICK FOR SUPRISE
        </button>
        <p id="msg"></p>
    </body>
</html>


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_service = Service("C:\\Users\\REVANTH\\Downloads\\chromedriver-win64\\chromedriver-win64\\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_service)

try:
    driver.get("file:///C:/devexternal/week11/index.html")

    driver.find_element(By.ID, "btn").click()
    time.sleep(20)

    msg = driver.find_element(By.ID, "msg").text
    print("Output:", msg)

finally:
    driver.quit()
