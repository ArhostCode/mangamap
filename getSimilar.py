from bs4 import BeautifulSoup
from selenium import webdriver
import json

options = webdriver.ChromeOptions()

all = json.loads("".join(open("all.json", encoding="UTF-8").readlines()))

data = {}

binary_yandex_driver_file = 'yandexdriver.exe'
driver = webdriver.Chrome(binary_yandex_driver_file, options=options)
i = 0
for manga in all:
    i += 1
    if i < 500:
        continue
    if i > 700:
        break

    manga_name = all[manga]
    manga_rus_name = manga

    driver.get(f'https://mangalib.me/{manga_name}')

    soup = BeautifulSoup(driver.page_source)
    if len(soup.select(".media-sidebar__cover img")) == 0:
        continue
    img = soup.select(".media-sidebar__cover img")[0]['src']
    if len(soup.find_all("div", {"class": "media-section media-section_slider"})) > 1:
        k = soup.find_all("div", {"class": "media-section media-section_slider"})[1]
    else:
        k = soup.find_all("div", {"class": "media-section media-section_slider"})[0]
    t = []
    for elem in k.find_all("div", {"class": "manga-list-item__name"}):
        t.append(elem.text.replace("\n", "").lstrip().rstrip())

    data[manga_rus_name] = {"name": manga_name, "img": img, "similar": t}

    print(data)


k = open("all-mangas-parsed500-700.json", "w", encoding="UTF-8")
k.write(json.dumps(data,ensure_ascii=False))

driver.quit()
