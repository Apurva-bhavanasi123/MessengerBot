
def fetch_image_urls(query:str, max_links_to_fetch:int, wd, sleep_between_interactions:int=1):
    
    # build the google query
    search_url = "https://www.google.com/search?safe=off&site=&tbm=isch&source=hp&q={q}&oq={q}&gs_l=img"

    # load the page
    wd.get(search_url.format(q=query))
    
    image_urls = set()
    image_count = 0
    results_start = 0
    while image_count < max_links_to_fetch:
       # scroll_to_end(wd)

        # get all image thumbnail results
        smallImages = wd.find_elements_by_class_name("Q4LuWd")
        number_results = len(smallImages)
        
       # print(f"Found: {number_results} search results. Extracting links from {results_start}:{number_results}")
        
        for img in smallImages[results_start:number_results]:
            # try to click every thumbnail such that we can get the real image behind it
            try:
                img.click()
                
            except Exception:
                continue

            # extract image urls    
            actual_images = wd.find_elements_by_class_name('n3VNCb')
            print(len(actual_images))
            for actual_image in actual_images:
                
                if actual_image.get_attribute('src') and 'http' in actual_image.get_attribute('src'):
                    image_urls.add(actual_image.get_attribute('src'))

            image_count = len(image_urls)

            if len(image_urls) >= max_links_to_fetch:
               
                break
       
            load_more_button = wd.find_element_by_css_selector(".mye4qd")
            if load_more_button:
                wd.execute_script("document.querySelector('.mye4qd').click();")

        # move the result startpoint further down
        results_start = len(smallImages)

    return image_urls
from selenium import webdriver



driver = webdriver.Chrome()


k=fetch_image_urls("memes about christino ronaldo",10,driver)