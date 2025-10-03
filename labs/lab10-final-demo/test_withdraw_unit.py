import pytest
import sqlite3
import hashlib
import os

def setup_database():
    """Tạo database và dữ liệu test"""
    conn = sqlite3.connect('test_atm.db')
    cur = conn.cursor()
    
    # Tạo tables
    cur.execute('''
        CREATE TABLE IF NOT EXISTS accounts (
            account_id INTEGER PRIMARY KEY,
            balance DECIMAL(15,2)
        )
    ''')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS cards (
            card_no TEXT PRIMARY KEY,
            account_id INTEGER,
            pin_hash TEXT
        )
    ''')
    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS transactions (
            tx_id INTEGER PRIMARY KEY,
            account_id INTEGER,
            card_no TEXT,
            amount DECIMAL(15,2),
            balance_after DECIMAL(15,2)
        )
    ''')
    
    # Xóa dữ liệu cũ và thêm mới
    cur.execute("DELETE FROM accounts")
    cur.execute("DELETE FROM cards")
    cur.execute("DELETE FROM transactions")
    
    # Thêm dữ liệu test
    cur.execute("INSERT INTO accounts (account_id, balance) VALUES (1, 1000000)")
    pin_hash = hashlib.sha256("1234".encode()).hexdigest()
    cur.execute("INSERT INTO cards (card_no, account_id, pin_hash) VALUES (?, ?, ?)", 
               ('1234567890123456', 1, pin_hash))
    
    conn.commit()
    conn.close()

def verify_pin(card_no, pin):
    """Xác thực PIN"""
    try:
        conn = sqlite3.connect('test_atm.db')
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
    """Rút tiền"""
    try:
        conn = sqlite3.connect('test_atm.db')
        cur = conn.cursor()
        
        cur.execute('''
            SELECT accounts.account_id, accounts.balance 
            FROM accounts 
            JOIN cards ON accounts.account_id = cards.account_id
            WHERE cards.card_no = ?
        ''', (card_no,))
        
        result = cur.fetchone()
        if not result:
            return False, "Card not found"
            
        account_id, balance = result
        
        if balance < amount:
            return False, "Insufficient funds"
        
        new_balance = balance - amount
        cur.execute("UPDATE accounts SET balance = ? WHERE account_id = ?", 
                   (new_balance, account_id))
        
        cur.execute('''
            INSERT INTO transactions(account_id, card_no, amount, balance_after) 
            VALUES(?, ?, ?, ?)
        ''', (account_id, card_no, amount, new_balance))
        
        conn.commit()
        conn.close()
        return True, f"Withdraw success! New balance: {new_balance:,} VND"
        
    except Exception as e:
        return False, f"Error: {str(e)}"

class TestATMWithdraw:
    def setup_method(self):
        """Chuẩn bị database trước mỗi test"""
        setup_database()
        self.valid_card = "1234567890123456"
        self.valid_pin = "1234"
        self.invalid_pin = "9999"
        self.invalid_card = "0000000000000000"
    
    def test_verify_pin_correct(self):
        assert verify_pin(self.valid_card, self.valid_pin) == True
    
    def test_verify_pin_incorrect(self):
        assert verify_pin(self.valid_card, self.invalid_pin) == False
    
    def test_verify_pin_invalid_card(self):
        assert verify_pin(self.invalid_card, self.valid_pin) == False
    
    def test_withdraw_success(self):
        success, message = withdraw(self.valid_card, 50000)
        assert success == True
        assert "success" in message.lower()
    
    def test_withdraw_insufficient_funds(self):
        success, message = withdraw(self.valid_card, 10000000)
        assert success == False
        assert "insufficient" in message.lower()
    
    def test_withdraw_invalid_card(self):
        success, message = withdraw(self.invalid_card, 100000)
        assert success == False
        assert "not found" in message.lower()

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
