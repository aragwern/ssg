from enum import Enum


class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown):
    """
    Takes a string - entire markdown document.
    Returns list of "blocks" strings.
    """
    raw_blocks = markdown.split("\n\n")
    final_blocks = []
    for index, block in enumerate(raw_blocks):
        if block == "\n" or block == "":
            continue
        clean_block = ""
        lines = block.split("\n")
        for no, line in enumerate(lines):
            clean_block += line.strip()
            if no != len(lines) - 1:
                clean_block += "\n"
        final_blocks.append(clean_block.strip())

    return final_blocks


def block_to_block_type(block: str):
    """
    Takes single block, looks at its begining and returns one of supported block types.
    """
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith("> "):
        for line in lines:
            if not line.startswith("> "):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- ") or block.startswith("* "):
        for line in lines:
            if not line.startswith("- ") and not line.startswith("* "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    for line in lines:
        if ". " in line:
            if line.split(". ")[0].isdigit() and line.startswith(line.split(". ")[0]):
                continue
            else:
                return BlockType.PARAGRAPH
        else:
            return BlockType.PARAGRAPH
    return BlockType.ORDERED_LIST
