# WEBSITE QUẢN LÝ VÀ ĐẶT CHỖ NHÀ HÀNG

## Giới thiệu
- Website với mục đích đặt chỗ online, quản lý nhà hàng.
- Công nghệ sử dụng: HTML, CSS, JS, Python Django
- Thành viên nhóm:
  
| Họ tên              | MSSV     |
|---------------------|----------|
| Lê Công Hiếu        | 20521319 |
| Nguyễn Hoàng Phúc   | 20520277 |
| Nguyễn Văn Đức Ngọc | 20521666 |
| Phạm Văn Ngọ        | 20520254 |

## I. Setup local
### Nếu chưa cài môi trường thì tải env
1. pip install virtualenv
2. virtualenv env
3. env\Scripts\activate
4. pip install requirements.txt
### Nếu đã cài rồi
- Sau khi tải xong, tại thư mục Restaurant-manage: env\Scripts\activate
- Sau khi vào đc môi trường env kiểm tra lại đầu thư mục đã có (env) chưa. Trong môi trường này do được cài sẵn các thư viện lên hạn chế lỗi. Nếu bị lỗi thiếu thư viện có thể do chưa vào môi trường env.
- Kiểm tra lại thư mục Restaurant-manage đã có những folder này chưa.
```
\env
\restaurant_manage
\README.md
```
### Đã setup chung, ko cần làm nữa.
Setup MySQL
- root
- 123456

## II. Tổng quan chức năng

| Chức năng            | Mô tả                                                      |
|----------------------|------------------------------------------------------------|
| Đăng ký              | Tạo tài khoản trên hệ thống giúp quản lý thông tin đặt bàn |
| Đăng nhập/ Đăng xuất | Truy cập/thoát vào/khỏi hệ thống                           |
| Đặt chỗ              | Đặt chỗ online                                             |
| Cart                 | Quản lý thông tin đặt hàng các món ăn trên menu            |
| Thanh toán           | Tích hợp thanh toán qua paypal                             |
| Địa điểm             | Tích hợp google map địa chỉ nhà hàng                       |

## III. Tổng quan giao diện hệ thống
