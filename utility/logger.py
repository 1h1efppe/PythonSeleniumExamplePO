import logging


class Logger:
    @staticmethod
    def info(message):
        logging.info(message)

    @staticmethod
    def error(message):
        logging.error(message)

    @staticmethod
    def locator_found_message(locator):
        return 'Element {} found'.format(locator)

    @staticmethod
    def locator_check_message(locator):
        return 'Checking for {} element'.format(locator)

    @staticmethod
    def locator_not_found(locator):
        return 'Element {} not found or interactable'.format(locator)

    @staticmethod
    def clicking_locator(locator):
        return 'Clicking {} element'.format(locator)

    @staticmethod
    def waiting_for_click(locator):
        'Waiting for {} element to click it'.format(locator)

    @staticmethod
    def sending_text_to_element(text, locator):
        'Sending {} to {} element'.format(text, locator)

    @staticmethod
    def getting_text_from_element(locator):
        'Getting text from {} element'.format(locator)

    @staticmethod
    def text_of_locator(locator, element):
        'Text of {} is {}'.format(locator, element.text)
