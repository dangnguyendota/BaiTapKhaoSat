# encoding: utf-8
# module Task
"""
Bài tập 1
Tạo ngày: 19/8/2018 10:15PM
Bởi: Nguyễn Đăng Nguyên
Đề bài: Viết chương trính tính 𝑓(𝑥) = √𝑥 với 𝑥 > 0 mà không sử dụng hàm thư viện sqrt có sẵn.
Bài làm: Sử dụng công thức truy hồi Un = (Un-1 + U0/ Un-1)/2; Với U0 là số cần tìm căn bậc 2. Un là kết quả.
"""

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
