import requests, time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

service = Service(ChromeDriverManager().install())
URI = 'https://weather.com/weather/today/l/35a741555bbfc8bc576be864b0b64af6d1b2ad1328d2ee729f0de0ae00098e85'
driver = webdriver.Chrome(service=service)

def get_source_code(URI: str) -> None:
    driver.get(URI)
    
    while True:
        try:
            element = WebDriverWait(driver=driver, timeout=5).until(
                expected_conditions.presence_of_all_elements_located((By.ID, 'todayDetails'))
            )
            for e in element:
                with open('result.txt', 'a', encoding='utf-8') as f:
                    f.write(e.text)
            break
        except TimeoutException as _ex:
            print(_ex)
            break


def main() -> None:
    get_source_code(URI)


if __name__ == '__main__':
    main()