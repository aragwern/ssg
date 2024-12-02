import unittest

from block_markdown import markdown_to_blocks


class TestBlockMarkdown(unittest.TestCase):
    def test_1(self):
        markdown_sample = """
        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside of it.

        * This is the first list item in a list block
        * This is a list item
        * This is another list item
        """

        expected = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]

        result = markdown_to_blocks(markdown_sample)
        print("======================================================================")
        print(f"Testing method: {markdown_to_blocks.__name__}")
        print(f"EXPECTED:\n{expected}")
        print(f"RESULT:\n{result}")
        print("======================================================================")
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
