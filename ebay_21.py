#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
#|r|e|d|a|n|d|g|r|e|e|n|.|c|o|.|u|k|
#+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
import os
import datetime
import sys
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection

# API key is set in .env file - create and save in same directory
from dotenv import load_dotenv
load_dotenv()
API_KEY=os.getenv('api_key')

class Ebay_21(object):
    def __init__(self, API_KEY,st):
        self.api_key = API_KEY
        self.st = st
    
    
    def fetch(self):
        try:
            api = Connection(appid=self.api_key, config_file=None, siteid="EBAY-GB")
            response = api.execute('findItemsAdvanced', {'keywords': st})
            
            #The total number of items found that match the search criteria in your request
            print(f"Total items {response.reply.paginationOutput.totalEntries}\n")
            
            for item in response.reply.searchResult.item:
                print(f"Title: {item.title}, Price: {item.sellingStatus.currentPrice.value}")
                print(f"Buy it now available : {item.listingInfo.buyItNowAvailable}")
                print(f"Country : {item.country}")
                print(f"End time :{item.listingInfo.endTime}")
                print(f"URL : {item.viewItemURL}")
                try:
                    print(f"Watchers : {item.listingInfo.watchCount}\n")
                except:
                    pass
  
        except ConnectionError as e:
            print(e)
            print(e.response.dict())
    
    def parse(self):
        pass
    

# main driver
if __name__=='__main__':
    
    # check if keyword was passed when calling script
    if len(sys.argv) ==1:
        print("Needs at least 1 search keywowrd")
        sys.exit(1)
    
    # set search term as 'st' and create instance of Ebay_21 to make API call 
    st = sys.argv[1]
    e = Ebay_21(API_KEY, st)
    e.fetch()
    e.parse()