def track_customers(N, S):
    occupied = set()
    walked_away = set()
    
    for customer in S:
        if customer in occupied:
            occupied.remove(customer)
        else:
            if len(occupied) < N:
                occupied.add(customer)
            else:
                walked_away.add(customer)
    
    return len(walked_away)

# Example usage:
N = 3
S = "GACCBDDBAGEE"
print(track_customers(N, S))  # Output: 1

N = 1
S = "ABCBAC"
print(track_customers(N, S))  # Output: 2
