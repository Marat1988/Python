from bs4 import BeautifulSoup
import requests
import json

url = "https://ru.wikipedia.org/wiki/%D0%A1%D1%82%D1%80%D0%B0%D0%BD%D1%8B_%D0%95%D0%B2%D1%80%D0%BE%D0%BF%D1%8B_%D0%BF%D0%BE_%D0%BD%D0%B0%D1%81%D0%B5%D0%BB%D0%B5%D0%BD%D0%B8%D1%8E"

countries = {}


def get_data():
    page = requests.get(url)
    page_country = BeautifulSoup(page.text, 'html.parser')
    table_country = page_country.find('table', class_='wikitable').find('tbody').find_all('tr')
    for country in table_country[1:]:
        country_name = country.findAll('td')[1].find('span').get_text().replace(" ", "")
        flag_link = 'https:' + country.findAll('td')[1].find_all('img')[0]['src']
        print(flag_link)
        images_name_country_folder = "images/" + country_name + ".png"
        image_link_stream = requests.get(flag_link, stream=True)
        with open(images_name_country_folder, "wb") as image_file:
            for packet in image_link_stream.iter_content(1024):
                image_file.write(packet)
        population, *_ = country.findAll('td')[3].text.replace(" ", "").partition('[')
        is_growth = country.findAll('td')[2].find('span')
        if is_growth is None:
            is_growth = "Стабильность"
        elif is_growth.text == "▼":
            is_growth = False
        else:
            is_growth = True
        countries[country_name] = {'flag': images_name_country_folder,
                                   'is_growth': is_growth,
                                   'population': int(population)}


get_data()

with open("country.json", "w") as db_file:
    json.dump(countries, db_file, indent=4, ensure_ascii=False)
