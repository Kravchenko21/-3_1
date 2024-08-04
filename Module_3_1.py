calls = 0


def string_info(*args):
    global calls
    calls = calls + 1
    print(args)

string_info('Capybara'.upper(), 'Capybara'.lower(), len('Capybara'))
string_info('Armagedon'.upper(), 'Armagedon'.lower(), len('Armagedon'))
print(calls)



def is_contains(string, list_to_search):
    global calls
    calls = calls + 1
    if string in list_to_search:
        print(True)
    else:
        print(False)
    print(string, list_to_search)


is_contains('Urban', ['ban', 'BaNaN', 'Urban'])
is_contains('cycle', ['recycling', 'cyclic'])
print(calls)