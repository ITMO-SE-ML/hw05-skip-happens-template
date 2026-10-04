"""Показатель и его параметры выбирает студент, независимо от сценария."""

def permutation_importance(model, X, y, score_fn, greater_is_better,
                           n_repeats=3, seed=42):
    """score_fn(model, X, y) возвращает скаляр с фиксированными настройками.

    Importance положительна при ухудшении качества после перестановки.
    Модель не переобучается внутри измерения importance.
    Вернуть словарь {имя колонки X: средняя importance по перестановкам}.
    greater_is_better задаёт направление улучшения score_fn.
    Для показателя, где больше лучше: importance = исходный score - score
    после перестановки; где меньше лучше — разность с обратным знаком.
    n_repeats — положительное целое число; seed обеспечивает воспроизводимость.
    """
    raise NotImplementedError


def select_features(importances, n_features):
    """Вернуть имена n_features признаков с наибольшей importance.

    importances — словарь {имя признака: числовая importance}.
    n_features — целое число от 1 до размера словаря; иначе ValueError.
    При равной importance сортировать имена по алфавиту.
    Размер набора студент выбирает по локальной валидации.
    """
    raise NotImplementedError

