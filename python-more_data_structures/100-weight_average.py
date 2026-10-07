#!/usr/bin/python3
"""Calculate the weighted average of score and weight pairs."""


def weight_average(my_list=[]):
    """Return the weighted mean, or 0 for an empty/zero-weight list."""
    if not my_list:
        return 0
    weighted_sum = sum(score * weight for score, weight in my_list)
    total_weight = sum(weight for score, weight in my_list)
    return weighted_sum / total_weight if total_weight else 0
