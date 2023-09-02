from bs4 import BeautifulSoup
import requests

root = 'https://subslikescript.com'
web_site = f'{root}/movies'

result = requests.get(web_site)

content = result.text

soup = BeautifulSoup(content, 'lxml')

pagination = soup.find('ul', class_='pagination')
pages = pagination.find_all('li', class_='page-item')
lastPage = pages[-2].text
links = []
for page in range(1, 5):
    web_site = f'{web_site}?page={page}'

    result = requests.get(web_site)

    content = result.text

    soup = BeautifulSoup(content, 'lxml')

    box = soup.find('article', class_='main-article')

    for link in box.find_all('a', href=True):
        links.append(link['href'])

    for link in links:
        try:
            web_site = f'{root}/{link}'

            result = requests.get(web_site)

            content = result.text

            soup = BeautifulSoup(content, 'lxml')

            box = soup.find('article', class_='main-article')

            title = box.find('h1').get_text()

            transcript = box.find('div', class_='full-script').get_text(strip=True, separator=' ')

            with open(f'{title}.txt', 'w') as file:
                file.write(transcript)
        except:
            pass
