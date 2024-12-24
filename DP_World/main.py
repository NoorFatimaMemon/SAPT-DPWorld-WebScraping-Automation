from Helper import Helper
import pandas as pd
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Main():
    Helper = Helper()
    def csv_creator(self, file_path):
        headers = [{'Tracking_ID':'Container_No.','Shipping_Line':'Shipping_Line','Size/Type':'Size/Type','Category':'Category',
                    'Status':'Status','Port_of_Discharge':'Port_of_Discharge','Destination':'Destination','Position':'Position',
                    'In_Time':'In_Time','Load_Time':'Load_Time','VIR_No':'VIR_No','Vessel':'Vessel','Voyage':'Voyage',
                    'Booking_No':'Booking_No',"Shipper_Seal":"Shipper_Seal","Line_Seal":"Line_Seal",'Standing':'Standing',
                    'Hold_Description':'Hold_Description','Pre-Gate_Arrival_Time':'Pre-Gate_Arrival_Time',"Truck_In_Time":"Truck_In_Time",
                    "Truck_In_Yard":"Truck_In_Yard"}]
        
        if os.path.exists(file_path): 
            print("The file exists.")
            TrackingIDs = pd.read_csv(file_path)['Container_No.'].tolist()
            print(TrackingIDs)
            return TrackingIDs
        else:
            print("The file does not exist. Therefore, creating one")
            df = pd.DataFrame(headers)
            df.to_csv(file_path, header=False, index=False)
            return None

    def main(self):
        # to check csv file containing container details exist or have to create one
        data_stored_file = 'DP_World\DP_World_Karachi_Data.csv'
        logging.info(f"--------------- Checking csv file {data_stored_file} exist or have to create one ---------------")
        Scraped_Tracking_IDs = self.csv_creator(data_stored_file)  

        # to get saved Tracking IDs to give them as input from Tracking_IDs csv file 
        logging.info("--------------- Getting Tracking IDs from Tracking_IDs csv file  ---------------")
        New_Tracking_IDs = pd.read_csv('DP_World\Tracking_IDs.csv')['Tracking_IDs'].tolist()
        main_URL = "https://lfs.qict.com.pk/"

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