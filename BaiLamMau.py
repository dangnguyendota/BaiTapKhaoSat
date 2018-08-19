# encoding: utf-8
"""
Tạo ngày: 19/8/2018 10:00PM
Bởi: Nguyễn Đăng Nguyên
Bài giải mẫu các hàm trong các module.
Các bài toán được thiết kế giải bài toán tổng quát, không riêng gì trường hợp đề bài cho.
File gồm 7 packages tương ứng với 7 bài tập.
- Mỗi package gồm 2 file:
  + __init__.py : dùng để gọi hàm.
  + Task.py : là file code chính của bài tập, chứa các hàm chính.
"""

import numpy as np
import BT1
import BT2
import BT3
import BT4
import BT5
import BT6
import BT7

# Lời giải bài tập 1:
# Code nằm trong thư mục BT1/__init__.py, BT1/Task.py
print("\n******************* Bài tập 1***********************")
print("Căn bậc 2 của 2:", BT1.sqrt(2))  # 1.414213562373095
print("Căn bậc 2 của 4:", BT1.sqrt(4))  # 2.0
print("Căn bậc 2 của 10.19:", BT1.sqrt(10.19))  # 3.1921779399024732

# Lời giải bài tập 2:
# Code nằm trong thư mục BT2/__init__.py, BT2/Task.py
print("\n******************* Bài tập 2***********************")
a = BT2.Point(2, 4, 5)
b = BT2.Point(4, 7, 9)
c = BT2.Point(7, 9, 2)
d = BT2.Point(30, 25, 56)
proj = BT2.projection(d, a, b, c)  # proj là hình chiếu của điểm d lên mặt phằng chứa 3 điểm a, b, c
print("Hình chiếu d có tọa độ:", proj.toString())  # in kết quả ra màn hình

# Lời giải bài tập 3:
# Code nằm trong thư mục BT3/__init__.py, BT3/Task.py
print("\n******************* Bài tập 3***********************")
factor = np.array([[3., 4., 2., 7., 129.],
                   [7., 5., 1., 9., 151.],
                   [8., 12., 25., 3., 709.],
                   [9., 11., 15., 7., 505.]])
bt3Result = BT3.getResult(factor)
print("Bài tập 3: x, y, z, t = ", bt3Result)

# Lời giải bài tập 4:
# Code nằm trong thư mục BT4/__init__.py, BT4/Task.py
print("\n******************* Bài tập 4***********************")
input = np.array([5., 12])
factor = np.array([[5., 3.], [7., 2.]])
padd = np.array([1., 9.])
print("Kết quả:", BT4.get(input, factor, padd))

# Lời giải bài tập 5
# Code nằm trong thư mục BT5/__init__.py, BT5/Task.py
print("\n******************* Bài tập 5***********************")
print("Xác suất tung 5 lần có tổng 17 là:",BT5.xs(5, 17)) # 5 là số lần xúc xắc, 17 là tổng kì vọng.

# Lời giải bài tập 6
# Code nằm trong thư mục BT6/__init__.py, BT6/Task.py
print("\n******************* Bài tập 6***********************")
factor = np.array([7., 3., -2., 5., 4.])
print("nghiệm của phương trình: ", BT6.find(factor, 1000.))

# Lời giải bài tập 7
# Code nằm trong thư mục BT7/__init__.py, BT7/Task.py
print("\n******************* Bài tập 7***********************")
factor = np.array([[0.3, 0.7], [0.6, 0.4]]) # Xác suất chuyển đổi.
today = np.array([0.5, 0.5]) # Xác suất nắng mưa hôm nay.
print("Xác suất nắng mưa ngày sau 7 ngày [nắng, mưa]:",BT7.xs(today, factor, 7)) # 7 là 7 ngày, 1 tuần.
