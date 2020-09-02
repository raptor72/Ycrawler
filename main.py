import os
import logging
import asyncio
import aiohttp
import requests
from bs4 import BeautifulSoup

url = 'https://news.ycombinator.com'

def get_file(url):
    r = requests.get(url, allow_redirects=True)
    return r.content

def get_news_names(html):
    names = []
    soup = BeautifulSoup(html, 'lxml')
    blocks = soup.find_all('td', class_='title')
    # print(blocks)
    # logging.INFO(f'{blocks}')
    for block in blocks:
        try:
            link = block.find('a', class_='storylink').get('href')
            name = block.find('a', class_='storylink').get_text()
            names.append({name: link})
        except:
            continue
        # if link:
        #     print(link)
        #     print(name)
        # print(block)
        # print()
        # names.append(name)
    return names


def check_exists_topic(name, dir='topics'):
    # if not os.path.exists(dir):
    #     logging.info("Log directory does not exists")
    #     return
    if name in os.listdir(dir):
        logging.info("Topic already downloaded")
        return


def main():
    html = get_file(url)
    names = get_news_names(html)
    check_exists_topic(names[0].keys())

# def write_image(data):
#     dirname = None
#     filename = 'file-{}.jpeg'.format(int(time() * 1000))
#     with open(filename, 'wb') as file:
#         file.write(data)


# def get_current_news():

# async def fetch_content(url, session):
#     async with session.get(url, allow_redirects=True) as response:
#         data = await response.read()



if __name__ == "__main__":
    print(main())

