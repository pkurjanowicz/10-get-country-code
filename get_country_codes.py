def get_country_codes(prices):
    split_string = prices.split()
    final_str = ''
    for country in split_string:
        new_value = country[:2]
        new_country_str = new_value + ", "
        final_str += new_country_str
    final_str = final_str[:-2]
    return final_str

from test import testEqual

testEqual(get_country_codes("NZ$300, KR$1200, DK$5"), "NZ, KR, DK")
testEqual(get_country_codes("US$40, AU$89, JP$200"), "US, AU, JP")
testEqual(get_country_codes("AU$23, NG$900, MX$200, BG$790, ES$2"), "AU, NG, MX, BG, ES")
testEqual(get_country_codes("CA$40"), "CA")
