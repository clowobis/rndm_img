import requests
from bs4 import BeautifulSoup as Bs
import random
import os


def get_url(num):
    req = requests.get("http://randomavatar.com/")
    bs1 = Bs(req.text, 'html.parser')
    img_urls = []
    for img in bs1.find_all('img', {'class': 'img-responsive MainSpace RAFade'}):
        img_urls.append(img['src'])
    r_img_url = random.sample(img_urls, min(num, len(img_urls)))
    return r_img_url


def take_img():
    r_urls = get_url(amount)
    if not os.path.exists('img'):
        os.makedirs('img')
    for idx, a_url in enumerate(r_urls):
        img_res = requests.get(a_url)
        if img_res.status_code == 200:
            img_name = f'image_{idx + 1}.jpg'
            img_path = os.path.join('img', img_name)
            with open(img_path, 'wb') as f:
                f.write(img_res.content)
            print(f'image saves: {img_path}')
        else:
            print(f'an error occurred {a_url}')


if __name__ == "__main__":
    amount = 5
    take_img()
