#better code readability

def checkArmstrong(n):
    num = n
    length = len(str(n))  # Calculate the number of digits directly
    sumo = sum(int(digit) ** length for digit in str(n))  # Use list comprehension for efficiency
    return sumo == num