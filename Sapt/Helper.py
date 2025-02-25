from seleniumbase import Driver
from selenium.webdriver.common.by import By
import logging
import time
import pandas as pd

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Helper():
    def start_browser(self, main_URL, headless):
        logging.info("--------------- Starting new browser session ---------------")
        driver = Driver(uc=True, undetectable=True, headless=headless)

        logging.info(f"Accessing -------------> {main_URL}")
        driver.get(main_URL)
        driver.implicitly_wait(50)

        try:
            # To Click the Dialog box
            logging.info("Clicking on Dialog Box if present")
            try:
                dialog_box = driver.find_element(By.XPATH,'//div[@class="modal-dialog"]//div[@class="modal-content"]')
            except:
                dialog_box = driver.find_element(By.XPATH,'//div[@class="modal-dialog"]//div[@class="modal-header"]')

            time.sleep(0.5)
            if dialog_box:
                driver.refresh()
                time.sleep(0.5)
                close_button = driver.find_element(By.XPATH, '//div[@class="modal-dialog"]//div[@class="modal-content"]//div[@class="wpb_close_btn"]')
                close_button.click()  

            # Scroll to the "Find your Container" element
            container_element = driver.find_element(By.XPATH, '(//div[@class="dt_row container row"])[2]')
            time.sleep(0.5)
            # Scroll the element into view
            driver.execute_script("arguments[0].scrollIntoView();", container_element)

            # Click on "Find your Container" button
            logging.info("Clicking on Find your Container button")
            container_inquiry_button = driver.find_element(By.XPATH, '//h1[@class="day_time"]//span[text()= "Find Your"]')
            time.sleep(0.5)
            driver.execute_script("arguments[0].scrollIntoView(); window.scrollBy(0, -100);", container_inquiry_button)
            container_inquiry_button.click()
            time.sleep(0.5)
            logging.info('"Find your Container" button Clicked')

        except Exception as e:
            logging.error(f"Error interacting with the page: {e}")

        return driver
    
    def scraper(self, Tracking_ID, driver, data_stored_file):
        # To Enter Tracking ID or Container No.
        logging.info("--------------- Entering Tracking ID or Container No. ---------------")
        Tracking_ID_input = driver.find_element(By.XPATH, '//input[@id="ContainerId"]')
        Tracking_ID_input.click()
        Tracking_ID_input.send_keys(Tracking_ID)
        logging.info("--------------- Entered Tracking ID or Container No. ---------------")

        # To Click on Search Button
        logging.info("--------------- Clicking on Search Button ---------------")
        search_button = driver.find_element(By.XPATH, '//input[@id="SearchContainer"]')
        # Get the bounding rectangle of the search button
        location = search_button.rect  # dictionary with x, y, width, height
        # Calculate the x and y coordinates for the center of the element
        x = location['x'] + location['width'] / 2
        y = location['y'] + location['height'] / 2
        # Click using JavaScript at the calculated coordinates
        driver.execute_script("document.elementFromPoint(arguments[0], arguments[1]).click();", x, y)
        time.sleep(2)
        logging.info("--------------- Search Button Clicked ---------------")
        time.sleep(1)

        # To Click on Tracking ID to get its details
        logging.info("--------------- Clicking on Tracking ID to get details ---------------")
        TrackingIDs_links = driver.find_elements(By.XPATH, '//a[@href="#detailView"]')
        for TrackingIDs_link in TrackingIDs_links:
            TrackingIDs_link.click()
            time.sleep(2)
            logging.info("--------------- Tracking ID Clicked to get details ---------------")

            # To Get Container Details
            logging.info("--------------- Getting Container Details ---------------")
            try:
                Owner = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Owner"]//parent::tr//b)[1]').text
            except:
                Owner = ''

            print(f"Owner: {Owner}")

            try:
                Shipping_Bill_No = driver.find_element(By.XPATH, '(//td[normalize-space(.)="BL/ Shipping Bill No."]//parent::tr//b)[2]').text
            except:
                Shipping_Bill_No = ''

            print(f"BL/ Shipping Bill No.: {Shipping_Bill_No}")
            
            try:
                Container_SizeType = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Container Size/Type"]//parent::tr//td)[last()]').text
            except:
                Container_SizeType = ''

            print(f"Container Size/Type: {Container_SizeType}")

            try:
                Category = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Category"]//parent::tr//td)[2]').text
            except:
                Category = ''

            print(f"Category: {Category}")
            
            try:
                Status = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Status"]//parent::tr//td)[last()]').text
            except:
                Status = ''

            print(f"Status: {Status}")
            
            try:
                Vessel_Voyage = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Vessel Voyage"]//parent::tr//td)[2]').text
            except:
                Vessel_Voyage = ''

            print(f"Vessel Voyage: {Vessel_Voyage}")

            try:
                VIR_No = driver.find_element(By.XPATH, '(//td[normalize-space(.)="VIR No"]//parent::tr//td)[last()]').text
            except:
                VIR_No = ''

            print(f"VIR No: {VIR_No}")

            try:
                ETA = driver.find_element(By.XPATH, '(//td[normalize-space(.)="ETA"]//parent::tr//td)[2]').text
            except:
                ETA = ''

            print(f"ETA: {ETA}")

            try:
                ETD = driver.find_element(By.XPATH, '(//td[normalize-space(.)="ETD"]//parent::tr//td)[last()]').text
            except:
                ETD = ''

            print(f"ETD: {ETD}")

            try:
                Discharge_Time = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Discharge Time"]//parent::tr//td)[2]').text
            except:
                Discharge_Time = ''

            print(f"Discharge Time: {Discharge_Time}")

            try:
                Load_Time = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Load Time"]//parent::tr//td)[last()]').text
            except:
                Load_Time = ''

            print(f"Load Time: {Load_Time}")

            try:
                DO_Issuance_Date = driver.find_element(By.XPATH, '(//td[normalize-space(.)="DO Issuance Date"]//parent::tr//td)[2]').text
            except:
                DO_Issuance_Date = ''

            print(f"DO Issuance Date: {DO_Issuance_Date}")

            try:
                DO_Expiry_Date = driver.find_element(By.XPATH, '(//td[normalize-space(.)="DO Expiry Date"]//parent::tr//td)[last()]').text
            except:
                DO_Expiry_Date = ''

            print(f"DO Expiry Date: {DO_Expiry_Date}")

            try:
                GateIn_Time = driver.find_element(By.XPATH, '(//td[normalize-space(.)="GateIn Time"]//parent::tr//td)[2]').text
            except:
                GateIn_Time = ''

            print(f"GateIn Time: {GateIn_Time}")

            try:
                GateOut_Time = driver.find_element(By.XPATH, '(//td[normalize-space(.)="GateOut Time"]//parent::tr//td)[last()]').text
            except:
                GateOut_Time = ''

            print(f"GateOut Time: {GateOut_Time}")

            try:
                Origin = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Origin"]//parent::tr//td)[2]').text
            except:
                Origin = ''

            print(f"Origin: {Origin}")

            try:
                Destination = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Destination"]//parent::tr//td)[last()]').text
            except:
                Destination = ''

            print(f"Destination: {Destination}")

            try:
                Custom_Seal_No = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Custom Seal No."]//parent::tr//td//span)[1]').text
            except:
                Custom_Seal_No = ''

            print(f"Custom Seal No.: {Custom_Seal_No}")

            try:
                Line_Seal_No = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Line Seal No."]//parent::tr//td//span)[last()]').text
            except:
                Line_Seal_No = ''

            print(f"Line Seal No.: {Line_Seal_No}")

            try:
                Security_Seal_No = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Security Seal No."]//parent::tr//td//span)[1]').text
            except:
                Security_Seal_No = ''

            print(f"Security Seal No.: {Security_Seal_No}")

            try:
                Other_Seal_No = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Other Seal No."]//parent::tr//td//span)[last()]').text
            except:
                Other_Seal_No = ''

            print(f"Other Seal No.: {Other_Seal_No}")

            try:
                Custom_Status = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Custom Status"]//parent::tr//td//span)[1]').text
            except:
                Custom_Status = ''

            print(f"Custom Status: {Custom_Status}")

            try:
                Current_Position = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Current Position"]//parent::tr//td)[last()]').text
            except:
                Current_Position = ''

            print(f"Current Position: {Current_Position}")

            try:
                Commodity = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Commodity"]//parent::tr//td)[2]').text
            except:
                Commodity = ''

            print(f"Commodity: {Commodity}")

            try:
                Weight = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Weight"]//parent::tr//td)[last()]').text
            except:
                Weight = ''

            print(f"Weight: {Weight}")

            try:
                Weighment = driver.find_element(By.XPATH, '//td[normalize-space(.)="Weighment"]//parent::tr//td//span').text
            except:
                Weighment = ''

            print(f"Weighment: {Weighment}")

            try:
                Scanning = driver.find_element(By.XPATH, '(//td[normalize-space(.)="Scanning"]//parent::tr//td)[last()]').text
            except:
                Scanning = ''

            print(f"Scanning: {Scanning}")

            try:
                Present_Holds = driver.find_element(By.XPATH, '//td[normalize-space(.)="Present Holds"]//parent::tr//td//span').text
            except:
                Present_Holds = ''

            print(f"Present Holds: {Present_Holds}")

            data = {'Owner':Owner.strip(),'BL/ Shipping Bill No.':Shipping_Bill_No.strip(),'Tracking ID':Tracking_ID,
                'Container Size/Type':Container_SizeType.strip(),'Category':Category.strip(),'Status':Status.strip(),
                'Vessel Voyage':Vessel_Voyage.strip(),'VIR No':VIR_No.strip(),'ETA':ETA.strip(),'ETD':ETD.strip(),'Discharge Time':Discharge_Time.strip(),
                'Load Time':Load_Time.strip(),'DO Issuance Date':DO_Issuance_Date.strip(),'DO Expiry Date':DO_Expiry_Date.strip(),
                'GateIn Time':GateIn_Time.strip(),'GateOut Time':GateOut_Time.strip(),'Origin':Origin.strip(),'Destination':Destination.strip(),
                'Custom Seal No.':Custom_Seal_No.strip(),'Line Seal No.':Line_Seal_No.strip(),'Security Seal No.':Security_Seal_No.strip(),
                'Other Seal No.':Other_Seal_No.strip(),'Custom Status':Custom_Status.strip(),'Current Position':Current_Position.strip(),
                'Commodity':Commodity.strip(),'Weight':Weight.strip(),'Weighment':Weighment.strip(),'Scanning':Scanning.strip(),
                'Present Holds':Present_Holds.strip()}
        
            print(data)
            logging.info(f"Tracking ID ------------> {Tracking_ID} data is scraped!!!!")

            # Save scraped data
            df = pd.DataFrame([data])
            df.to_csv(data_stored_file, mode='a', index=False, header=False)
            logging.info(f"Tracking ID {Tracking_ID} saved to CSV.")
         
        time.sleep(1)
        logging.info("--------------- Got all Container Details ---------------")
        # Scroll to the top of the page
        driver.execute_script("window.scrollTo(0, 0);")
        # To Clear the Tracking ID input field
        Tracking_ID_input = driver.find_element(By.XPATH, '//input[@id="ContainerId"]')
        Tracking_ID_input.click()
        Tracking_ID_input.clear()