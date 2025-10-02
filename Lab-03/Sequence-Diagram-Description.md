# MÔ TẢ SEQUENCE DIAGRAM - THÊM SẢN PHẨM VÀO GIỎ HÀNG

## 📋 Tổng quan quy trình
**Quy trình:** Thêm sản phẩm vào giỏ hàng  
**Mô tả:** User thực hiện thao tác thêm sản phẩm vào giỏ hàng, hệ thống xử lý và trả về kết quả

## 👥 Các đối tượng tham gia

### 1. User (Actor)
- **Vai trò:** Người sử dụng hệ thống
- **Hành động:** Khởi tạo quy trình thêm sản phẩm

### 2. UI/Frontend
- **Vai trò:** Giao diện người dùng
- **Chức năng:** Tiếp nhận yêu cầu từ user và hiển thị kết quả

### 3. CartController
- **Vai trò:** Điều phối các yêu cầu liên quan đến giỏ hàng
- **Chức năng:** Nhận request, gọi service, trả response

### 4. ProductService
- **Vai trò:** Xử lý logic nghiệp vụ sản phẩm
- **Chức năng:** Kiểm tra tồn kho, thông tin sản phẩm

### 5. CartService
- **Vai trò:** Xử lý logic nghiệp vụ giỏ hàng
- **Chức năng:** Quản lý giỏ hàng, cart items

### 6. Database
- **Vai trò:** Lưu trữ dữ liệu
- **Chức năng:** Thực hiện các thao tác CRUD

## 📨 Thông điệp trao đổi

### Giai đoạn 1: Kiểm tra sản phẩm
1. **User → UI:** `clickAddToCart(productId, quantity)`
   - User click nút thêm vào giỏ hàng
2. **UI → CartController:** `POST /api/cart/add`
   - Gửi yêu cầu HTTP đến backend
3. **CartController → ProductService:** `checkProductAvailability(productId, quantity)`
   - Kiểm tra sản phẩm có đủ hàng không
4. **ProductService → Database:** `SELECT * FROM products`
   - Truy vấn thông tin sản phẩm

### Giai đoạn 2: Xử lý giỏ hàng
5. **CartController → CartService:** `addToCart(sessionId, productId, quantity)`
   - Gọi service xử lý thêm vào giỏ hàng
6. **CartService → Database:** `SELECT/INSERT carts`
   - Tìm hoặc tạo giỏ hàng mới
7. **CartService → Database:** `SELECT/INSERT/UPDATE cart_items`
   - Thêm hoặc cập nhật sản phẩm trong giỏ

### Giai đoạn 3: Cập nhật và phản hồi
8. **CartService → Database:** `UPDATE products SET stock = stock - quantity`
   - Cập nhật số lượng tồn kho
9. **CartService → CartController:** `CartUpdateResponse`
   - Trả về kết quả cập nhật
10. **CartController → UI:** `200 OK`
    - Phản hồi thành công
11. **UI → User:** Hiển thị thông báo thành công

## ⚠️ Luồng thay thế (Alternative Flow)
- **Sản phẩm hết hàng:** Dừng quy trình và thông báo lỗi
- **Giỏ hàng chưa tồn tại:** Tạo giỏ hàng mới
- **Sản phẩm đã có trong giỏ:** Cập nhật số lượng

## 💾 Thao tác database
- **SELECT:** Lấy thông tin sản phẩm, giỏ hàng
- **INSERT:** Tạo giỏ hàng mới, thêm cart item
- **UPDATE:** Cập nhật số lượng, tồn kho
