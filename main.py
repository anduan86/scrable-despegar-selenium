from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.us.despegar.com/flights/UIO/AGP?from=SB&di=1-0&reSearch=true")
flights = driver.find_elements(By.CLASS_NAME, "cluster-container")
for f in flights:
    airline_name = f.find_element(by=By.TAG_NAME, value="img").accessible_name
    departure = f.find_element(by=By.CLASS_NAME, value="cluster-part-0").text
    arrival = f.find_element(by=By.CLASS_NAME, value="cluster-part-1").text
    day = f.find_element(by=By.CLASS_NAME, value="quantity-days").text
    price = f.find_element(by=By.CLASS_NAME, value="price").text

    print(airline_name)
    print(departure)
    print(arrival)
    print(price)
    print('=' * 40)


driver.close()