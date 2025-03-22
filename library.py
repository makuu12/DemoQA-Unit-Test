from selenium.webdriver.common.by import By

class FormValidator:
    ERROR_COLOR = "rgb(220, 53, 69)"  # Equivalent to #dc3545

    @staticmethod
    def validate_fields(driver, field_xpaths):
        """
        Checks if all specified fields have a red border (error validation).
        
        :param driver: Selenium WebDriver instance
        :param field_xpaths: List of XPaths for the input fields
        :return: True if all fields show an error, False otherwise
        
        usage:
        fields = [list of text]
        result = FormValidator.validate_fields(driver, fields)
        
        print(f"Test #: {'PASSED' if result else 'FAILED'}")
        """
        all_valid = True  # Assume all fields have an error

        for field_xpath in field_xpaths:
            field = driver.find_element(By.XPATH, field_xpath)
            border_color = field.value_of_css_property("border-color").strip()

            if border_color != FormValidator.ERROR_COLOR:
                all_valid = False  # If any field is not red, set to False

        return all_valid
    
