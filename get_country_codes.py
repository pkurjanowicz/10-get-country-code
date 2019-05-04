def get_country_codes(prices):
    split_string = prices.split()
    final_str = ''
    for country in split_string:
        new_value = country[:2]
        new_country_str = new_value + ", "
        final_str += new_country_str
    final_str = final_str[:-2]
    return final_str
