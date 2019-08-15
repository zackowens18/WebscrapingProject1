from selenium import webdriver


#How to webscrape Amazon 
browser = webdriver.Chrome(r'C:\\Users\user\source\repos\WebScraper\WebScraper\chromedriver\chromedriver.exe')
browser.get('https://www.amazon.com') 
search = browser.find_element_by_id('twotabsearchtextbox')
search.send_keys('Portable hard drives')
search.submit() #preforms search


links_objects = browser.find_elements_by_xpath('//a[@href]') #object with all links
links = [] 
file_hrefs = open("hrefs.txt","w") # writes to a file to be used in other scripts


lastLink = links_objects[2].get_attribute("href")


for i in range(len(links_objects)-3): # elimates some unneeded links by removing duplicates 
    link = links_objects[i]
    if(("External" in link.get_attribute("href")) and lastLink!=link.get_attribute("href")):
        links.append(link.get_attribute("href"))
        lastLink = link.get_attribute("href") # sets current to last before next iteration
        file_hrefs.write(link.get_attribute("href")+";")
        print(link.get_attribute("href")) # prints all links
browser.quit()
file_hrefs.close()



    

 