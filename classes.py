from bs4 import BeautifulSoup, NavigableString
import cloudscraper
from csv import writer

def scrap_price(direccio):
    scraper = cloudscraper.create_scraper()
    cpu = scraper.get(direccio).text

    cpu_soup = BeautifulSoup(cpu, 'html.parser')

    cpu_price = cpu_soup.find('div', attrs={'class': 'precioMain h1'})

    preu = cpu_price.text[:-1]

    preu = preu.replace('\n', '')

    disponibilitat = cpu_soup.find('button', attrs={'id': 'add-cart'})

    if disponibilitat is None:
        disponible = "No"
    else:
        disponible = 'si'
    return preu, disponible

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


