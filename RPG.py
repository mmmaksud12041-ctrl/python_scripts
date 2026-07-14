#For STATS
full_dot = '●'
empty_dot = '○'

#Creating Function
def create_character(a, b, c, d):
    # 1. Check if name is a string
    if not isinstance(a, str):
        return 'The character name should be a string'
        
    # 2. Check if name is empty
    if a == '':
        return 'The character should have a name'
        
    # 3. Check if name is too long (> 10 characters)
    if len(a) > 10:
        return 'The character name is too long'
        
    # 4. Check if name contains spaces
    if ' ' in a:
        return 'The character name should not contain spaces'
        
    # 5. Check if stats are integers
    if not (isinstance(b, int) and isinstance(c, int) and isinstance(d, int)):
        return 'All stats should be integers'
        
    # 6. Check if any stats are less than 1
    if b < 1 or c < 1 or d < 1:
        return 'All stats should be no less than 1'
        
    # 7. Check if any stats are greater than 4
    if b > 4 or c > 4 or d > 4:
        return 'All stats should be no more than 4'
        
    # 8. Check if stats sum to exactly 7
    if b + c + d != 7:
        return 'The character should start with 7 points'
        
    # 9. Format output
    return f'{a}\nSTR {b*full_dot + (10-b)*empty_dot}\nINT {c*full_dot + (10-c)*empty_dot}\nCHA {d*full_dot + (10-d)*empty_dot}'
