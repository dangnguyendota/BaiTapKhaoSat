# encoding: utf-8
# module Task
"""
Bài tập 4
Tạo ngày: 19/8/2018 10:00PM
Bởi: Nguyễn Đăng Nguyên
Đề bài: .....
Bài làm: df/dy = (df/dx) / (dy/dx). mà phương trình y theo x có rồi nên tính ra được dy/dx. Xong nhân ngược sang ra kết quả.
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
    return np.dot(factor, input)