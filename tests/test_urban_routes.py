from ssl import Options
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from pages.urban_routes_page import UrbanRoutesPage
from data import data
from helpers import retrieve_code


class TestUrbanRoutes:

    driver = None

    # Runs once before all tests: opens Chrome, enables performance logs
    # (needed to read the SMS code), maximizes the window and loads the app.
    @classmethod
    def setup_class(cls):
        options = Options()
        options.set_capability('goog:loggingPrefs', {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(),options=options)
        cls.driver.maximize_window()
        cls.driver.get(data.urban_routes_url)
        cls.routes_page = UrbanRoutesPage(cls.driver)

    # Test 1: Set the route (from / to addresses).
    # Expected result: both fields show the addresses that were entered.
    def test_set_route(self):
        address_from = data.address_from
        address_to = data.address_to
        self.routes_page.set_route(address_from, address_to)
        assert self.routes_page.get_from() == address_from
        assert self.routes_page.get_to() == address_to

    # Test 2: Request a taxi and select the Comfort tariff.
    # Expected result: the Comfort options ("Manta y pañuelos") are shown.
    def test_comfort_tariff_selection(self):
        self.routes_page.click_request_taxi_button()
        self.routes_page.click_comfort_icon()
        assert self.routes_page.get_comfort_container_assert() == "Manta y pañuelos"

    # Test 3: Enter the phone number and confirm it with the SMS code.
    # Expected result: the confirmed phone number matches the one entered.
    def test_enter_phone_number(self):
        phone_number = data.phone_number
        self.routes_page.click_phone_number_button()
        self.routes_page.set_phone_number_field(phone_number)
        self.routes_page.click_next_phone_number_button()
        code_phone_number = retrieve_code.retrieve_phone_code(self.driver)
        self.routes_page.set_code_phone_number_field(code_phone_number)
        self.routes_page.click_confirm_phone_button()
        assert self.routes_page.get_phone() == data.phone_number

    # Test 4: Add a credit card as the payment method.
    # Expected result: the added card checkbox is selected.
    def test_add_card(self):
        card_number = data.card_number
        card_code = data.card_code
        self.routes_page.click_payment_method_button()
        self.routes_page.click_add_card_button()
        self.routes_page.set_add_card_number(card_number)
        self.routes_page.set_add_card_code(card_code)
        self.routes_page.click_confirm_add_card_button()
        self.routes_page.click_payment_method_close_button()
        assert self.routes_page.get_card_added_checkbox().is_selected()

    # Test 5: Write a message for the driver that exceeds the 24-character limit.
    # Expected result: the "Longitud máxima 24" error message is shown.
    def test_message_to_long_error(self):
        message = data.message_for_driver
        self.routes_page.set_message_field(message)
        assert self.routes_page.get_message_to_long_error() == 'Longitud máxima 24'

    # Test 6: Request a blanket and tissues (Comfort extra).
    # Expected result: the blanket/tissues switch is turned on.
    def test_blanket_and_tissues_request(self):
        self.routes_page.click_blanket_tissues_checkbox()
        assert self.routes_page.get_blanket_tissues_input().is_selected()

    # Test 7: Order 2 ice creams using the "+" button.
    # Expected result: the counter shows "2".
    def test_order_two_ice_creams(self):
        self.routes_page.click_ice_cream_plus(2)
        assert self.routes_page.get_ice_cream_value() == '2'

    # Test 8: The ice cream "+" button reaches its maximum at 2.
    # Expected result: the "+" button becomes disabled.
    def test_ice_cream_plus_disabled_at_max(self):
        self.routes_page.click_ice_cream_plus(2)
        assert 'disabled' in self.routes_page.get_ice_cream_plus_class()

    # Test 9: The order button is ready to request the taxi.
    # Expected result: the button text is "Pedir un taxi".
    def test_ready_to_get_a_taxi(self):
        assert self.routes_page.get_find_taxi_value() == 'Pedir un taxi'

    # Test 10: Click "Pedir un taxi" to open the car-search pop-up.
    # Expected result: the pop-up title is "Buscar automóvil".
    def test_find_a_taxi_pop_up(self):
        self.routes_page.click_find_taxi_button()
        assert self.routes_page.get_title_order_value() == 'Buscar automóvil'

    # Test 11: Wait for the driver-arrival modal.
    # Expected result: the modal text contains "El conductor llegará en".
    def test_arrival_modal(self):
        assert "El conductor llegará en" in self.routes_page.get_driver_arrival_modal()

    # Runs once after all tests: closes the browser.
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()