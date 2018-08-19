# encoding: utf-8
# module Task
"""
Bài tập 4
Tạo ngày: 19/8/2018 10:00PM
Bởi: Nguyễn Đăng Nguyên
Đề bài: .....
Bài làm: df/dy0 = (df/dx0) / (dy0/dx0). mà phương trình y0 theo x0, x1 có rồi nên tính ra được dy0/dx0,
tương tự ta tính được df/dx1 dựa vào df/dy1. Xong nhân ngược sang ra kết quả.
"""

import numpy as np

def _get(input: np.ndarray, factor: np.ndarray, padding: np.ndarray):
    """
    Lấy giá trị cần tính
    :param input: kết quả ban đầu
    :param factor: hệ số của y0, y1 với x0, x1
    :param padding: phần bù thêm vào.
    :return:
    """
    _tmp = np.array([factor[0][0], factor[1][1]])
    return input * _tmp