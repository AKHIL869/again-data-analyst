def getMaxToys(prices, money):
    max_toys = 0
    window_sum = 0
    left = 0
    
    for right in range(len(prices)):
        window_sum += prices[right]
        
        while window_sum > money:
            window_sum -= prices[left]
            left += 1
        
        max_toys = max(max_toys, right - left + 1)
    
    return max_toys

# Example usage:
prices = [1, 4, 5, 3, 2, 1, 6]
money = 6
print(getMaxToys(prices, money))
