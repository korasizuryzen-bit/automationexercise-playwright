# AutomationExercise UI Test Automation (Playwright + Pytest + POM + Allure)

## What this project does
End-to-end automated UI test for https://www.automationexercise.com

Scenario covered:
1) User Registration
2) Add 2 products to cart
3) Verify cart contains products
4) Proceed to checkout and pay
5) Verify successful order confirmation

## Tech stack
- Python
- Pytest
- Playwright
- Page Object Model (POM)
- Allure Report

## Project structure
- `pages/` - Page Objects (POM)
- `tests/` - Tests and fixtures
- `utils/` - helper functions (test data)

## Setup (Windows)
Open PowerShell in VS Code in the project folder and run:

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
playwright install
