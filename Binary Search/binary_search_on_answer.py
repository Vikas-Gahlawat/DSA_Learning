def hours_needed(piles, speed):
    cal_hour = 0
    for index, value in enumerate(piles):
        cal_hour += -( -value // speed)
    return cal_hour

def min_eating_speed(piles, h):
    left = 1
    right = max(piles)
    answer = 0
    if h == len(piles):
        return right
    while left <= right:
        mid = (right + left) // 2
        needed = hours_needed(piles, mid)
        if needed <= h:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

min_eating_speed([3, 6, 7, 11], 8)