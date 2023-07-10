from bs4 import BeautifulSoup

def html_page(page):
    return BeautifulSoup(page.text, 'html.parser')