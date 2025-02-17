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

def validate_first_name(first_name):
    """Validates the first name to ensure it starts with a capital letter and has at least 3 characters."""
    name_pattern = "^[A-Z][a-z]{2,}$"
    if re.fullmatch(name_pattern, first_name):
        logger.info(f"Valid first name: {first_name}")
        return True
    logger.warning("Invalid first name entered.")
    return False

def validate_last_name(last_name):
    """Validates the last name to ensure it starts with a capital letter and has at least 3 characters."""
    name_pattern = "^[A-Z][a-z]{2,}$"
    if re.fullmatch(name_pattern, last_name):
        logger.info(f"Valid last name: {last_name}")
        return True
    logger.warning("Invalid last name entered.")
    return False

def validate_email(e_mail):
    """Validates an email address based on a general email format pattern."""
    mail_pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2})?$'
    if re.fullmatch(mail_pattern, e_mail):
        logger.info(f"Valid email entered: {e_mail}")
        return True
    logger.warning("Invalid email entered.")
    return False

def validate_contact_number(phone_number):
    """Validates a phone number ensuring it follows the format: country code followed by a 10-digit number."""
    pattern = r"^\d{1,3} \d{10}$"
    if re.fullmatch(pattern, phone_number):
        logger.info("Valid phone number entered.")
        return True
    logger.warning("Invalid phone number entered.")
    return False

def validate_password(password):
    """Validates the password ensuring it has at least 8 characters, an uppercase letter, a number, and a special character."""
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$'
    if re.fullmatch(pattern, password):
        logger.info("Valid password entered.")
        return True
    logger.warning("Invalid password format entered.")
    return False

def get_validated_input(prompt, validation_func):
    """Prompts the user for input and validates it using the provided validation function."""
    user_input = input(prompt)
    while not validation_func(user_input):
        print("Invalid input. Please try again.")
        user_input = input(prompt)
    return user_input

def main():
    """Main function to handle user registration with input validation."""
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
