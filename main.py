import argparse
from fetch_url import fetch_page
from vulnerabilities import analyze_page
from classes import ScanResult, DirEnumeration, CrawlerResults
from crawler import crawl_website

def main():
    parser = argparse.ArgumentParser(description="Web vulnerbility scanner")
    parser.add_argument("url",help="URL to scan")
    parser.add_argument("-C","--crawl-depth", type=int, help="Depth for webcrawler (t.ex -C 3)")
    scan_result = ScanResult()
    dir_enumertion = DirEnumeration()
    
    args = parser.parse_args()

    if args.crawl_depth is not None:
        if args.crawl_depth <= 0:
            print("Depth cant be negativ!")
            return

    if args.crawl_depth:
        print(f"\nScanning URL: {args.url} with depth {args.crawl_depth}")
        crawl_result = CrawlerResults()
        page_content = fetch_page(args.url,scan_result,dir_enumertion)
        if page_content:
            analyze_page(page_content,scan_result)
            crawl_website(args.url,crawl_result,args.crawl_depth)
        print("-"*40)
        print("    Crawler Data\n")
        crawl_result.display_results()
        
    else:
        print(f"Scanning URL: {args.url}")
        scan_result = ScanResult()
        page_content = fetch_page(args.url,scan_result,dir_enumertion)
        if page_content: 
            analyze_page(page_content,scan_result)
    print("-"*40)
    scan_result.print_results()
    print("-"*40)
    dir_enumertion.print_results()


if __name__ == "__main__":
    main()