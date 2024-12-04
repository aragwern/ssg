import unittest

from block_markdown import BlockType, markdown_to_blocks, block_to_block_type


class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
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

    def test_block_to_block_type(self):
        self.assertEqual(block_to_block_type("# Heading"), BlockType.HEADING)
        self.assertEqual(block_to_block_type("```\ncode\n```"), BlockType.CODE)
        self.assertEqual(block_to_block_type("> quote"), BlockType.QUOTE)
        self.assertEqual(
            block_to_block_type("- unordered\n* list"), BlockType.UNORDERED_LIST
        )
        self.assertEqual(block_to_block_type("1. ordered"), BlockType.ORDERED_LIST)
        self.assertEqual(block_to_block_type("Lorem ipsum"), BlockType.PARAGRAPH)
        self.assertEqual(
            block_to_block_type("100. Lorem ipsum\n200. Dolor est"),
            BlockType.ORDERED_LIST,
        )
        self.assertEqual(
            block_to_block_type("1. Lorem ipsum\nDolor est"),
            BlockType.PARAGRAPH,
        )


if __name__ == "__main__":
    unittest.main()
