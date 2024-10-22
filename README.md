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
- **-C eller --crawl-depth**: Djupet för webcrawlern (Hur många nivåer av länkar som ska följas.)

