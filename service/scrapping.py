import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

load_dotenv()
class ScrappingService:
    def __init__(self):
       self.api_key = os.getenv('FIRECRAWL_API_KEY')
       self.api_url = os.getenv('FIRECRAWL_API_URL')

       self.app = FirecrawlApp(api_key=self.api_key, api_url=self.api_url)

    def scrape_website(self,url, collection_name):
        try:
            map_result = self.app.map_url(url)

            if hasattr(map_result, 'links'):
                links = map_result.links
            elif hasattr(map_result,'data') and hasattr(map_result.data,'links'):
                links = map_result.data.links
            else: 
                links =getattr(map_result,'links',[])
            if not links:
                raise Exception("No links found to scrape.")
            print(f"Found {len(links)} links to scrape.")


            scrape_result = self.app.batch_scrape_urls(links)
            if hasattr(scrape_result, 'data'):
                scraped_data = scrape_result.data
            else: 
                scraped_data = scrape_result.get('data',[]) if hasattr (scrape_result,'get') else [] 