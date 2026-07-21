from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys


# Page Object for the Urban Routes app: keeps every locator and page action
# in one place, so the tests only call readable methods (set_route, add_card…).
class UrbanRoutesPage:
    # ----- Locators -----
    # Route (origin / destination fields)
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    # Request taxi button and Comfort tariff
    request_taxi_button = (By.CSS_SELECTOR, '.button.round')
    comfort_icon = (By.XPATH, '//div[@class="tcard-title" and text()="Comfort"]')
    comfort_container_assert = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]')
    # Phone number and SMS confirmation
    phone_number_button = (By.XPATH, '//div[@class="np-text" and text()="Número de teléfono"]')
    phone_number_field = (By.ID, 'phone')
    code_phone_number_field = (By.ID, 'code')
    next_phone_number_button = (By.XPATH, '//button[@class="button full" and text()="Siguiente"]')
    confirm_phone_button = (By.XPATH, '//button[@class="button full" and text()="Confirmar"]')
    phone = (By.CSS_SELECTOR, '.np-text')
    # Payment method / add card
    payment_method_button = (By.XPATH, '//div[@class="pp-text" and text()="Método de pago"]')
    add_card_button = (By.XPATH, '//div[@class="pp-title" and text()="Agregar tarjeta"]')
    add_card_number_field = (By.ID, 'number')
    add_card_code_field = (By.CSS_SELECTOR, '.card-code-input #code')
    confirm_add_card_button = (By.XPATH, '//button[@class="button full" and text()="Agregar"]')
    payment_method_close_button = (By.CSS_SELECTOR, ".payment-picker.open .section.active .close-button.section-close")
    card_added_checkbox = (By.ID, 'card-1')
    # Message for the driver
    message_field = (By.ID, 'comment')
    message_to_long_error = (By.XPATH, '//div[@class="error"]')
    # Comfort extras: blanket & tissues switch (the visible slider is clicked, the hidden input holds the state)
    blanket_tissues_checkbox = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]/following-sibling::div[@class="r-sw"]//span[@class="slider round"]')
    blanket_tissues_input = (By.XPATH, '//div[@class="r-sw-label" and text()="Manta y pañuelos"]/following-sibling::div[@class="r-sw"]//input[@class="switch-input"]')
    # Ice cream counter ("+" uses contains() so it still matches when the "disabled" class is added)
    ice_cream_plus = (By.XPATH, '//div[@class="r-counter-label" and text()="Helado"]/following-sibling::div[@class="r-counter"]//div[contains(@class,"counter-plus")]')
    ice_cream_value = (By.XPATH, '//div[@class="r-counter-label" and text()="Helado"]/following-sibling::div[@class="r-counter"]//div[@class="counter-value"]')
    # Order the taxi / car-search pop-up / driver-arrival modal
    find_taxi_button = (By.XPATH, '//div[@class="smart-button-wrapper"]//span[@class="smart-button-main" and text()="Pedir un taxi"]')
    title_order_pop_up = (By.CLASS_NAME, 'order-header-title')
    driver_arrival_modal = (By.XPATH, '//div[@class="order-header-title" and contains(text(), "El conductor llegará en")]')


    def __init__(self, driver):
        self.driver = driver
        # Default explicit wait (in seconds) reused by most methods
        self.wait = WebDriverWait(driver, 5)

    # ----- Route (origin / destination) -----
    def get_from_field(self):
        return self.wait.until(
            ec.visibility_of_element_located(self.from_field)
        )

    def set_from_field(self,address_from):
        self.get_from_field().send_keys(address_from)

    def get_to_field(self):
        return self.wait.until(
            ec.visibility_of_element_located(self.to_field)
        )

    def set_to_field(self,address_to):
        self.get_to_field().send_keys(address_to)

    # Read the current value typed into the origin / destination fields
    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    # Fill both route fields in one call
    def set_route(self, address_from, address_to):
        self.set_from_field(address_from)
        self.set_to_field(address_to)

    # ----- Request taxi and Comfort tariff -----
    def get_request_taxi_button(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.request_taxi_button)
        )

    def click_request_taxi_button(self):
        self.get_request_taxi_button().click()

    def get_comfort_icon(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.comfort_icon)
        )

    def click_comfort_icon(self):
        self.get_comfort_icon().click()

    # Text used to confirm the Comfort tariff is selected
    def get_comfort_container_assert(self):
        return self.wait.until(
            ec.presence_of_element_located(self.comfort_container_assert)
        ).text

    # ----- Phone number -----
    def get_phone_number_button(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.phone_number_button)
        )

    def click_phone_number_button(self):
        self.get_phone_number_button().click()

    def get_phone_number_field(self):
        return self.wait.until(
            ec.visibility_of_element_located(self.phone_number_field)
        )

    def set_phone_number_field(self,phone_number):
        self.get_phone_number_field().send_keys(phone_number)

    def get_code_phone_number_field(self):
        return self.wait.until(
            ec.visibility_of_element_located(self.code_phone_number_field)
        )

    def set_code_phone_number_field(self,code_phone_number):
        self.get_code_phone_number_field().send_keys(code_phone_number)

    def get_next_phone_number_button(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.next_phone_number_button)
        )

    def click_next_phone_number_button(self):
        self.get_next_phone_number_button().click()

    def get_confirm_phone_button(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.confirm_phone_button)
        )

    def click_confirm_phone_button(self):
        self.get_confirm_phone_button().click()

    # Read the confirmed phone number shown on the page
    def get_phone(self):
        return self.wait.until(
            ec.visibility_of_element_located(self.phone)
        ).text

    # ----- Payment method / add card -----
    def get_payment_method_button(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.payment_method_button)
        )

    def click_payment_method_button(self):
        self.get_payment_method_button().click()

    def get_add_card_button(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.add_card_button)
        )

    def click_add_card_button(self):
        self.get_add_card_button().click()

    def get_add_card_number_field(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.add_card_number_field)
        )

    def set_add_card_number(self,card_number):
        self.get_add_card_number_field().send_keys(card_number)

    def get_add_card_code_field(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.add_card_code_field)
        )

    # TAB after the code triggers the field's blur event so the "Agregar" button enables
    def set_add_card_code(self,card_code):
        self.get_add_card_code_field().send_keys(card_code, Keys.TAB)

    def get_confirm_add_card_button(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.confirm_add_card_button)
        )

    def click_confirm_add_card_button(self):
        self.get_confirm_add_card_button().click()

    def get_payment_method_close_button(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.payment_method_close_button)
        )

    def click_payment_method_close_button(self):
        self.get_payment_method_close_button().click()

    # The added card checkbox is hidden, so presence (not visibility) is used to read it
    def get_card_added_checkbox(self):
        return self.wait.until(
            ec.presence_of_element_located(self.card_added_checkbox)
        )

    # ----- Message for the driver -----
    def get_message_field(self):
        return self.wait.until(
            ec.visibility_of_element_located(self.message_field)
        )

    def set_message_field(self,message):
        self.get_message_field().send_keys(message)

    # Read the current text stored in the message field
    def get_message(self):
        return self.get_message_field().get_attribute('value')

    # Read the validation error shown when the message is too long
    def get_message_to_long_error(self):
        return self.wait.until(
            ec.visibility_of_element_located(self.message_to_long_error)
        ).text

    # ----- Comfort extras: blanket & tissues -----
    def get_blanket_tissues_checkbox(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.blanket_tissues_checkbox)
        )

    # Click the visible slider to turn the switch on
    def click_blanket_tissues_checkbox(self):
        self.get_blanket_tissues_checkbox().click()

    # The real checkbox is hidden, so presence is used; assert its state with .is_selected()
    def get_blanket_tissues_input(self):
        return self.wait.until(
            ec.presence_of_element_located(self.blanket_tissues_input)
        )

    # ----- Comfort extras: ice cream counter -----
    def get_ice_cream_plus(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.ice_cream_plus)
        )

    # Click "+" the given number of times (defaults to once)
    def click_ice_cream_plus(self,times=1):
        for _ in range(times):
            self.get_ice_cream_plus().click()

    # Read the current counter value (returned as text)
    def get_ice_cream_value(self):
        return self.wait.until(
            ec.visibility_of_element_located(self.ice_cream_value)
        ).text

    # Read the "+" button class; contains "disabled" once the max is reached
    def get_ice_cream_plus_class(self):
        return self.get_ice_cream_plus().get_attribute('class')

    # ----- Order the taxi / car-search / arrival modal -----
    def get_find_taxi_button(self):
        return self.wait.until(
            ec.element_to_be_clickable(self.find_taxi_button)
        )

    # The button label ("Pedir un taxi") is only present once phone is set
    def get_find_taxi_value(self):
        return self.get_find_taxi_button().text

    def click_find_taxi_button(self):
        self.get_find_taxi_button().click()

    def get_title_order_pop_up(self):
        return self.wait.until(
            ec.visibility_of_element_located(self.title_order_pop_up)
        )

    # Title of the car-search pop-up ("Buscar automóvil")
    def get_title_order_value(self):
        return self.get_title_order_pop_up().text

    # The driver search takes more than 30s, so this uses a longer 60s wait than the default
    def get_driver_arrival_modal(self):
        return WebDriverWait(self.driver, 60).until(
            ec.visibility_of_element_located(self.driver_arrival_modal)
        ).text