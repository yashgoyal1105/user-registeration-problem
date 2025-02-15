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
    """Validates that the first name starts with an uppercase letter and has at least 3 characters."""
    return bool(re.fullmatch("^[A-Z][a-z]{2,}$", first_name))

def validate_last_name(last_name):
    """Validates that the last name starts with an uppercase letter and has at least 3 characters."""
    return bool(re.fullmatch("^[A-Z][a-z]{2,}$", last_name))

def validate_email(email):
    """Validates email format (e.g., example@domain.com)."""
    pattern = r'^[a-zA-Z0-9]+(\.[a-zA-Z0-9]+)?@[a-zA-Z0-9]+\.[a-zA-Z]{2,3}(\.[a-zA-Z]{2})?$'
    return bool(re.fullmatch(pattern, email))

def validate_contact_number(phone_number):
    """Validates phone number format (e.g., 91 9876543210)."""
    return bool(re.fullmatch(r"^\d{1,3} \d{10}$", phone_number))

def validate_password(password):
    """Validates password with at least 8 chars, 1 uppercase, 1 digit, and 1 special char."""
    pattern = r'^(?=.*[A-Z])(?=.*\d)(?=.*[^a-zA-Z0-9]).{8,}$'
    return bool(re.fullmatch(pattern, password))

def get_validated_input(prompt, validation_func):
    """Prompts the user for input and validates it using the provided function."""
    while True:
        user_input = input(prompt)
        if validation_func(user_input):
            return user_input
        print("Invalid input. Please try again.")

def main():
    """Handles user registration by collecting and validating user details."""
    try:
        user_data = {
            "First Name": get_validated_input("Enter First Name: ", validate_first_name),
            "Last Name": get_validated_input("Enter Last Name: ", validate_last_name),
            "Email": get_validated_input("Enter Email: ", validate_email),
            "Phone Number": get_validated_input("Enter Phone Number: ", validate_contact_number),
            "Password": get_validated_input("Set Password: ", validate_password)
        }
        logger.info(f"User {user_data['First Name']} {user_data['Last Name']} registered successfully!")
        print("\nRegistration Successful!")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
