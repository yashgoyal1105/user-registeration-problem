import re 
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("user_registration.log"),  # Logs to file
        logging.StreamHandler()  # Logs to console
    ]
)
logger = logging.getLogger(__name__)

#fisrt name
def get_first_name():
    first_name = input("Enter first name (First name starts with Cap and has minimum 3 characters): ")
    name_pattern = "^[A-Z][a-z]{2,}$"

    while (not re.fullmatch(name_pattern,first_name)):
        logger.warning("Invalid First name was entered by the user.")
        first_name = input("Invalid first name. Enter Fisrt name again: ")
    
    logger.info(f"valid first name: {first_name}")
    print("valid First name!") 
    return first_name

#last name
def get_last_name():
    last_name = input("Enter Last name (Last name starts with Cap and has minimum 3 characters): ")
    name_pattern = "^[A-Z][a-z]{2,}$"
    
    while (not re.fullmatch(name_pattern,last_name)):
        logger.warning("Invalid last name entered.")
        last_name = input("Invalid last name. Enter Fisrt name again: ")
    
    logger.info(f"valid last name: {last_name}")
    print("valid Last name!")
    return last_name

#e_mail id
def get_email_id():
    e_mail = input("Enter Email id: ")
    mail_pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2})?$'
    
    while (not re.fullmatch(mail_pattern,e_mail)):
        logger.warning("Invalid Email entered")
        e_mail = input(f"{e_mail} is an Invalid Email! Kindly Enter it again: ")
        
    logger.info(f"valid e-mail entered: {e_mail}")
    print(f"{e_mail} is a Valid Email id!")
    return e_mail

#phone number
def get_contact_number(): 
    phone_number = input("Enter phone number followed by country code(seprated by whitespace): ")
    pattern = "^\d{1,4} \d{10}$"
    
    while not re.fullmatch(pattern,phone_number):
        phone_number = logger.warning("Invalid phnoe number entered.")
        print(f"{phone_number} is an invalid number. Enter number again! : ")

    logger.info("valid phone number entered.")
    print(f"{phone_number} is a valid number! ")
    return phone_number
  
#password  
def set_password():
    password = input("Set a password (min 8 chars, 1 uppercase, 1 number, exactly 1 special character): ")
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$'  

    while not re.fullmatch(pattern,password):
        logger.warning("Invalid format entered")
        password = input("Invalid password format! set password again! : ")
    
    logger.info("valid password entered.")
    print("valid passwrod! ")
    return password


def main():
    try:
        first_name = get_first_name()
        last_name = get_last_name()
        e_mail = get_email_id()
        phone_number = get_contact_number()
        password = set_password()
        logger.info(f"{first_name} {last_name} registered successfully!!")
        print("registration successful!")
    
    except Exception as e:
        logger.error(f"Unexpected error {e}")
    
if __name__ == '__main__':
    main() 