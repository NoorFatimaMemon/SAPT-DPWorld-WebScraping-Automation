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
        # File paths
        data_stored_file = 'Sapt\Sapt_Data.csv'
        tracking_ids_file = 'Sapt\Tracking_IDs.csv'
        main_URL = "https://sapt.com.pk/"
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
                self.Helper.scraper(Tracking_ID=tracking_id, driver=driver, data_stored_file=data_stored_file)
                count += 1

        # Ensure browser is closed at the end
        if driver:
            driver.quit()
            logging.info("Browser session closed. Scraping completed.")


test = Main()
test.main()