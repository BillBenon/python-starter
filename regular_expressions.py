import re


# patterns = ['term1', 'term2']
#
# text = 'This is a string with term1, not the other!'

# for pattern in patterns:
#     print("I'm searching for: " + pattern)
#
#     if re.search(pattern, text):
#         print("MATCH!")
#     else:
#         print("NO MATCH!")

# match = re.search('term1', text)
# print(type(match))
# print(match.start())
#
# split_term = '@'
# email = 'user@gmail.com'
# print(re.split(split_term, email))

# print(re.findall('match', 'test phrase match in match middle'))

def multi_re_find(patterns, phrase):
    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat, phrase))
        print('\n')


# test_phrase = 'This is a string! But it has punctuation. How can we remove it?'

test_phrase = 'This is a string with numbers 12345 and a symbol #hashtag'

# test_patterns = ['sd*']
# test_patterns = ['sd+']
# test_patterns = ['sd{3}']
# test_patterns = ['sd{1,3}']
# test_patterns = ['s[sd]+']


# test_patterns = ['[^!.?]+']
# test_patterns = ['[a-z]+']
# test_patterns = ['[A-Z]+']

# test_patterns = [r'\d+']     # for numbers
# test_patterns = [r'\D+']       # for excluding numbers
# test_patterns = [r'\s+']         # for whitespaces only
# test_patterns = [r'\S+']         # for non-whitespaces only
# test_patterns = [r'\w+']         # for alphanumeric characters only
test_patterns = [r'\W+']         # for non-alphanumeric characters only

multi_re_find(test_patterns, test_phrase)
