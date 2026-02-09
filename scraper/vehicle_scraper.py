from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
import time


def scrape_vehicle_listings(brand: str, pages: int):
    base_url = f"https://riyasewana.com/search/{brand}?page="
    keyword_url = f"https://riyasewana.com/buy/{brand.replace('-', '-')}"
    results = []

    options = webdriver.ChromeOptions()
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        for page in range(1, pages + 1):
            url = f"{base_url}{page}/"
            driver.get(url)

            try:
                WebDriverWait(driver, 10).until(
                    EC.presence_of_all_elements_located((By.CLASS_NAME, "item.round"))
                )
            except TimeoutException:
                print(f"Timeout loading page {page}")
                continue

            cards = driver.find_elements(By.CLASS_NAME, "item.round")

            for card in cards:
                try:
                    anchor = card.find_element(By.TAG_NAME, "a")
                    href = anchor.get_attribute("href")

                    if href and keyword_url in href:
                        vehicle = card.find_element(By.CLASS_NAME, "more").text
                        place = card.find_element(By.CLASS_NAME, "boxintxt").text
                        price = card.find_element(By.CSS_SELECTOR, ".boxintxt.b").text
                        mileage = card.find_elements(By.CLASS_NAME, "boxintxt")[2].text
                        time_posted = card.find_element(By.CLASS_NAME, "boxintxt.s").text

                        results.append({
                            "vehicle": vehicle,
                            "place": place,
                            "price": price,
                            "mileage": mileage,
                            "time": time_posted,
                            "url": href
                        })

                except NoSuchElementException:
                    continue

    finally:
        driver.quit()

    return results
