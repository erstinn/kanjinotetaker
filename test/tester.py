import unittest
from mainproj import kanjiNote


class Test(unittest.TestCase):

    def setUp(self):
        self.kanji = kanjiNote.KanjiNoteTaker()

    def test_tag_options(self):
        self.assertEqual(self.kanji.tagoptions('c'), 'Common')
        self.assertEqual(self.kanji.tagoptions('u'), 'Uncommon')
        self.assertEqual(self.kanji.tagoptions('n1'), 'N1')
        self.assertEqual(self.kanji.tagoptions('n2'), 'N2')
        self.assertEqual(self.kanji.tagoptions('n3'), 'N3')
        self.assertEqual(self.kanji.tagoptions('n4'), 'N4')
        self.assertEqual(self.kanji.tagoptions('n5'), 'N5')
        self.assertEqual(self.kanji.tagoptions('cn1'), 'Common, N1')
        self.assertEqual(self.kanji.tagoptions('cn2'), 'Common, N2')
        self.assertEqual(self.kanji.tagoptions('cn3'), 'Common, N3')
        self.assertEqual(self.kanji.tagoptions('cn4'), 'Common, N4')
        self.assertEqual(self.kanji.tagoptions('cn5'), 'Common, N5')
        self.assertEqual(self.kanji.tagoptions('un1'), 'Uncommon, N1')
        self.assertEqual(self.kanji.tagoptions('un2'), 'Uncommon, N2')
        self.assertEqual(self.kanji.tagoptions('un3'), 'Uncommon, N3')
        self.assertEqual(self.kanji.tagoptions('un4'), 'Uncommon, N4')
        self.assertEqual(self.kanji.tagoptions('un5'), 'Uncommon, N5')
        self.assertEqual(self.kanji.tagoptions('n1u'), 'N1')
        self.assertEqual(self.kanji.tagoptions('n4c'), 'N4')

    def test_take_input(self):
        self.assertIsNone(self.kanji.takeinput())


if __name__ == '__main__':
    unittest.main()
