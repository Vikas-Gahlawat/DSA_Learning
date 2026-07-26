def days_needed(weights, capacity):
    current_load = 0
    days = 1
    for weight in weights:
        if current_load + weight <= capacity:
            current_load += weight
        else:
            days += 1
            current_load = weight
    return days

def ship_within_days(weights, days):
    left = max(weights)
    right = sum(weights)
    answer = 0
    while left <= right:
        mid = (right + left) // 2
        cal_days = days_needed(weights, mid)
        if cal_days <= days:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer

ship_within_days([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5)
        
        