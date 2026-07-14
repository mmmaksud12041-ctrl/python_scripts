#discount function
def apply_discount(price, discount):

    #check if price is a number
    if not isinstance(price, (int, float)):
        return 'The price should be a number'

    #check if discount is a number
    if not isinstance(discount, (int, float)):
        return 'The discount should be a number'

    #check if discount is lower than or equal to 0
    if price <= 0:
        return 'The price should be greater than 0'
    
    #check if discount is lower than 0 and greater than 100
    if discount < 0 or discount > 100:
        return 'The discount should be between 0 and 100'
    
    #Return the discount percentage and calculate the price after applying discount
    return price - (price * (discount / 100))
