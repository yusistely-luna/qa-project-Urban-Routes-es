# 🚕 Urban Routes — UI Test Automation

**Web · Selenium · Pytest · POM** — TripleTen Bootcamp Project (2026)
> 🎓 Sprint Project

---

## 🎯 Problem

End-to-end UI automation of the complete "order a taxi" flow in the Urban Routes web application. The goal was to script the full happy path — from setting the route to receiving driver details — as a reliable, maintainable test suite built on the Page Object Model (POM), so the flow could be re-run and verified without manual clicking.

---

## 📊 Results & Impact

| Metric              | Value                          |
| -------------------- | -------------------------------- |
| Flow steps automated | **11**                           |
| Design pattern        | **Page Object Model (POM)**      |
| Framework             | **Selenium + Pytest**            |
| Language              | **Python**                       |

---

## ⚙️ What I Did

### Test Automation (Python + Selenium + Pytest)

- Structured the project around the **Page Object Model**, separating locators and page actions (`pages/urban_routes_page.py`) from test logic (`tests/test_urban_routes.py`) — so a UI change only requires updating one place
- Built a helper (`helpers/retrieve_code.py`) that reads the browser's network logs to retrieve the SMS confirmation code automatically, instead of hardcoding or skipping that step
- Centralized all test data — addresses, phone number, card details, driver message — in `data/data.py`, keeping the test file focused on behavior rather than literals
- Automated the full happy path plus key UI validations end to end, covering the entire taxi-ordering journey in a single, repeatable suite

### Flow Covered

1. Set the route (from / to addresses)
2. Select the Comfort tariff
3. Enter a phone number and retrieve the SMS confirmation code
4. Add a credit card
5. Validate the driver-message field (maximum length)
6. Request a blanket and tissues
7. Order 2 ice creams
8. Verify the "add ice cream" button is disabled at the maximum
9. Confirm the "Pedir un taxi" button is ready
10. Verify the car-search pop-up appears
11. Verify the driver-arrival modal ("El conductor llegará en…")

---

## ✅ Learning

Automating a real multi-step flow surfaces problems that a single-page test never does — session state has to survive across steps, and a value entered in step 3 (like the SMS code) has to be fetched dynamically rather than assumed. Separating locators from test logic through POM made the suite far easier to maintain: when a selector changed, the fix lived in exactly one file instead of being scattered across every test. Retrieving the confirmation code from the browser's own network logs, instead of skipping or mocking that step, kept the test honest to the real user flow.

---

## 🛠️ Skills

Python · Selenium WebDriver · Pytest · Page Object Model (POM) · UI Test Automation · End-to-End Testing · Test Data Management · Browser Network Log Inspection

---

## 🧰 Technologies Used

- Python 3.14.6
- Selenium 4.46.0
- Pytest 9.1.1
- Google Chrome + ChromeDriver

---

## 📁 Project Structure

- `data/data.py` — application URL and test data (addresses, phone, card, message)
- `pages/urban_routes_page.py` — Page Object: all locators and page actions
- `helpers/retrieve_code.py` — retrieves the phone confirmation code from the browser network logs
- `tests/test_urban_routes.py` — the automated test cases

---

## ▶️ How to Run the Tests

1. Open the project in PyCharm
2. Make sure Google Chrome and a matching ChromeDriver are installed
3. Install the required packages:

\`\`\`
pip install selenium pytest
\`\`\`

4. Run all tests with:

\`\`\`
pytest
\`\`\`

> **Note:** TripleTen container URLs are temporary. If the tests can't reach the site, update `urban_routes_url` in `data/data.py` with the current address.
