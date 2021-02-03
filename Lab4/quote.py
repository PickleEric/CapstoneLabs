"""
Generate quotes for a lawn mowing service
small = 10
med = 15 
large = 20
add same day + 5

"""

def lawn_quote(size, same_day):
    if size == 'small':
        price = 10
    elif size == 'medium':
        price = 15
    elif size == 'large':
        price = 20
    else:
        return #cant calc, return None

    if same_day:
        price += 5
    
    return price
