"""
Selenium script to test website login functionality with:
1. Number input (class selector)
2. Proceed button
3. OTP input with manual time entry
4. Login success/failure validation
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
import time
from datetime import datetime


class LoginTester:
    def __init__(self, website_url):
        """Initialize the WebDriver and navigate to the website"""
        self.website_url = website_url
        self.driver = webdriver.Chrome()  # Make sure ChromeDriver is installed
        self.wait = WebDriverWait(self.driver, 10)
        self.test_results = []
        self.start_time = None
        self.end_time = None
        
    def test_login_with_number(self, number_input):
        """
        Test Step 1: Enter number and click proceed
        
        Args:
            number_input (str): The number to enter in the first input field
        """
        step_start = time.time()
        try:
            print(f"\n[STEP 1] Navigating to {self.website_url}")
            self.driver.get(self.website_url)
            time.sleep(2)
            
            # Find the number input field using class attribute
            print("[STEP 1] Looking for number input field...")
            number_field = self.wait.until(
                EC.presence_of_element_located((By.CLASS_NAME, "login-input-field"))
            )
            
            # Clear and enter the number
            number_field.clear()
            number_field.send_keys(number_input)
            print(f"[SUCCESS] Entered number: {number_input}")
            
            # Click the proceed button
            print("[STEP 1] Clicking proceed button...")
            proceed_btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-proceed.btn-block.text-uppercase.pointer"))
            )
            proceed_btn.click()
            print("[SUCCESS] Proceed button clicked")
            
            # Wait for OTP screen to appear
            time.sleep(2)
            
            step_duration = time.time() - step_start
            self.test_results.append({
                'step': 'Step 1: Number Input & Proceed',
                'status': 'PASSED',
                'message': f'Successfully entered number {number_input} and clicked proceed',
                'duration': f'{step_duration:.2f}s'
            })
            return True
            
        except Exception as e:
            step_duration = time.time() - step_start
            self.test_results.append({
                'step': 'Step 1: Number Input & Proceed',
                'status': 'FAILED',
                'message': str(e),
                'duration': f'{step_duration:.2f}s'
            })
            print(f"[ERROR] Step 1 failed: {str(e)}")
            return False
    
    def test_otp_entry(self, otp_code, wait_seconds=0):
        """
        Test Step 2: Wait for manual OTP entry, then click verify.
        Args:
            otp_code (str): Unused; kept for API compatibility.
            wait_seconds (int): Time to wait before clicking verify (user enters OTP manually).
        """
        step_start = time.time()
        try:
            print(f"\n[STEP 2] Waiting for manual OTP entry")

            if wait_seconds > 0:
                print(f"[INFO] Waiting {wait_seconds} seconds before clicking verify...")
                time.sleep(wait_seconds)

            # Click verify/submit button (after user has entered OTP manually)
            print("[STEP 2] Clicking OTP verify button...")
            verify_btn = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-main.btn-block.text-uppercase.sendlink.mt30"))
            )
            verify_btn.click()
            print("[SUCCESS] OTP verify button clicked")

            # Wait for response
            time.sleep(8)
            
            step_duration = time.time() - step_start
            self.test_results.append({
                'step': 'Step 2: OTP Verification',
                'status': 'PASSED',
                'message': 'Successfully clicked OTP verify button after manual entry',
                'duration': f'{step_duration:.2f}s'
            })
            return True

        except Exception as e:
            step_duration = time.time() - step_start
            self.test_results.append({
                'step': 'Step 2: OTP Verification',
                'status': 'FAILED',
                'message': str(e),
                'duration': f'{step_duration:.2f}s'
            })
            print(f"[ERROR] Step 2 failed: {str(e)}")
            return False
    
    def check_login_success(self):
        """
        Check if login was successful by looking for the track-order nav element.
        
        Returns:
            tuple: (success: bool, message: str)
        """
        step_start = time.time()
        try:
            print("\n[STEP 3] Verifying login status...")
            # Primary check: presence of track-order nav item implies authenticated session
            track_order_element = self.wait.until(
                EC.presence_of_element_located(
                    (
                        By.CSS_SELECTOR,
                        ".nav-item.navicon.track-order",
                    )
                )
            )
            print("[SUCCESS] Track-order element found - login confirmed")
            
            step_duration = time.time() - step_start
            self.test_results.append({
                'step': 'Step 3: Login Verification',
                'status': 'PASSED',
                'message': 'Track-order nav item present; user successfully logged in',
                'duration': f'{step_duration:.2f}s'
            })
            return True, "Track-order nav item present; user was logged in"
                        
        except Exception as e:
            step_duration = time.time() - step_start
            self.test_results.append({
                'step': 'Step 3: Login Verification',
                'status': 'FAILED',
                'message': str(e),
                'duration': f'{step_duration:.2f}s'
            })
            print(f"[ERROR] Could not verify login status: {str(e)}")
            return False, str(e)
    
    def generate_html_report(self, overall_result):
        """
        Generate an HTML test report
        
        Args:
            overall_result (bool): Overall test result (pass/fail)
        """
        total_duration = (self.end_time or 0) - (self.start_time or 0)
        passed_tests = sum(1 for result in self.test_results if result['status'] == 'PASSED')
        failed_tests = sum(1 for result in self.test_results if result['status'] == 'FAILED')
        
        html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login Test Report - {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            padding: 20px;
            min-height: 100vh;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background: white;
            border-radius: 10px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
            overflow: hidden;
        }}
        .header {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 30px;
            text-align: center;
        }}
        .header h1 {{
            font-size: 2.5em;
            margin-bottom: 10px;
        }}
        .header p {{
            font-size: 1.1em;
            opacity: 0.9;
        }}
        .summary {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 30px;
            background: #f8f9fa;
        }}
        .summary-card {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
            text-align: center;
        }}
        .summary-card h3 {{
            color: #666;
            font-size: 0.9em;
            text-transform: uppercase;
            margin-bottom: 10px;
        }}
        .summary-card .value {{
            font-size: 2em;
            font-weight: bold;
            color: #333;
        }}
        .summary-card.passed .value {{
            color: #28a745;
        }}
        .summary-card.failed .value {{
            color: #dc3545;
        }}
        .summary-card.overall {{
            grid-column: 1 / -1;
        }}
        .overall.passed {{
            background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
            color: white;
        }}
        .overall.failed {{
            background: linear-gradient(135deg, #dc3545 0%, #fd7e14 100%);
            color: white;
        }}
        .overall h3 {{
            color: white;
        }}
        .test-details {{
            padding: 30px;
        }}
        .test-details h2 {{
            color: #333;
            margin-bottom: 20px;
            border-bottom: 3px solid #667eea;
            padding-bottom: 10px;
        }}
        .test-step {{
            background: #f8f9fa;
            border-left: 4px solid #667eea;
            padding: 20px;
            margin-bottom: 15px;
            border-radius: 5px;
            transition: transform 0.2s;
        }}
        .test-step:hover {{
            transform: translateX(5px);
        }}
        .test-step.passed {{
            border-left-color: #28a745;
        }}
        .test-step.failed {{
            border-left-color: #dc3545;
        }}
        .test-step-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 10px;
        }}
        .test-step-title {{
            font-size: 1.2em;
            font-weight: bold;
            color: #333;
        }}
        .status-badge {{
            padding: 5px 15px;
            border-radius: 20px;
            font-weight: bold;
            font-size: 0.9em;
        }}
        .status-badge.passed {{
            background: #28a745;
            color: white;
        }}
        .status-badge.failed {{
            background: #dc3545;
            color: white;
        }}
        .test-step-message {{
            color: #666;
            margin-bottom: 10px;
            line-height: 1.6;
        }}
        .test-step-duration {{
            color: #999;
            font-size: 0.9em;
        }}
        .footer {{
            background: #f8f9fa;
            padding: 20px;
            text-align: center;
            color: #666;
            border-top: 1px solid #dee2e6;
        }}
        .test-info {{
            background: white;
            padding: 20px;
            margin: 20px 30px;
            border-radius: 8px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        .test-info-row {{
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #eee;
        }}
        .test-info-row:last-child {{
            border-bottom: none;
        }}
        .test-info-label {{
            font-weight: bold;
            color: #666;
        }}
        .test-info-value {{
            color: #333;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🔐 Login Functionality Test Report</h1>
            <p>Automated Selenium Test Execution</p>
        </div>
        
        <div class="summary">
            <div class="summary-card overall {'passed' if overall_result else 'failed'}">
                <h3>Overall Status</h3>
                <div class="value">{'✓ PASSED' if overall_result else '✗ FAILED'}</div>
            </div>
            <div class="summary-card passed">
                <h3>Passed Tests</h3>
                <div class="value">{passed_tests}</div>
            </div>
            <div class="summary-card failed">
                <h3>Failed Tests</h3>
                <div class="value">{failed_tests}</div>
            </div>
            <div class="summary-card">
                <h3>Total Duration</h3>
                <div class="value">{total_duration:.2f}s</div>
            </div>
        </div>
        
        <div class="test-info">
            <div class="test-info-row">
                <span class="test-info-label">Website URL:</span>
                <span class="test-info-value">{self.website_url}</span>
            </div>
            <div class="test-info-row">
                <span class="test-info-label">Test Execution Time:</span>
                <span class="test-info-value">{datetime.fromtimestamp(self.start_time or 0).strftime('%Y-%m-%d %H:%M:%S')}</span>
            </div>
            <div class="test-info-row">
                <span class="test-info-label">Browser:</span>
                <span class="test-info-value">Chrome</span>
            </div>
        </div>
        
        <div class="test-details">
            <h2>📋 Test Execution Details</h2>
            {''.join([f'''
            <div class="test-step {result['status'].lower()}">
                <div class="test-step-header">
                    <span class="test-step-title">{result['step']}</span>
                    <span class="status-badge {result['status'].lower()}">{result['status']}</span>
                </div>
                <div class="test-step-message">{result['message']}</div>
                <div class="test-step-duration">⏱ Duration: {result['duration']}</div>
            </div>
            ''' for result in self.test_results])}
        </div>
        
        <div class="footer">
            <p>Generated by Selenium Login Test Automation</p>
            <p>Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
        </div>
    </div>
</body>
</html>
        """
        
        # Save the report
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        report_filename = f"test_reports/login_test_report_{timestamp}.html"
        
        # Create test_reports directory if it doesn't exist
        import os
        os.makedirs('test_reports', exist_ok=True)
        
        with open(report_filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"\n[REPORT] HTML report generated: {report_filename}")
        return report_filename
    
    def run_complete_login_test(self, number, otp, wait_before_otp=0):
        """
        Run the complete login test flow
        
        Args:
            number (str): The number to enter
            otp (str): The OTP code to enter
            wait_before_otp (int): Seconds to wait before entering OTP
        """
        self.start_time = time.time()
        
        print("="*60)
        print("STARTING LOGIN FUNCTIONALITY TEST")
        print(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)
        
        # Step 1: Number input and proceed
        if not self.test_login_with_number(number):
            self.end_time = time.time()
            self.generate_html_report(False)
            self.close()
            return False
        
        # Step 2: OTP entry
        if not self.test_otp_entry(otp, wait_before_otp):
            self.end_time = time.time()
            self.generate_html_report(False)
            self.close()
            return False
        
        # Step 3: Check login status
        success, message = self.check_login_success()
        
        self.end_time = time.time()
        
        print("="*60)
        print(f"TEST RESULT: {'PASSED' if success else 'FAILED'}")
        print(f"Message: {message}")
        print("="*60)
        
        # Generate HTML report
        self.generate_html_report(success)
        
        return success
    
    def close(self):
        """Close the WebDriver"""
        self.driver.quit()
        print("\n[INFO] Browser closed")


# Main test execution
if __name__ == "__main__":
    
    # Configuration
    WEBSITE_URL = "https://www.thesouledstore.com/login"  # Replace with actual website URL
    TEST_NUMBER = "9370277695"  # Replace with actual test number
    TEST_OTP = "123456"  # Replace with actual test OTP
    WAIT_BEFORE_OTP = 20  # Seconds to wait before entering OTP (for manual observation)
    
    # Create tester instance
    tester = LoginTester(WEBSITE_URL)
    
    try:
        # Run the login test
        result = tester.run_complete_login_test(
            number=TEST_NUMBER,
            otp=TEST_OTP,
            wait_before_otp=WAIT_BEFORE_OTP
        )
        
        # Keep browser open for 5 seconds to see the result
        time.sleep(10)
        
    except Exception as e:
        print(f"[CRITICAL ERROR] {str(e)}")
        
    finally:
        tester.close()
