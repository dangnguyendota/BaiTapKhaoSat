# encoding: utf-8
# module Task
"""
Bài tập 6
Tạo ngày: 19/8/2018 11:30PM
Bởi: Nguyễn Đăng Nguyên
Đề bài: Cho hàm 𝑓(𝑥) = 4𝑥^4 + 5𝑥^3 − 2𝑥^2 + 3𝑥 + 7. Viết chương trình tìm ít nhất một giá trị của 𝑥 (giá trị xấp xỉ) để 𝑓(𝑥) = 1000.
Bài làm: Sử dụng phương pháp Newton, nếu x0 là nghiệm của phương trình f(x) thì x = x0 - f(x)/f'(x0) (x -> x0).Khởi tạo với x = 0.
Tìm đến khi nào f(x) có giá trị sấp sỉ kết quả cần tìm.
"""

import numpy as np

def _xArr(xValue, maxExponent):
    """
    Trả về một ma trận array(0, x, x^2, ...., x^n) là ma trận giá trị của số x.
    :param xValue: là x
    :param maxExponent: là n
    :return:
    """
    _result = []
    for i in range(maxExponent):
        _result.append(xValue ** i)
    return np.array(_result)

def _f(factor: np.ndarray, x):
    """
    Trả về giá trị hàm f(x)
    :param factor: ma trận hệ số của f(x) (array(a0, a1, a2, ...., an)).
    :param x: giá trị của x.
    :return:
    """
    if len(factor.shape) != 1:
        raise ValueError("Ma trận hệ số không chính xác.")
    xArr = _xArr(x, len(factor))
    return np.dot(xArr, factor.T)

def _fx(factor: np.ndarray):
    """
    Trả về ma trận hệ số của đạo hàm của hàm fx.
    :param factor: ma trận hệ số của hàm fx
    :return:
    """
    _result = []
    for i in range(len(factor)):
        _result.append(i * factor[i])
    return np.array(_result[1:])

def _find(factor: np.ndarray, result):
    """
    Tìm ra 1 nghiệm của phương trình
    :param factor: hệ số của phương trình.
    :param result: giá trị mà phương trình sẽ hướng tới.
    :return: giá trị x sao cho f(x) ~ result.
    """
    _x = 0
    _min = 0.1
    _derivation = _fx(factor)
    _tmp = _f(factor, _x)
    while _tmp - result > _min or _tmp  - result < -_min:
        _x = _x - _tmp/_f(_derivation, _x)
        _tmp = _f(factor, _x)
    return _x