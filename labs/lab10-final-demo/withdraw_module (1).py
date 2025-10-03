import sqlite3
import hashlib
import os

def init_database():
    """Khởi tạo database SQLite"""
    conn = sqlite3.connect('atm_demo.db')
    cur = conn.cursor()
    
    # Tạo tables
    cur.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY AUTOINCREMENT,
            balance DECIMAL(15,2) DEFAULT 0
        )
    ''')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            card_no TEXT PRIMARY KEY,
            account_id INTEGER,
            pin_hash TEXT,
            FOREIGN KEY (account_id) REFERENCES accounts(account_id)
        )
    ''')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
            account_id INTEGER,
            card_no TEXT,
            atm_id INTEGER,
            tx_type TEXT,
            amount DECIMAL(15,2),
            balance_after DECIMAL(15,2),
            tx_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Thêm dữ liệu test nếu chưa có
    cur.execute("SELECT COUNT(*) FROM accounts")
    if cur.fetchone()[0] == 0:
        cur.execute("INSERT INTO accounts (account_id, balance) VALUES (1, 5000000)")
        pin_hash = hashlib.sha256("1234".encode()).hexdigest()
        cur.execute("INSERT INTO cards (card_no, account_id, pin_hash) VALUES (?, ?, ?)", 
                   ('1234567890123456', 1, pin_hash))
    
    conn.commit()
    conn.close()

def verify_pin(card_no, pin):
    """Xác thực PIN của thẻ"""
    try:
        conn = sqlite3.connect('atm_demo.db')
        cur = conn.cursor()
        cur.execute("SELECT pin_hash FROM cards WHERE card_no=?", (card_no,))
        row = cur.fetchone()
        conn.close()
        
        if row:
            pin_hash = hashlib.sha256(pin.encode()).hexdigest()
            return row[0] == pin_hash
        return False
    except Exception as e:
        print(f"Database error: {e}")
        return False

def withdraw(card_no, amount):
    """Thực hiện rút tiền"""
    conn = sqlite3.connect('atm_demo.db')
    cur = conn.cursor()
    
    try:
        # Kiểm tra số dư
        cur.execute('''
            SELECT account_id, balance 
            FROM accounts 
            JOIN cards USING(account_id) 
            WHERE card_no=?
        ''', (card_no,))
        
        result = cur.fetchone()
        if not result:
            raise Exception("Card not found")
            
        account_id, balance = result
        
        # Kiểm tra số dư
        if balance < amount:
            raise Exception("Insufficient funds")
        
        # Cập nhật số dư
        new_balance = balance - amount
        cur.execute(
            "UPDATE accounts SET balance=? WHERE account_id=?",
            (new_balance, account_id)
        )
        
        # Ghi log transaction
        cur.execute('''
            INSERT INTO transactions(account_id, card_no, atm_id, tx_type, amount, balance_after) 
            VALUES(?, ?, 1, 'WITHDRAW', ?, ?)
        ''', (account_id, card_no, amount, new_balance))
        
        conn.commit()
        return True, f"Withdraw success! New balance: {new_balance:,.0f} VND"
        
    except Exception as e:
        conn.rollback()
        return False, f"Error: {e}"
    finally:
        conn.close()

# Hàm main để test
if __name__ == "__main__":
    print("=== ATM Withdraw Module Test ===")
    
    # Khởi tạo database
    init_database()
    
    # Test data
    card_no = "1234567890123456"
    pin = "1234"
    amount = 100000
    
    print(f"Card: {card_no}")
    print(f"PIN: {pin}")
    print(f"Amount: {amount:,.0f} VND")
    print("-" * 30)
    
    if verify_pin(card_no, pin):
        print("✓ PIN verification successful")
        success, message = withdraw(card_no, amount)
        print(f"Result: {message}")
    else:
        print("✗ Invalid PIN")