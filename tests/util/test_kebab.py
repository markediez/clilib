import clilib.util


def test_to_kebab():
    mock = {
        'alllower': 'alllower',
        'ALLCAPS': 'allcaps',
        'ProperCase': 'proper-case',
        'camelCase': 'camel-case',
        'CAPSlower': 'cap-slower',
        'lowerCAPS': 'lower-caps',
        'CAPSlowerProper': 'cap-slower-proper',
        'lowerCAPSlower': 'lower-cap-slower'
    }

    for userInput, expectedOutput in mock.items():
        assert(clilib.util.to_kebab(userInput) == expectedOutput)
