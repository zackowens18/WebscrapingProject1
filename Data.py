from selenium import webdriver

class Drive:  #Class for Drive 
    def __init__(self,name,price,price_per_gb=0,size=0):
        self.name = name
        self.price = float(price[1:])
        try:
            self.size = int(name[name.rfind('TB')-1])
        except:
            self.size = -1;
        if(self.size!=-1):
            self.price_per_gb = self.size*1000.0/self.price
        else:
            self.price_per_gb = 0

browser = webdriver.Chrome(r'C:\\Users\user\source\repos\WebScraper\WebScraper\chromedriver\chromedriver.exe')
file = open('hrefs.txt','r') # opens file after WebScraper is ran 
for line in file: # turns File into useable links
    links = line.split(";")

Drives = []
links = links[0:-1] # removes last links as they have issues 
for link in links: # breaks the website into data
    browser.get(link)
    n = browser.find_element_by_xpath('//*[@id="productTitle"]').text.strip() #name 
    p = browser.find_element_by_xpath('//*[@id="priceblock_ourprice"]').text.strip() #price
    
    temp_drive = Drive(n,p) 
    #print(temp_drive.name+str(temp_drive.size)+" "+str(temp_drive.price)+str(temp_drive.price_per_gb))
    length = len(Drives)
    i = 0
    same = 0
    while i < length:
        if Drives[i].name == temp_drive.name :
            same = 1 # checks if any drives are the same
        i +=1
    if same == 0:
        Drives.append(temp_drive)
print(len(Drives))
file_drives = open("drives.txt","w") #saves all drive data to a file 
for i in range(len(Drives)): # writes data using for-loop
    if(Drives[i].size != -1):
        print("writing"+str(i))
        file_drives.write(Drives[i].name+";"+str(Drives[i].price)+";"+str(Drives[i].price_per_gb)+";"+str(Drives[i].size)+"\n")
browser.quit() #ends file and browser
file_drives.close()


    





