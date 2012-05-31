from unittest import TestCase, main

from rummy import TILES, valid_set, valid_run, strs_to_tiles

class TestTiles(TestCase):
    def test_len(self):
        self.assertEqual(len(TILES), 13*4*2 + 2)

class TestValid(TestCase):
    def test_valid_set(self):
        self.assertTrue(valid_set(
            strs_to_tiles('1Ba', '1Oa', '1Ra')))
        self.assertTrue(valid_set(
            strs_to_tiles('1Ba', '1Oa', '1Ra', '1Ua')))
        self.assertTrue(valid_set(
            strs_to_tiles('1Ba', '1Oa', 'JJa')))
        self.assertTrue(valid_set(
            strs_to_tiles('1Ba', '1Oa', 'JJa', 'JJb')))

        self.assertFalse(valid_set(
            strs_to_tiles('1Ba', '1Oa')))
        self.assertFalse(valid_set(
            strs_to_tiles('1Ba', '1Oa', '1Ra', '1Bb')))
        self.assertFalse(valid_set(
            strs_to_tiles('1Ba', '1Oa', '2Ra')))

    def test_valid_run(self):
        self.assertTrue(valid_run(
            strs_to_tiles('1Ba', '2Ba', '3Ba')))
        self.assertTrue(valid_run(
            strs_to_tiles('2Ba', '1Ba', '3Ba')))
        self.assertTrue(valid_run(
            strs_to_tiles('1Ba', '2Ba', 'JJa', '4Ba')))
        self.assertTrue(valid_run(
            strs_to_tiles('1Ba', '2Ba', 'JJa', 'JJb', '5Ba')))
        self.assertTrue(valid_run(
            strs_to_tiles('JJa', 'JJb', *('{n}Ba'.format(n=n) for n in range(2, 13)))))

        self.assertFalse(valid_run(
            strs_to_tiles('1Ba', '2Ba')))
        self.assertFalse(valid_run(
            strs_to_tiles('1Ua', '2Ba', '3Oa')))
        self.assertFalse(valid_run(
            strs_to_tiles('1Ba', '2Ba', '3Ba', '3Bb')))
        self.assertFalse(valid_run(
            strs_to_tiles('1Ba', '2Ba', '4Ba', '5Ba')))
        self.assertFalse(valid_run(
            strs_to_tiles('1Ba', '2Ba', 'JJa', '5Ba')))
        self.assertFalse(valid_run(
            strs_to_tiles('JJa', 'JJb', *('{n}Ba'.format(n=n) for n in range(1, 14)))))

if __name__ == '__main__':
    main()
