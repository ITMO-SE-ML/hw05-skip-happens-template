"""Реализуйте метрики самостоятельно. Положительный класс — skip=1.

Входы: непустые одномерные массивы одинаковой длины. Метки только 0/1.
Для вероятностей допустимы конечные значения в [0, 1].
Некорректные входы отклоняются с ValueError.
Каждая функция возвращает скаляр float.
"""

def precision(y_true, y_pred):
    """TP/(TP+FP). Нулевой знаменатель даёт 0."""
    raise NotImplementedError


def recall(y_true, y_pred):
    """TP/(TP+FN). Нулевой знаменатель даёт 0."""
    raise NotImplementedError


def fbeta(y_true, y_pred, beta=1.0):
    """(1+beta**2)*TP/((1+beta**2)*TP+beta**2*FN+FP).

    beta — конечное положительное число. Нулевой знаменатель даёт 0.
    """
    raise NotImplementedError


def error_cost(y_true, y_pred, fp_cost=1.0, fn_cost=1.0):
    """(fp_cost*FP + fn_cost*FN)/N.

    Веса — конечные неотрицательные числа.
    """
    raise NotImplementedError


def binary_log_loss(y_true, probabilities, eps=1e-6):
    """Среднее -y*log(p)-(1-y)*log(1-p), натуральный логарифм.

    eps — конечное число в (0, 0.5).
    Допустимые p обрезаются в [eps, 1-eps].
    """
    raise NotImplementedError

