from seleniumbase import Driver
from selenium.webdriver.common.by import By
import logging
import time

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
            # Scroll to "General Public Options"
            logging.info("Scrolling to 'General Public Options'.")
            general_public_options = driver.find_element(By.XPATH, '//h2[text()="General Public Options"]')
            driver.execute_script("arguments[0].scrollIntoView();", general_public_options)
            time.sleep(0.5)

            # Click on "Container Inquiry"
            logging.info("Clicking 'Container Inquiry' button.")
            container_inquiry_button = driver.find_element(By.XPATH, 
                "//h3[contains(normalize-space(.), 'Container') and contains(normalize-space(.), 'Inquiry')]"
                "//parent::div//button[normalize-space(text()) = 'Click Here']")
            container_inquiry_button.click()
            time.sleep(1)

        except Exception as e:
            logging.error(f"Error interacting with the page: {e}")

        return driver

    def scraper(self, Tracking_ID, driver):        
        # To Enter Tracking ID or Container No.
        logging.info("--------------- Entering Tracking ID or Container No. ---------------")
        Tracking_ID_input = driver.find_element(By.XPATH, '//label[@for="txtcontainerNumber"]//parent::div//input[@placeholder="Enter container #"]')
        Tracking_ID_input.click()
        Tracking_ID_input.send_keys(Tracking_ID)
        time.sleep(1)

        # To Click on Search Button
        logging.info("--------------- Clicking on Search Button ---------------")
        Search_button = driver.find_element(By.XPATH, '//button[text()="Search" and @id="btnsearchctrinq"]')
        Search_button.click()
        time.sleep(1)

        # To Get Container Details
        logging.info("--------------- Getting Container Details ---------------")
        try:
            Shipping_Line = driver.find_element(By.XPATH, '(//b[text()="Shipping Line"]//parent::td//parent::tr//td)[2]').text
        except:
            Shipping_Line = ''

        print(f"Shipping Line: {Shipping_Line}")

        try:
            Size_Type = driver.find_element(By.XPATH, '(//b[text()="Size/Type"]//parent::td//parent::tr//td)[2]').text
        except:
            Size_Type = ''

        print(f"Size/Type: {Size_Type}")
        
        try:
            Category = driver.find_element(By.XPATH, '(//b[text()="Category"]//parent::td//parent::tr//td)[2]').text
        except:
            Category = ''

        print(f"Category: {Category}")
        
        try:
            Status = driver.find_element(By.XPATH, '(//b[text()="Status"]//parent::td//parent::tr//td)[2]').text
        except:
            Status = ''

        print(f"Status: {Status}")
        
        try:
            Discharge_Port = driver.find_element(By.XPATH, '(//b[text()="Port Of Discharge"]//parent::td//parent::tr//td)[2]').text
        except:
            Discharge_Port = ''

        print(f"Port Of Discharg: {Discharge_Port}")
        
        try:
            Destination = driver.find_element(By.XPATH, '(//b[text()="Destination"]//parent::td//parent::tr//td)[2]').text
        except:
            Destination = ''

        print(f"Destination: {Destination}")
        
        try:
            Position = driver.find_element(By.XPATH, '(//b[text()="Position"]//parent::td//parent::tr//td)[2]').text
        except:
            Position = ''

        print(f"Position: {Position}")
        
        try:
            In_Time = driver.find_element(By.XPATH, '(//b[text()="In Time"]//parent::td//parent::tr//td)[2]').text
        except:
            In_Time = ''

        print(f"In Time: {In_Time}")
        
        try:
            Load_Time = driver.find_element(By.XPATH, '(//b[text()="Load Time"]//parent::td//parent::tr//td)[2]').text
        except:
            try: Load_Time = driver.find_element(By.XPATH, '(//b[text()="Out Time"]//parent::td//parent::tr//td)[2]').text
            except: Load_Time = ''

        print(f"Load Time: {Load_Time}")
        
        try:
            VIR_No = driver.find_element(By.XPATH, '(//b[text()="VIR #"]//parent::td//parent::tr//td)[2]').text
        except:
            VIR_No = ''

        print(f"VIR #: {VIR_No}")
        
        try:
            Vessel = driver.find_element(By.XPATH, '(//b[text()="Vessel"]//parent::td//parent::tr//td)[2]').text
        except:
            Vessel = ''

        print(f"Vessel: {Vessel}")
        
        try:
            Voyage = driver.find_element(By.XPATH, '(//b[text()="Voyage"]//parent::td//parent::tr//td)[2]').text
        except:
            Voyage = ''

        print(f"Voyage: {Voyage}")
        
        try:
            Booking_No = driver.find_element(By.XPATH, '(//b[text()="Booking #"]//parent::td//parent::tr//td)[2]').text
        except:
            Booking_No = ''

        print(f"Booking #: {Booking_No}")
        
        try:
            Shipper_Seal = driver.find_element(By.XPATH, '(//b[text()="Shipper Seal"]//parent::td//parent::tr//td)[2]').text
        except:
            Shipper_Seal = ''

        print(f"Shipper Seal: {Shipper_Seal}")
        
        try:
            Line_Seal = driver.find_element(By.XPATH, '(//b[text()="Line Seal"]//parent::td//parent::tr//td)[2]').text
        except:
            Line_Seal = ''

        print(f"Line Seal: {Line_Seal}")
        
        try:
            Standing = driver.find_element(By.XPATH, '(//b[text()="Standing"]//parent::td//parent::tr//td)[2]').text
        except:
            Standing = ''

        print(f"Standing: {Standing}")
        
        try:
            Hold_Description = driver.find_element(By.XPATH, '(//b[text()="Hold Description"]//parent::td//parent::tr//td)[2]').text
        except:
            Hold_Description = ''

        print(f"Hold Description: {Hold_Description}")
        
        try:
            PreGate_Arrival_Time = driver.find_element(By.XPATH, '(//b[text()="Pre-Gate Arrival Time"]//parent::td//parent::tr//td)[2]').text
        except:
            PreGate_Arrival_Time = ''

        print(f"Pre-Gate Arrival Time: {PreGate_Arrival_Time}")
        
        try:
            Truck_In_Time = driver.find_element(By.XPATH, '(//b[text()="Truck In Time"]//parent::td//parent::tr//td)[2]').text
        except:
            Truck_In_Time = ''

        print(f"Truck In Time: {Truck_In_Time}")
        
        try:
            Truck_In_Yard = driver.find_element(By.XPATH, '(//b[text()="Truck In Yard"]//parent::td//parent::tr//td)[2]').text
        except:
            Truck_In_Yard = ''

        print(f"Truck In Yard: {Truck_In_Yard}")
        time.sleep(1)
        
        # To Click on Close Button
        logging.info("--------------- Clicking on Close Button ---------------")
        Search_button = driver.find_element(By.XPATH, '(//div[@class="modal-header"]//button[@aria-label="Close"])[3]')
        Search_button.click()
        time.sleep(2)

        data = {'Tracking_ID':Tracking_ID,'Shipping_Line':Shipping_Line,'Size/Type':Size_Type,'Category':Category,
                'Status':Status,'Port_of_Discharge':Discharge_Port,'Destination':Destination,'Position':Position,
                'In_Time':In_Time,'Load_Time':Load_Time,'VIR_No':VIR_No,'Vessel':Vessel,'Voyage':Voyage,
                'Booking_No':Booking_No,"Shipper_Seal":Shipper_Seal,"Line_Seal":Line_Seal,'Standing':Standing,
                'Hold_Description':Hold_Description,'Pre-Gate_Arrival_Time':PreGate_Arrival_Time,
                "Truck_In_Time":Truck_In_Time,"Truck_In_Yard":Truck_In_Yard}
        
        print(data)
        logging.info(f"Tracking ID ------------> {Tracking_ID} data is scraped!!!!")
        return data
