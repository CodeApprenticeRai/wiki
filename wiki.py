import requests
from bs4 import BeautifulSoup

def starts_with_wiki_url(text):
    return text[:6] == "/wiki/"

'''
A function that
returns all the /wiki links
to a wikipedia page
'''
def get_page_wiki_links():
    origin_wiki_url = "/wiki/philosophy"
    page = requests.get("https://wikipedia.org" + origin_wiki_url)
    soup = BeautifulSoup(page.content, 'html.parser')
    out_links = soup.find_all('a')

    wiki_out_links = []
    for link in out_links:
        if link.has_attr('href') and starts_with_wiki_url(link.get('href')):
            wiki_out_links.append(link.get('href'))
    return wiki_out_links
