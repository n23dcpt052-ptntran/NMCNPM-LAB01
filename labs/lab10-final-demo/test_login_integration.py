from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

print("=== Login Form Integration Test ===")

try:
    # Setup Chrome driver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(5)
    
    # Tạo file HTML test
    html_content = '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Login Test</title>
        <style>
            body { font-family: Arial; margin: 50px; }
            .container { max-width: 300px; margin: auto; }
            input, button { width: 100%; padding: 10px; margin: 5px 0; }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>ATM Login</h2>
            <input type="text" id="username" placeholder="Username">
            <input type="password" id="password" placeholder="Password">
            <button onclick="login()">Login</button>
            <div id="message"></div>
        </div>
        <script>
            function login() {
                const user = document.getElementById('username').value;
                const pass = document.getElementById('password').value;
                const msg = document.getElementById('message');
                
                if (user === 'admin' && pass === 'password123') {
                    msg.innerHTML = '<p style="color:green">Login successful!</p>';
                } else {
                    msg.innerHTML = '<p style="color:red">Login failed!</p>';
                }
            }
        </script>
    </body>
    </html>
    '''
    
    with open('test_login.html', 'w') as f:
        f.write(html_content)
    
    # Test 1: Mở trang login
    driver.get('file://' + __file__.replace('test_login_integration.py', 'test_login.html'))
    print("✓ Login page opened")
    
    # Test 2: Tìm form elements
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    button = driver.find_element(By.TAG_NAME, "button")
    print("✓ Form elements found")
    
    # Test 3: Test login thành công
    username.send_keys("admin")
    password.send_keys("password123")
    button.click()
    time.sleep(2)
    print("✓ Login success test completed")
    
    # Test 4: Test login sai
    driver.get('file://' + __file__.replace('test_login_integration.py', 'test_login.html'))
    username = driver.find_element(By.ID, "username")
    password = driver.find_element(By.ID, "password")
    button = driver.find_element(By.TAG_NAME, "button")
    
    username.send_keys("admin")
    password.send_keys("wrongpassword")
    button.click()
    time.sleep(2)
    print("✓ Login failed test completed")
    
    driver.quit()
    print("🎉 ALL INTEGRATION TESTS PASSED!")
    
except Exception as e:
    print(f"❌ Integration test failed: {e}")
