class ScanResult:
    def __init__(self):
        self.warnings = []

    def add_warning(self,message):
        self.warnings.append(message)

    def print_results(self):
        if not self.warnings:
            print("No vulnerabilitys!")
        else:
            print("\n   Vulnerabilitys:\n")
            for warning in self.warnings:
                print(f"- {warning}")
        print("-"*40)

class DirEnumeration:
    def __init__(self):
        self.dir = []
    def add_warning(self,message):
        self.dir.append(message)
    def print_results(self):
        if not self.dir:
            print("No directories found in the enumeration!")
        else:
            print("\n   Enumerations found:\n")
            for enumeration in self.dir:
                print(f"- {enumeration}")
        print("-"*40)

class CrawlerResults:
    def __init__(self):
        self.pages = {}
    def add_page(self,url, metadata = None):
        """
        Lägger till  en sida till reultatet.
        :param url: URL för sidan.
        :param metadata: Eventuell extra informtaion om sidan (title, antal länkar, etc.)
        """
        if url not in self.pages:
            self.pages[url] = {
                "metadata": metadata or {},
                "sub_links": []
            } 
    def add_link_to_page(self,parent_url,sub_link):
        """
        Lägg till en sub-link till redan sparad sida.
        :param parent_url: URLn där sublinken hittades.
        :param sub_link: URL för hittad sublink
        """           
        if parent_url in self.pages:
            self.pages[parent_url]["sub_links"].append(sub_link)
    def display_results(self):
        """
        Visar alla hittade sidor och deras länkar på ett strukturerat sätt.
        """
        for url,data in self.pages.items():
            print(f"URL: {url}")
            if data["metadata"]:
                for key, value in data["metadata"].items():
                    print(f"{key}:{value}")
                if data["sub_links"]:
                    print(" Sub_links:")
                    for link in data["sub_links"]:
                        print(f"    -{link}")
                print("-"*40)