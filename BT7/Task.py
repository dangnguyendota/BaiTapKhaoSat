# encoding: utf-8
# module Task
"""
Bài tập 7
Tạo ngày: 19/8/2018 11:45PM
Bởi: Nguyễn Đăng Nguyên
Đề bài: Nếu ngày hôm nay Nắng thì xác suất ngày hôm sau cũng Nắng là 0.3 và xác suất ngày hôm sau Mưa là 0.7.
Nếu ngày hôm nay Mưa thì xác suất ngày hôm sau Mưa là 0.4, xác suất ngày hôm sau Nắng là 0.6.
Giả định xác suất Nắng một ngày nào đó là 0.5. Viết và công thức và chương trình tính xác suất Nắng/Mưa ngày sau đó 1 tuần.
Bài làm: Dùng nhân ma trận, tính xác suất ngày thứ 2, xong dùng ngày thứ 2 tính xs ngày thứ 3,.....
"""
import numpy as np

def _xs(today: np.ndarray, factor: np.ndarray, day):
    """
    Tính xác suất nắng và mưa sau n ngày
    :param today: xác suất nắng mưa ngày hôm này array(nắng, mưa)
    :param factor: xác suất chuyển đổi array((nắng-> nắng, nắng-> mưa), (mưa->nắng, mưa->mưa))
    :param day: số ngày
    :return: xác suất nắng, mưa sau n ngày dạng array(nắng, mưa)
    """
    _result = today.copy()
    for i in range(day):
        _result = np.dot(_result, factor)
    return _result