from bs4 import BeautifulSoup
import requests

def crawl(url, visited, crawl_result, depth, max_depth,max_links = 100):
    """
    Rekursiv funktion för att följa länkar och analysera sidor.
    """
    if depth > max_depth or url in visited or len(visited) >= max_links:
        return
    visited.add(url)
    
    try:
        #Försök till anpassning så att den inte fastnar i en loop
        response = requests.get(url, timeout=10, allow_redirects=True)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Samla mer data från sidan
        title = soup.title.string if soup.title else "No title"
        
        # Hämta meta-description och meta-keywords
        meta_description = soup.find("meta", attrs={"name": "description"})
        description = meta_description["content"] if meta_description else "No description"
        
        meta_keywords = soup.find("meta", attrs={"name": "keywords"})
        keywords = meta_keywords["content"] if meta_keywords else "No keywords"

        # Samla antal bilder
        image_count = len(soup.find_all("img"))

        # Räkna externa och interna länkar
        external_links = []
        internal_links = []
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith("http"):
                if url in href:  # Kontrollerar om länken är intern
                    internal_links.append(href)
                else:
                    external_links.append(href)

        # Lägg till sidan i crawl-resultat med extra metadata
        crawl_result.add_page(url, metadata={
            "Title": title,
            "Description": description,
            "Keywords": keywords,
            "Image_count": image_count,
            "External_links_count": len(external_links),
            "Internal_links_count": len(internal_links)
        })

        # Hitta och analysera alla länkar för att fortsätta crawling
        for link in soup.find_all('a', href=True):
            href = link['href']
            if href.startswith("http"):
                crawl(href, visited, crawl_result, depth + 1, max_depth)

    except requests.RequestException as e:
        print(f"Failed to crawl {url}: {e}")
        return
    
def crawl_website(url,crawl_result,max_depth):
    visited = set()
    crawl(url,visited,crawl_result,0,max_depth)
