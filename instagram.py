from selenium import webdriver
from time import sleep
from tiktok import title, description
from video_editor import editing
from downloader import downloader

downloader()
sleep(5)
print("i'm fucking working")

editing()

print("editing done !")

url = "https://www.instagram.com/"
username = ""
password = ""
video_path = "tiktok-scraper/final_clip.mp4"

# options = webdriver.ChromeOptions()
# options.headless = True
driver = webdriver.Chrome(r"C:\Users\LENOVO\PycharmProjects\web scraping\chromedriver.exe")

driver.get(url)
sleep(3)


def login():
    try:
        username_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        password_input = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')

        username_input.send_keys(username)
        password_input.send_keys(password)

        login_button = driver.find_element_by_xpath("//button[@type='submit']")
        login_button.click()

        sleep(5)
        print("login done.")
    except Exception as e:
        print(e)


def home():
    driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
    driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]').click()
    print("home done.")


def upload():
    driver.get('https://www.instagram.com/tv/upload/')
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/form/div/div[1]/label/input').send_keys(video_path)
    sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/form/div/div[2]/div[4]/div/div/input').send_keys(title)
    sleep(2)
    driver.find_element_by_tag_name('textarea').send_keys(description)
    sleep(3)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/form/div/div[2]/div[7]/button').click()
    print("upload in progress.")


login()
home()
upload()

print("Done thanks for using InstaTik ! <3")
