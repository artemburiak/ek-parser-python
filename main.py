from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

options = ChromeOptions()
options.add_argument('--window-size=1920,1080')

driver = Chrome('chromedriver.exe', options=options)
driver.maximize_window()

def next_page():
    driver.find_element(By.CLASS_NAME, 'pager-next').click()

def get_blocks():
    elements = driver.find_elements(By.CLASS_NAME, 'list-item--goods-group')
    return elements

def extract_info(block):
    name = block.find_element(By.CLASS_NAME, 'u').text
    link = block.find_element(By.CLASS_NAME, 'no-u').get_attribute('href')

    img = block.find_element(By.CLASS_NAME, 'list-img').find_element(By.TAG_NAME, 'img').get_attribute('src')
    print(name, link, img)

def main():
    driver.get('https://ek.ua/list/298/')
    while True:
        blocks = get_blocks()
        for block in blocks:
            extract_info(block)
        try:
            next_page()
        except:
            driver.close()
            break

if __name__ == '__main__':
    main()
