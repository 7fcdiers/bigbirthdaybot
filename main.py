from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import random
from time import sleep

import messages as m


def init(s, show, download_dir=None):
    options = Options()

    if download_dir != None:
        options.add_experimental_option('prefs', {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "plugins.always_open_pdf_externally": True
        }
                                        )

    if show:
        options.headless = True
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--window-size=1920,1080')
        options.add_argument('start-maximized')
        # options.add_argument(f'user-agent={user_agent}')
    try:
        driver = webdriver.Chrome(service=s, chrome_options=options)
    except:
        driver = webdriver.Chrome(service=s, options=options)

    driver.get("https://www.seleniumhq.org/download/")

    a = driver.execute_script("return navigator.userAgent")
    user_agent = str(a).replace('HeadlessChrome', 'Chrome')
    options.add_argument(f'user-agent={user_agent}')

    driver.quit()
    try:
        driver = webdriver.Chrome(service=s, chrome_options=options)
    except:
        driver = webdriver.Chrome(service=s, options=options)

    return driver

def paste_content(driver, el, content):
    driver.execute_script(
      f'''
const text = `{content}`;
const dataTransfer = new DataTransfer();
dataTransfer.setData('text', text);
const event = new ClipboardEvent('paste', {{
  clipboardData: dataTransfer,
  bubbles: true
}});
arguments[0].dispatchEvent(event)
''',
      el)

# Initialisation du navigateur web (assure-toi d'avoir installé le navigateur et le pilote appropriés)
driver = webdriver.Chrome('chromedriver.exe')

# Ouvre WhatsApp Web
driver.get('https://web.whatsapp.com')

input("Appuie sur Entrée après t'être connecté à WhatsApp Web...")

# Pour un contact
contact_name = 'Maternat' #TODO remplacer Cyril Diers par Franck Van Daele
contact = driver.find_element(By.XPATH, '//span[@title="' +contact_name +'"]')
contact.click()

total_sec = 0
input_box = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]')

for msg in m.msg_list:
    if msg[1] == "rand":
        sec = random.randint(15,90) #TODO remplacer 2 par valeur plus grande le jour J
    else:
        sec = msg[1]
    print("Prochain message dans...",sec, "secondes")

    total_sec += sec
    sleep(sec)

    paste_content(driver, input_box, msg[0])
    input_box.send_keys(Keys.RETURN)
    input_box.clear()


print("36 messages envoyés en", total_sec)
# Ferme le navigateur
driver.quit()
