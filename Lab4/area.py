""" 
Functions for calc dif functions for various shapes:

"""

def triangle_area(height, base):
    if base < 0 or height < 0:
        raise ValueError('Base and height need to be greater then 0')
    
    return height * base * 0.5