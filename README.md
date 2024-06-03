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

- Giao diện trang chủ
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/b2023ac5-c090-43bb-8d34-3c336b04cb57)
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/09194f45-eed7-4f9b-803a-8517e80ea6c7)
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/a4a7d719-210a-4595-86e8-9cc6839d3960)
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/f70ce1ea-be21-48f8-b4a9-81cd268f70af)
- Giao diện event
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/2cfb5155-7559-404d-8ac8-58d799596fba)
- Giao diện location
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/3b645a1a-8db5-4661-856c-8ee141e24e84)
- Giao diện menu
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/8ca01e9e-edf9-4915-a80e-5af5ca2a8e09)
- Giao diện delivery
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/dc5a7c20-d06b-4a5e-bb6a-f719641dd4b9)
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/bf6b8558-b70d-4d07-a275-ea758d988dcd)
- Giao diện cart
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/de9610d5-260b-4217-9c6d-9f95bb56b2bc)
- Giao diện checkout
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/da285346-e106-4c07-86af-c0ffb1eaff5f)
- Giao diện account
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/3943a66e-20c2-428b-b3f0-cd11519e1172)
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/8ccc0216-7096-4d20-8dd9-7244db652835)
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/fc83b1da-a7ba-460d-b0d6-6f73a42b937c)
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/04a17310-cf6d-479f-809d-afe6b7eeb164)
- Sign in/ Sign up
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/2e98917d-1e6a-44e1-a8b1-538f02e8f52a)
![image](https://github.com/PhucsS24/Restaurant-manage/assets/131946074/d6e0ca9f-c62a-4bb1-bfb7-7866a04ae6fb)














