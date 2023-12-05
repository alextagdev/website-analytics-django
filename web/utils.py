# web/utils.py

import socket
from urllib.parse import urlparse

def get_ip_address(url):
    try:
        # Adaugă http:// sau https:// la începutul URL-ului, dacă nu este deja prezent
        if not url.startswith('http://') and not url.startswith('https://'):
            url = 'http://' + url

        # Obține adresa IP
        hostname = urlparse(url).hostname
        if hostname:
            ip_address = socket.gethostbyname(hostname)
            return ip_address
        else:
            return f"Error: Unable to extract hostname from the URL"
    except socket.error as e:
        return f"Error: {e}"
# web/utils.py

import requests
from bs4 import BeautifulSoup
from .utils import get_ip_address  # Importă funcția get_ip_address din același modul

def get_website_info(url):
    try:
        # Realizează o cerere HTTP către site
        print("Sending HTTP request to", url)
        response = requests.get(url)
        response.raise_for_status()  # Aruncă o excepție dacă statusul HTTP indică o eroare (de exemplu, 404)
        
        # Utilizează BeautifulSoup pentru a parsa conținutul HTML
        print("Parsing HTML content")
        soup = BeautifulSoup(response.content, 'html.parser')

        # Afișează adresa IP
        ip_address = get_ip_address(url)
       

        # Aici, poți selecta și extrage informațiile dorite din HTML folosind metodele BeautifulSoup
        # Exemplu: preia lungimea conținutului HTML și numărul de caractere din el
        content_length = len(str(response.content))
        char_count = len(str(soup))

        return {
            'ip_address': ip_address,
            'bytes_received': content_length,
            'content_displayed': char_count
        }
    except requests.exceptions.RequestException as e:
        # Gestionarea erorilor: afișează un mesaj de eroare sau întoarce o valoare specială
        print(f"Error accessing {url}: {e}")
        return {
            'error': f"Error accessing {url}: {e}"
        }
def extract_meta_info(url):
    # Realizați cererea HTTP pentru a obține conținutul paginii web
    response = requests.get(url)
    if response.status_code == 200:
        # Utilizați BeautifulSoup pentru a parsa conținutul HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extrageți titlul și descrierea meta
        title_tag = soup.find('title')
        meta_description = soup.find('meta', attrs={'name': 'description'})
        meta_image = soup.find('meta', attrs={'property': 'og:image'})

        # Returnați rezultatele
        return {
            'title': title_tag.text if title_tag else None,
            'description': meta_description['content'] if meta_description else None,
            'image_url': meta_image['content'] if meta_image else None,
        }
    else:
        print(f"Error {response.status_code}: Unable to fetch the page content.")
        return None