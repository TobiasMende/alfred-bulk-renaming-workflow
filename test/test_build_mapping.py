import unittest

import datetime

from src.algo.build_mapping import build_filename_translations


class TestBuildMapping(unittest.TestCase):
    def test_dollar0_returnsOriginal(self):
        self.assert_single_name('abc.zip', '', '$0', 'abc.zip')
        self.assert_single_name('abc.zip', '', '$0-123', 'abc-123.zip')
        self.assert_single_name('a b c.txt', 'sadasdfs', '$0-$0', 'a b c-a b c.txt')

    def test_match_groups(self):
        self.assert_single_name('abc-123', '(.*)-.+', '$1', 'abc')
        self.assert_single_name('abc-123', '(.*)-.+', '$1-$1', 'abc-abc')
        self.assert_single_name('abc-123', '(.*)-(.+)', '$2-$1', '123-abc')
        self.assert_single_name('a-b-c-d-e-f.hello', '(a)-(b)-(c)-(d)-(e)-(f)', '$6$5$4$3$2$1', 'fedcba.hello')
        self.assert_single_name('a-b-c-d-e-f.hello', '(a)-(b)-(c)-(d)-(e)-(f)', '$6$5$4$3$2$1.txt', 'fedcba.txt.hello')

    def test_sequence_numbers(self):
        self.assert_multiple_names(['', '', '', ''], '', '{n}', ['1', '2', '3', '4'])
        self.assert_multiple_names(['', '', '', ''], '', '$0{n}', ['1', '2', '3', '4'])
        self.assert_multiple_names(['', '', '', ''], '', '$1{n}', ['1', '2', '3', '4'])
        self.assert_multiple_names(['', '', '', ''], '', '{n}{n}', ['11', '22', '33', '44'])
        self.assert_multiple_names(['a', 'b', 'c', 'd'], '', '$0-{n}', ['a-1', 'b-2', 'c-3', 'd-4'])

    def test_date_replacement(self):
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        self.assert_single_name('', '', '{d}', date)
        self.assert_single_name('hello-world.txt', '', '$0-{d}', 'hello-world-{}.txt'.format(date))

    def test_only_part_after_slash_is_used_as_pattern(self):
        self.assert_single_name('a', '', '/$0', 'a')

    def test_words_are_capitalized_with_capitalize_option(self):
        self.assert_single_name('a', '', 'c/$0', 'A')
        self.assert_single_name('a b c', '', 'c/$0', 'A B C')
        self.assert_single_name('a-b-c', '', 'c/$0', 'A-B-C')
        self.assert_single_name('a1-b-c', '', 'c/$0', 'A1-B-C')
        self.assert_single_name('a-1_b_c', '', 'c/$0', 'A-1_B_C')

    def test_replace_option(self):
        self.assert_single_name('a-', '', 'r(-,)/$0', 'a')
        self.assert_single_name('a-b-c-d', '', 'r(-, )/$0', 'a b c d')
        self.assert_single_name('a-b-', '', 'r(-,hi)/$0', 'ahibhi')

    def test_acceptance(self):
        self.assert_single_name('ab_b_c-1-2-3  .hi', '(.*?)-(.*)', 'r(_, )/r(-, )/c/$1 $2', 'Ab B C 1 2 3  .hi')
        self.assert_single_name('ab_b_c-1-2-3  .hi', '(.*?)-(.*)', 'r(_, )/r(-, )/c/r(  ,)/$1 $2', 'Ab B C 1 2 3.hi')

    def assert_single_name(self, input, match_pattern, replace_pattern, expected):
        self.assert_multiple_names([input], match_pattern, replace_pattern, [expected])

    def assert_multiple_names(self, input, match_pattern, replace_pattern, expected):
        translation = build_filename_translations(input, match_pattern, replace_pattern)
        self.assertEqual(len(expected), len(translation))
        for i in range(0, len(expected)):
            self.assertEqual(input[i], translation[i][0])
            self.assertEqual(expected[i], translation[i][1])


if __name__ == '__main__':
    unittest.main()
