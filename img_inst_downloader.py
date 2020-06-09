import requests
from bs4 import BeautifulSoup
import sys


def check_request(link):
    try:
        response = requests.get(link)
        html = response.text
        return html
    except:
        print('An error was occured, check your link or/and your connection')
        sys.exit()


def find_photo_with_parsing(request_url):
    soup = BeautifulSoup(request_url, 'lxml')
    img_url = soup.find(name='meta', attrs={'property':'og:image'}).get('content')
    return img_url


def download_photo(only_image_link):
    img_name = only_image_link[-25:-6]
    req_url = requests.get(only_image_link)
    with open(img_name + '.jpg', 'ab') as file:
        file.write(req_url.content)

    print('Success, photo was downloaded')

def main():
    link = input('Enter your image link\n')
    request_url = check_request(link)
    only_image_link = find_photo_with_parsing(request_url)
    download_photo(only_image_link)

if __name__ == '__main__':
    main()
