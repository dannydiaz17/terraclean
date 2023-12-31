# Project Details

![TerraClean](https://github.com/dannydiaz17/terraclean/blob/main/terraclean.png)

### Welcome

I was tasked with the repair of [TerraClean's](https://terraclean.net) product database, as it had been compromised.
While initially tasked with manual data extraction for each product on various Wayback Machine URLs, I identified a more efficient approach. I compiled a comprehensive list of product category links, then leveraged the Wayback Machine's archive of the TerraClean product category pages to extract relevant product links and generate a "sites.txt" file. This facilitated the development of a custom web scraper, which iterated through the product links and automatically collected images, titles, and descriptions for each item. This significantly improved data collection accuracy and efficiency compared to manual copy-and-paste methods.

### The Issue

Faced with a critical data loss scenario, I tackled a seemingly insurmountable challenge. TerraClean's product database compromise, coupled with missing backups and the absence of alternative data sources, presented a complex obstacle. Manual extraction through Wayback Machine crawls, while feasible, was hampered by sluggish response times, rendering it an impractical solution.

### Planning

Seeking an efficient data acquisition method, I explored alternatives to manual extraction. Through web research, I discovered Beautiful Soup 4, which allowed me to analyze the target website's HTML structure and identify the tags encapsulating the desired data points (image, title, description). With this "map" in place, I focused on data output formatting. Recognizing the need for WooCommerce product CSV import on their new website, I tailored the data format accordingly.

[WooCommerce CSV Format](https://woo.com/document/product-csv-import-suite-column-header-reference/)

### Coding

#### Features:

##### Data Extraction:
	requests.get: Downloads the HTML content from each URL.
	BeautifulSoup: Parses the HTML using the 'html.parser' library.
	Specific tag selection: Identifies relevant data points based on HTML structure using class names and text extraction.

		*Example: Extracts part number from h3 element's span and description from div element.
##### Data Processing:
	make_spreadsheet: Converts extracted data to a Pandas dataframe with named columns.
	to_csv: Saves the dataframe as "terraclean.csv" without row indexes.
##### Error Handling:
	try-except: Catches any exceptions during data retrieval and prints the error message.
##### Looping and Progress Reporting:
	Iterates through the list of URLs in "sites.txt".
	Prints progress counter with current and total URL count.
##### Technical Skills Demonstrated:
	Python programming basics (imports, variables, functions, loops)
	Web scraping with requests and Beautiful Soup
	Data manipulation with Pandas
	Error handling and exception management
