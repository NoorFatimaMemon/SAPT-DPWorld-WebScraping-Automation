from Helper import Helper
import pandas as pd
import os
import logging
from seleniumbase import Driver
import time

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
        # File paths
        data_stored_file = 'DP_World\DP_World_Karachi_Data.csv'
        tracking_ids_file = 'DP_World\Tracking_IDs.csv'
        main_URL = "https://lfs.qict.com.pk/"
        headless = True

        # Logging setup
        logging.info(f"Checking if CSV file {data_stored_file} exists or needs to be created.")
        # Load already scraped Tracking IDs
        Scraped_Tracking_IDs = self.csv_creator(data_stored_file)

        # Load new Tracking IDs from CSV
        logging.info("Loading Tracking IDs from Tracking_IDs.csv")
        New_Tracking_IDs = pd.read_csv(tracking_ids_file)['Tracking_IDs'].tolist()

        # Start browser session
        count = 0
        driver = self.Helper.start_browser(main_URL, headless)

        for tracking_id in New_Tracking_IDs:
            if Scraped_Tracking_IDs is None or tracking_id not in Scraped_Tracking_IDs:
                # Restart browser after every 10 IDs
                if count > 0 and count % 10 == 0:
                    driver.quit()
                    logging.info("Restarting browser session after processing 10 IDs.")
                    driver = self.Helper.start_browser(main_URL, headless)  # Restart browser

                logging.info(f"Scraping Tracking ID: {tracking_id}")
                data = self.Helper.scraper(Tracking_ID=tracking_id, driver=driver)

                # Save scraped data
                df = pd.DataFrame([data])
                df.to_csv(data_stored_file, mode='a', index=False, header=False)
                logging.info(f"Tracking ID {tracking_id} saved to CSV.")

                count += 1

        # Ensure browser is closed at the end
        if driver:
            driver.quit()
            logging.info("Browser session closed. Scraping completed.")

test = Main()
test.main()