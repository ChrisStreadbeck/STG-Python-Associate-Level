import unittest
from utilities.fibonacci import fibonacci
import inflect

p = inflect.engine()


class challenge4(unittest.TestCase):

    def test_challenge4(self):
        number = fibonacci(5)
        print(f'{number} - {p.number_to_words(number)}')
        number = fibonacci(10)
        print(f'{number} - {p.number_to_words(number)}')
        number = fibonacci(15)
        print(f'{number} - {p.number_to_words(number)}')
        number = fibonacci(20)
        print(f'{number} - {p.number_to_words(number)}')
        number = fibonacci(25)
        print(f'{number} - {p.number_to_words(number)}')
        number = fibonacci(30)
        print(f'{number} - {p.number_to_words(number)}')


if __name__ == '__main__':
    unittest.main()