# encoding: utf-8
# module Task
"""
Bài tập 1
Tạo ngày: 19/8/2018 10:15PM
Bởi: Nguyễn Đăng Nguyên
Đề bài: Viết chương trính tính 𝑓(𝑥) = √𝑥 với 𝑥 > 0 mà không sử dụng hàm thư viện sqrt có sẵn.
Bài làm: Sử dụng công thức truy hồi Un = (Un-1 + U0/ Un-1)/2; Với U0 là số cần tìm căn bậc 2. Un là kết quả.
"""

import numpy as np

def __sqrt__(number):
    """
    Hàm tra về căn bậc 2 của 1 số bất kỳ lớn hơn 0.
    :param number: Số cần tìm căn bậc 2.
    :return: giá trị căn bậc 2 của số đưa vào.
    """
    if number < 0:
        raise ValueError("Căn bậc 2 của một số âm không khả dụng!")
    elif number == 0:
        return 0
    _root = number
    _last = _root
    _root = (_root + number / _root) / 2
    while _root - _last < -1e-17:
        _last = _root
        _root = (_root + number / _root) / 2
    return _root

def _newSqrt(number):
    """
    Tính căn bậc 2 của một số sử dụng phương pháp newton x = x - fx/f'x.
    Bước 1: Ta có log2(1/√𝑥 ) = -0.5 * log2(x).
    Bước 2: Tính log2(x):
    - biểu diễn: x = 2^ex . (1 + mx)
    -> log2(x) = ex + log2(1+mx) (mx ∈ [0, 1))
    - log2(1+mx) ~ mx + o ( o là tham số để điều chỉnh sai số)
    -> log2(x) ~ ex + mx + o
    - Biểu diễn x dưới dạng bit:
      + Ix = Ex.L + Mx
      + Ix = L(ex + B +mx) ~ L.log2(x) + L(B - o)
      -> log2(x) ~ Ix/L - (B - o)
      log2(1/√𝑥 ) = -0.5 * log2(x)
      -> I(1/√𝑥 )/ L - (B - o) ~ -0.5 * (Ix/L - (B - o))
      -> I(1/√𝑥 ) ~ 1.5 * L(B-o) - 0.5 Ix
      Trong đó 1.5 * L(B - o) = 0x5F3759DF
      còn 0.5 * Ix chính là i >> 1(dịch phải 1 tương đương với chia cho 2).
      Sau khi đã tính được log2(x) ta sử dụng phương pháp Newton:
      đặt 1/√𝑥  = t
      ta có: f(t) = 1/t^2 - x = 0
      f'(t) = -2/t^3
      ta có t = t - f(t)/f'(f)
      -> t = t0- (1/t0^2 - x)/(-2/t0^3) = t(3-x.t0^2)/2
     Ta có t0 đx được tính ở trên: t0 = 0x5f3759df - Ix >> 1
     t = 1/√𝑥 suy ra 1/t = √𝑥
    :param number:
    :return:
    """
    y = np.float32(number)
    i = y.view(np.int32)
    #Tính t0
    i = np.int32(0x5f3759df) - np.int32(i >> 1)
    #Tính t
    y = i.view(np.float32)
    y = y * (3 - number * y * y)/2
    return 1/float(y)
