
# Lab 06 - Thiết kế chi tiết lớp & kiến trúc ATM

## 📋 Thông tin
- **Họ tên:** Phạm Thị Ngọc Trần
- **MSSV:** N23DCPT052
- **Lab:** 06 - ATM Class & Package Diagram

## 🏗️ Kiến trúc hệ thống ATM

### 1. Class Diagram
**Mục tiêu:** Mô hình hóa các thực thể chính trong hệ thống ATM

**Các lớp chính:**
- **ATM:** Đại diện máy ATM vật lý, quản lý trạng thái và giao dịch
- **Bank:** Hệ thống ngân hàng trung tâm xử lý nghiệp vụ
- **Card:** Thẻ ATM với thông tin bảo mật
- **Account:** Tài khoản ngân hàng với số dư và nghiệp vụ
- **Transaction:** Giao dịch với trạng thái và lịch sử
- **Customer:** Khách hàng sở hữu tài khoản

**Quan hệ quan trọng:**
- ATM kết nối với Bank để xác thực
- Card truy cập Account
- Mỗi Transaction thuộc về một Account

### 2. Package Diagram
**Mục tiêu:** Tổ chức kiến trúc hệ thống thành các module

**Các package:**
- **UI Layer:** Giao diện người dùng (màn hình, bàn phím)
- **Controller Layer:** Điều phối luồng nghiệp vụ
- **Business Layer:** Nghiệp vụ chính (tài khoản, giao dịch)
- **Data Access Layer:** Truy cập cơ sở dữ liệu
- **Hardware Layer:** Thiết bị phần cứng

### 3. Thiết kế hướng đối tượng
- **Đóng gói:** Thuộc tính private với phương thức public
- **Kế thừa:** Có thể mở rộng cho các loại tài khoản khác nhau
- **Đa hình:** Các loại giao dịch khác nhau

## 🔧 Công cụ sử dụng
- **PlantUML:** Vẽ diagram
- **VS Code:** Soạn thảo code
- **Git:** Quản lý version

## 📁 File structure
