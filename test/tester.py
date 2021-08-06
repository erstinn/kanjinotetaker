import unittest
from mainproj import input


class Test(unittest.TestCase):
    def test_tag_options(self):
        self.assertEqual(input.tag_options('c'), 'Common')
        self.assertEqual(input.tag_options('u'), 'Uncommon')
        self.assertEqual(input.tag_options('n1'), 'N1')
        self.assertEqual(input.tag_options('n2'), 'N2')
        self.assertEqual(input.tag_options('n3'), 'N3')
        self.assertEqual(input.tag_options('n4'), 'N4')
        self.assertEqual(input.tag_options('n5'), 'N5')
        self.assertEqual(input.tag_options('cn1'), 'Common, N1')
        self.assertEqual(input.tag_options('cn2'), 'Common, N2')
        self.assertEqual(input.tag_options('cn3'), 'Common, N3')
        self.assertEqual(input.tag_options('cn4'), 'Common, N4')
        self.assertEqual(input.tag_options('cn5'), 'Common, N5')
        self.assertEqual(input.tag_options('un1'), 'Uncommon, N1')
        self.assertEqual(input.tag_options('un2'), 'Uncommon, N2')
        self.assertEqual(input.tag_options('un3'), 'Uncommon, N3')
        self.assertEqual(input.tag_options('un4'), 'Uncommon, N4')
        self.assertEqual(input.tag_options('un5'), 'Uncommon, N5')


if __name__ == '__main__':
    unittest.main()
