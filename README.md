# The Soul Store - Automation Testing Suite

A comprehensive Selenium-based automation testing suite for **The Soul Store** website, designed to validate critical user workflows including login functionality and navbar navigation.

## 📋 Project Overview

This project contains automated test scripts that validate:
- **Login Functionality**: Tests user login with OTP verification
- **Navbar Navigation**: Tests hamburger menu and navigation components

Website: [https://www.thesouledstore.com/](https://www.thesouledstore.com/)

## 📁 Project Structure

```
THE_SOUL_STORE/
├── THE_SOUL_STORE_LOGIN (1).PY      # Login functionality tests
├── the_soul_store_navbar (1).py     # Navbar & hamburger menu tests
├── test_reports/                    # Generated test reports
│   ├── login_test_report_*.html
│   └── navbar_test_report_*.html
└── README.md                        # This file
```

## 🚀 Features

### Login Testing Module
- **Phone Number Input**: Tests number input field with class selectors
- **OTP Verification**: Validates one-time password entry with manual time input
- **Success/Failure Validation**: Checks login success or failure scenarios
- **Detailed Logging**: Captures step-by-step test execution logs

### Navbar Testing Module
- **Hamburger Menu Detection**: Verifies hamburger menu presence and visibility
- **Menu Interaction**: Tests hamburger menu click functionality
- **Navigation Operations**: Validates menu interactions and navigation flows
- **Cross-browser Testing**: Supports Chrome driver automation

## 🔧 Requirements

- **Python 3.7+**
- **Selenium**: WebDriver automation library
  ```bash
  pip install selenium
  ```
- **ChromeDriver**: WebDriver for Chrome browser
  - Download from: [ChromeDriver](https://chromedriver.chromium.org/)
  - Ensure it's in your system PATH or specify the path in the script

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/LokeshMangrulkar/THE-SOUL-STORE.git
   cd THE-SOUL-STORE
   ```

2. Install dependencies:
   ```bash
   pip install selenium
   ```

3. Download ChromeDriver matching your Chrome version and add to PATH

## 🧪 Running Tests

### Login Tests
```bash
python "THE_SOUL_STORE_LOGIN (1).PY"
```

### Navbar Tests
```bash
python "the_soul_store_navbar (1).py"
```

## 📊 Test Reports

Test reports are automatically generated and saved in the `test_reports/` directory:
- Login reports: `login_test_report_[timestamp].html`
- Navbar reports: `navbar_test_report_[timestamp].html`

Open HTML reports in any web browser to view:
- Test execution timeline
- Pass/Fail status for each step
- Detailed error messages (if any)
- Screenshots and logs

## 🏗️ Test Structure

Both test classes follow a similar structure:

1. **Initialization**: Setup WebDriver and wait conditions
2. **Step-by-step Testing**: Each test method performs specific validations
3. **Result Recording**: Captures pass/fail status with timestamps
4. **Report Generation**: Creates HTML reports with comprehensive details

### Example Test Flow
```
1. Initialize WebDriver
2. Navigate to website
3. Locate elements using CSS selectors or class names
4. Perform interactions (click, input, wait)
5. Validate expected conditions
6. Record results with timestamps
7. Generate HTML report
```

## 🔍 Key Test Methods

### LoginTester
- `test_login_with_number()` - Tests number input and proceed button
- `test_otp_input()` - Tests OTP entry with manual time verification
- `test_login_success()` - Validates successful login
- `generate_html_report()` - Creates detailed HTML report

### NavbarTester
- `test_hamburger_menu_presence()` - Checks hamburger menu visibility
- `test_hamburger_menu_click()` - Tests menu click interactions
- `test_navbar_navigation()` - Tests navigation functionality
- `generate_html_report()` - Creates detailed HTML report

## ⚙️ Configuration

### WebDriver Options
The scripts use Chrome WebDriver. You can customize:
- Browser headless mode
- Window size
- User agent strings
- Proxy settings

Example:
```python
from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # Run in background
driver = webdriver.Chrome(options=options)
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| ChromeDriver not found | Download correct version matching your Chrome browser |
| Element not found | Check CSS selectors/class names match current website |
| Timeout errors | Increase `WebDriverWait` timeout or check internet connection |
| Port already in use | Close other instances of Chrome or WebDriver |

## 📝 Notes

- Tests use **explicit waits** with EC (Expected Conditions) for reliability
- Class-based structure allows easy extension and maintenance
- Timestamps captured for performance analysis
- HTML reports include detailed logging for debugging

## 🤝 Contributing

To contribute improvements:
1. Create a feature branch
2. Make your changes
3. Test thoroughly
4. Submit a pull request

## 📄 License

This project is part of the THE-SOUL-STORE repository owned by LokeshMangrulkar.

## 📧 Contact

For questions or issues, please open an issue on the repository.

---

**Last Updated**: January 18, 2026
