# Lab 07 - Withdraw Module

## Mô tả
Module rút tiền ATM được viết bằng Python kết nối MySQL

## Các chức năng
1. Xác thực PIN
2. Kiểm tra số dư
3. Thực hiện rút tiền
4. Ghi log transaction

## Cấu trúc database cần có
```sql
CREATE DATABASE atm_demo;

CREATE TABLE accounts (
    account_id INT PRIMARY KEY AUTO_INCREMENT,
    balance DECIMAL(15,2) DEFAULT 0
);

CREATE TABLE cards (
    card_no VARCHAR(16) PRIMARY KEY,
    account_id INT,
    pin_hash VARCHAR(64),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE TABLE transactions (
    tx_id INT PRIMARY KEY AUTO_INCREMENT,
    account_id INT,
    card_no VARCHAR(16),
    atm_id INT,
    tx_type ENUM('WITHDRAW', 'DEPOSIT'),
    amount DECIMAL(15,2),
    balance_after DECIMAL(15,2),
    tx_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);