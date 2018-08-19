# encoding: utf-8
# module Task
"""
Bài tập 3
Tạo ngày: 19/8/2018 10:30PM
Bởi: Nguyễn Đăng Nguyên
Đề bài: Viết chương trình giải hệ phương trình tuyến tính bằng phương pháp khử Gauss
Bài làm: Sử dụng phương pháp khử Gauss, đưa ma trận đầu vào thành ma trận tam giác trên xong giải ngược từ cuối lên.
"""

import numpy as np

def _upperTriangularMatrix(input: np.ndarray):
    """
    Chuyển đổi 1 ma trận thành ma trận tam giác trên.
    :param input: ma trận cần tìm.
    :return: ma trận tam giác trên của ma trận đưa vào.
    """
    if len(input) + 1 != len(input[0]):
        raise ValueError("Có gì đó sai sai thì phải???.")
    _length = len(input)
    _result = input.copy()
    for i in range(_length):
        for j in range(i+1, _length):
            if(_result[i][i] != 0):
                _result[j] = _result[j] - _result[i] * _result[j][i]/ _result[i][i]
            else:
                _tmp = _result[i].copy()
                _result[i] = _result[j]
                _result[j] = _tmp
    return _result

def _getResult(input: np.ndarray):
    """
    Giải phương trình với ma trận đầu vào biểu diễn hệ phương trình đó.
    :param input: ma trận biểu diễn hệ phương trình.
    :return: x, y, z,... là kết quả của các biến.
    """
    _upper = _upperTriangularMatrix(input)
    _length = len(_upper)
    _result = []
    for i in range(_length - 1, -1, -1):
        _tmp = 0
        for j in range(len(_result)):
            _tmp += _result[j] * _upper[i][_length - 1 - j]
        if _upper[i][_length - 1 - len(_result)] == 0:
            raise ValueError("Ma trận không thể giải được, vui lòng nhắn tin theo cú pháp: Ahihi gửi 113 để được tư vấn thêm.")
        else:
            _result.append((_upper[i][_length] - _tmp)/ _upper[i][_length - 1 - len(_result)])
    _result.reverse()
    return np.array(_result)
