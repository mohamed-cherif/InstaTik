from selenium import webdriver
from time import sleep
from tiktok import chosen_videos


def downloader():
    vid_links = chosen_videos
    success = ""
    options = webdriver.ChromeOptions()
    options.headless = True
    prefs = {"download.default_directory": r"C:\Users\LENOVO\PycharmProjects\tiktok-scraper\clips"}
    options.add_experimental_option("prefs", prefs)

    for vid_link in vid_links:
        try:
            driver = webdriver.Chrome(r"C:\Users\LENOVO\PycharmProjects\web scraping\chromedriver.exe", options=options)
            driver.get("https://musicaldown.com/")
            sleep(1)
            input_box = driver.find_element_by_xpath('//*[@id="link_url"]')
            input_box.send_keys(vid_link)
            btn = driver.find_element_by_xpath('//*[@id="submit-form"]/div/div[2]/button')
            btn.click()
            sleep(1)
            download = driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[2]/a[1]')
            download.click()
            print("Download SUCESSFUL !")
            sleep(10)
            driver.quit()
            sleep(5)
        except Exception as e:
            print("error during the process")
            print(e)

