calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    global calls
    count_calls()
    length = len(string)
    uppercase = string.upper()
    lowercase = string.lower()
    return length, uppercase, lowercase
def is_contains(string, list_to_search):
    global calls
    count_calls()
    if string.lower() in map(str.lower, list_to_search):
        return True
    else:
        return False

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~urBAN
print(is_contains('cycle', ['recycling', 'cycling'])) # No matches
print(calls)
