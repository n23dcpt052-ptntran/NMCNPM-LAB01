from withdraw_module import verify_pin, withdraw

# Test case 1: Rút tiền thành công
print("=== Test Case 1: Successful Withdraw ===")
card_no = "1234567890123456"
pin = "1234"
amount = 100000

if verify_pin(card_no, pin):
    success, message = withdraw(card_no, amount)
    print(f"Result: {message}")
else:
    print("PIN verification failed")

# Test case 2: Số dư không đủ
print("\n=== Test Case 2: Insufficient Funds ===")
amount = 10000000  # Số tiền rất lớn
if verify_pin(card_no, pin):
    success, message = withdraw(card_no, amount)
    print(f"Result: {message}")