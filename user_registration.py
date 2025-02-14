import re
import logging

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("user_registration.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Function to validate first name
def validate_first_name(first_name):
    name_pattern = "^[A-Z][a-z]{2,}$"
    if re.fullmatch(name_pattern, first_name):
        logger.info(f"Valid first name: {first_name}")
        return True
    logger.warning("Invalid first name entered.")
    return False

# Function to validate last name
def validate_last_name(last_name):
    name_pattern = "^[A-Z][a-z]{2,}$"
    if re.fullmatch(name_pattern, last_name):
        logger.info(f"Valid last name: {last_name}")
        return True
    logger.warning("Invalid last name entered.")
    return False

# Function to validate email
def validate_email(e_mail):
    mail_pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2})?$'
    if re.fullmatch(mail_pattern, e_mail):
        logger.info(f"Valid email entered: {e_mail}")
        return True
    logger.warning("Invalid email entered.")
    return False

# Function to validate phone number
def validate_contact_number(phone_number):
    pattern = r"^\d{1,3} \d{10}$"
    if re.fullmatch(pattern, phone_number):
        logger.info("Valid phone number entered.")
        return True
    logger.warning("Invalid phone number entered.")
    return False

# Function to validate password
def validate_password(password):
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$'
    if re.fullmatch(pattern, password):
        logger.info("Valid password entered.")
        return True
    logger.warning("Invalid password format entered.")
    return False

# Function to get validated user input
def get_validated_input(prompt, validation_func):
    user_input = input(prompt)
    while not validation_func(user_input):
        print("Invalid input. Please try again.")
        user_input = input(prompt)
    return user_input

# Main function to handle user registration
def main():
    try:
        first_name = get_validated_input(
            "Enter First name (Starts with a capital letter, min 3 chars): ", 
            validate_first_name
        )
        
        last_name = get_validated_input(
            "Enter Last name (Starts with a capital letter, min 3 chars): ", 
            validate_last_name
        )
        
        email = get_validated_input(
            "Enter Email ID: ", 
            validate_email
        )
        
        phone_number = get_validated_input(
            "Enter phone number (Country code followed by number, e.g., 91 9876543210): ", 
            validate_contact_number
        )
        
        password = get_validated_input(
            "Set a password (Min 8 chars, 1 uppercase, 1 number, 1 special char): ", 
            validate_password
        )

        logger.info(f"User {first_name} {last_name} registered successfully!")
        print("\nRegistration Successful!")

    except Exception as e:
        logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
