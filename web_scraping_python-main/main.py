import bs4
import requests


url = 'https://books.toscrape.com/catalogue/page-{}.html'

higt_rating_books = []

for page in range(1, 51):

    url_page = url.format(page)
    result = requests.get(url_page)
    soup = bs4.BeautifulSoup(result.text, 'lxml')

    books = soup.select('.product_pod')

    # loop in books
    for book in books:
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0:

            book_title = book.select('a')[1]['title']
            higt_rating_books.append(book_title)

# Show the results
for title in higt_rating_books:
    print(f'- {title}')
