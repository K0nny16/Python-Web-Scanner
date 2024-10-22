# Web Vulnerability Scanner

## Projektbeskrivning
Detta är en webbaserad scanner byggd i Python som kan crawla webbsidor och analysera dem för olika säkerhetsaspekter. Den kan även hämta detaljerad information från sidor som titlar, meta-beskrivningar, nyckelord och antal länkar, samt kontrollera om specifika säkerhetshuvuden saknas.

## Funktioner
- **Web Crawler**: Följer länkar på en webbplats upp till ett angivet djup.
- **Meta-Data Extraction**: Samlar in titlar, meta-beskrivningar och nyckelord från sidor.
- **Link Analysis**: Hittar och klassificerar länkar som interna eller externa.
- **Security Header Check**: Analyserar sidor för att identifiera saknade säkerhetshuvuden som `Content-Security-Policy` och `Strict-Transport-Security`.
- **SQL Injection Test**: Genomför enkla tester för att upptäcka potentiella SQL-injektioner.

## Installation

### Klona projektet
```bash
git clone <URL till ditt repo>
cd <mappnamn>
```
### Skapa och Aktivera Virtuell Miljö
```bash
python -m venv venv
source venv/bin/activate
```
### Installera Dependencies
```bash
pip install -r requirements.txt
```

## Argument och Flaggor
- **URL**: Den URL som ska skannas eller crawlas.
- **-C** eller **--crawl-depth**: Djupet för webcrawlern (Hur många nivåer av länkar som ska följas.)

## Crawler
Crawlern kommer att besöka webbsidor och samla in följande information:
- Sidans title
- Meta-beskrivningar och nyckelord
- Antal bilder
- Interna och externa länkar

## Security Analyzer 
Analyserar sidor för:
- Saknade säkerhetshuvuden som `Content-Security-Policy` och `STS`
- Möjliga SQL-injektioner genom att skicka test-sträng


## Exempel data

Scanning URL: https://juice-shop.herokuapp.com with depth 2
Pagetitle: OWASP Juice Shop
----------------------------------------
    Crawler Data

URL: https://juice-shop.herokuapp.com
Title:OWASP Juice Shop
Description:Probably the most modern and sophisticated insecure web application
Keywords: test, domain
Image_count:4
External_links_count:3
Internal_links_count:1
----------------------------------------

   Vulnerabilitys:

- Content-Security-Policy missing!
- Strict-Transport-Security missing!
- X-XSS-Protection missing!
- Permissions-Policy missing!
- Referrer-Policy missing!
----------------------------------------

   Enumerations found:

- Directory found: https://juice-shop.herokuapp.com/admin/
- Directory found: https://juice-shop.herokuapp.com/login/
- Directory found: https://juice-shop.herokuapp.com/backup/
- Directory found: https://juice-shop.herokuapp.com/config/
- Directory found: https://juice-shop.herokuapp.com/test/
- Directory found: https://juice-shop.herokuapp.com/staging/
----------------------------------------