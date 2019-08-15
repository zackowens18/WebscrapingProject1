# prompts user for application runs of the two applications
i = input("Run WebScrapper to get Links for products:")
if(i[0]=='y' or i[0]=='Y'):
    import WebScraper
i2 = input("Run Data collection on products:")
if(i2[0]=='y' or i2[0]=='Y'):
    import Data
