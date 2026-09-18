# Urban Routes Project

## Description
This project contains automated UI (end-to-end) tests that validate the full "order a taxi" flow in the Urban Routes web application, using Python, Selenium and Pytest. The tests follow the Page Object Model (POM) design pattern to keep locators and page actions separated from the test logic.

The suite covers the complete happy path and some validations:
1. Set the route (from / to addresses)
2. Select the Comfort tariff
3. Enter a phone number (retrieving the SMS confirmation code)
4. Add a credit card
5. Validate the driver-message field (maximum length)
6. Request a blanket and tissues
7. Order 2 ice creams
8. Verify the "add ice cream" button is disabled at the maximum
9. Confirm the "Pedir un taxi" button is ready
10. Verify the car-search pop-up appears
11. Verify the driver-arrival modal ("El conductor llegará en…")

## Application Under Test
The URL of the web app is configured in `data/data.py` (`urban_routes_url`).
> Note: TripleTen container URLs are temporary. If the tests can't reach the site, update `urban_routes_url` in `data/data.py` with the current address.

## Technologies Used
- Python 3.14.6
- Selenium 4.46.0
- Pytest 9.1.1
- Google Chrome + ChromeDriver

## Project Structure
- `data/data.py` — application URL and test data (addresses, phone, card, message).
- `pages/urban_routes_page.py` — Page Object: all locators and page actions.
- `helpers/retrieve_code.py` — retrieves the phone confirmation code from the browser network logs.
- `tests/test_urban_routes.py` — the automated test cases.

## How to Run the Tests
1. Open the project in PyCharm.
2. Make sure Google Chrome and a matching ChromeDriver are installed.
3. Install the required packages:
   ```bash
   pip install selenium pytest
   ```
4. Run all tests using the `pytest` command:
   ```bash
   pytest
   ```
