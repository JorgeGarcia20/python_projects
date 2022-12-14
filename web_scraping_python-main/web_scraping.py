import bs4
import requests

# url
url = 'https://www.escueladirecta.com/courses'

# Request
result = requests.get(url)

soup = bs4.BeautifulSoup(result.text, 'lxml')

# Data extraction by element.
print('Data extraction by element')
page_title = soup.select('title')[0].getText()
print(page_title)


paragraph = soup.select('p')[3].getText()
print(paragraph)
print('\n')


# Data extraction by class
print('Data extraction by class')
subtitles = soup.select('div .course-listing-subtitle')

for subtitle in subtitles:
    print(f'-{subtitle.getText().strip()}')
print('\n')


# Image extraction
print('Image extraction')
url_image = soup.select('.course-box-image')[0]['src']
print(url_image)

img_1 = requests.get(url_image)


image = open('my_image.jpg', 'wb')
image.write(img_1.content)
image.close()
print('Saved image!')
