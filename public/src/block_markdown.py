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
