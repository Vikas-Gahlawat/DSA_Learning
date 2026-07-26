# F F F T T T T koko banana the monotonic array is

# Find the Minimum Valid Answer
# Koko
# Shipping
# Minimum Pages
# Minimum Days

# the monotonicity if T T T F F F

# Find the Maximum Valid Answer
# Aggressive Cows
# Magnetic Force Between Two Balls
# Maximize Minimum Distance

def can_place_cows(stalls, cows, distance):
    placed_cows = 1
    last_position = stalls[0]
    for current_stall in stalls[1:]:
        if current_stall - last_position >= distance:
            last_position = current_stall
            placed_cows += 1
        if placed_cows == cows:
            return True
    return False

def aggressive_cows(stalls, cows):
        # Your code assumes the stalls are already sorted.
        # Many interview questions guarantee that.
        # Some don't.
        # A robust implementation would start with:
        # stalls.sort() or stalls = sorted(stalls)
    left = 1
    right = stalls[-1] - stalls[0]
    answer = 0
    while left <= right:
        mid = (right + left) // 2
        can_place = can_place_cows(stalls, cows, mid)
        if can_place:
            answer = mid
            left = mid + 1
        else:
            right =  mid -1
    return answer

aggressive_cows([1, 2, 4, 8, 9], 3)