from Helper import Helper
import pandas as pd
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Main():
    Helper = Helper()
    def csv_creator(self, file_path):
        headers = [{'Owner':'Owner','BL/ Shipping Bill No.':'BL/ Shipping Bill No.','Tracking ID':'Container No.',
                    'Container Size/Type':'Container Size/Type','Category':'Category','Status':'Status',
                    'Vessel Voyage':'Vessel Voyage','VIR No':'VIR No','ETA':'ETA','ETD':'ETD','Discharge Time':'Discharge Time',
                    'Load Time':'Load Time','DO Issuance Date':'DO Issuance Date','DO Expiry Date':'DO Expiry Date',
                    'GateIn Time':'GateIn Time','GateOut Time':'GateOut Time','Origin':'Origin','Destination':'Destination',
                    'Custom Seal No.':'Custom Seal No.','Line Seal No.':'Line Seal No.','Security Seal No.':'Security Seal No.',
                    'Other Seal No.':'Other Seal No.','Custom Status':'Custom Status','Current Position':'Current Position',
                    'Commodity':'Commodity','Weight':'Weight','Weighment':'Weighment','Scanning':'Scanning',
                    'Present Holds':'Present Holds'}]
        
        if os.path.exists(file_path): 
            print("The file exists.")
            TrackingIDs = pd.read_csv(file_path)['Container No.'].tolist()
            print(TrackingIDs)
            return TrackingIDs
        else:
            print("The file does not exist. Therefore, creating one")
            df = pd.DataFrame(headers)
            df.to_csv(file_path, header=False, index=False)
            return None

    def main(self):
        # to check csv file containing container details exist or have to create one
        data_stored_file = 'Sapt\Sapt_Data.csv'
        logging.info(f"--------------- Checking csv file {data_stored_file} exist or have to create one ---------------")
        Scraped_Tracking_IDs = self.csv_creator(data_stored_file)  

        # to get saved Tracking IDs to give them as input from Tracking_IDs csv file 
        logging.info("--------------- Getting Tracking IDs from Tracking_IDs csv file  ---------------")
        New_Tracking_IDs = pd.read_csv('Sapt\Tracking_IDs.csv')['Tracking_IDs'].tolist()
        main_URL = "https://sapt.com.pk/"

        for Tracking_ID in New_Tracking_IDs:
            if Scraped_Tracking_IDs is None or Tracking_ID not in Scraped_Tracking_IDs:
                logging.info(f"--------------- Beginning scraping Tracking ID/Container No. {Tracking_ID} details ---------------")
                data = self.Helper.scraper(main_URL=main_URL, Tracking_ID=Tracking_ID, headless=True)
                df = pd.DataFrame([data])
                logging.info(f"--------------- Storing scraping Tracking ID/Container No. {Tracking_ID} details ---------------")
                df.to_csv(data_stored_file, mode='a', index=False, header=False) 
                print(f"This Tracking ID '{Tracking_ID}' is scraped")

test = Main()
test.main()