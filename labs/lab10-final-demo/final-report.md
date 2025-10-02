# BÁO CÁO CUỐI KỲ: MINI PROJECT ATM SYSTEM

## Thông tin sinh viên
- **Họ tên:** [Họ tên sinh viên]
- **MSSV:** [Mã số sinh viên]
- **Lớp:** N23DCPT052
- **Môn học:** Nhập môn Công nghệ Phần mềm

## 1. Giới thiệu dự án ATM Mini-Project

### 1.1. Mục tiêu dự án
Xây dựng hệ thống ATM với các chức năng cơ bản:
- ✅ Đăng nhập và xác thực
- ✅ Rút tiền
- ✅ Kiểm tra số dư  
- ✅ Chuyển khoản
- ✅ Bảo trì hệ thống

### 1.2. Phạm vi dự án
- **Frontend:** Java Swing/JavaFX
- **Backend:** Java
- **Database:** MySQL
- **Project Management:** Jira

## 2. Mô hình UML

### 2.1. Use Case Diagram (Lab 02)
![Use Case Diagram](../artifacts/lab02-use-case/use-case-diagram.png)

**Mô tả:** Hệ thống có 2 actor chính: Customer và Technician với các use case tương ứng.

### 2.2. Sequence Diagram (Lab 03)
![Sequence Diagram](../artifacts/lab03-sequence/withdraw-sequence.png)

**Mô tả:** Luồng tương tác khi khách hàng thực hiện rút tiền.

### 2.3. Class Diagram (Lab 06)
![Class Diagram](../artifacts/lab06-class-diagram/class-diagram.png)

**Mô tả:** Cấu trúc các lớp trong hệ thống ATM.

## 3. Database & Code minh họa

### 3.1. ERD Diagram (Lab 05)
![ERD Diagram](../artifacts/lab05-erd-database/atm-erd.png)

### 3.2. Database Schema
```sql
-- Tạo database (Lab 05)
CREATE DATABASE ATMSystem;
USE ATMSystem;

-- Bảng tài khoản
CREATE TABLE Accounts (
    account_id VARCHAR(20) PRIMARY KEY,
    pin_code VARCHAR(6) NOT NULL,
    balance DECIMAL(15,2) DEFAULT 0.00,
    customer_name VARCHAR(100),
    status ENUM('ACTIVE', 'BLOCKED') DEFAULT 'ACTIVE'
);

-- Bảng giao dịch
CREATE TABLE Transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    account_id VARCHAR(20),
    transaction_type ENUM('WITHDRAW', 'TRANSFER', 'BALANCE_CHECK'),
    amount DECIMAL(15,2),
    transaction_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);
