from block_markdown import BlockType, markdown_to_blocks, block_to_block_type
from htmlnode import HTMLNode, LeafNode, ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, text_node_to_html_node


def markdown_to_html_node(markdown):
    raw_blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for block in raw_blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                p = create_p_node(block)
                html_blocks.append(p)
            case BlockType.HEADING:
                heading = create_heading_node(block)
                html_blocks.append(heading)
            case BlockType.CODE:
                pre = create_code_node(block)
                html_blocks.append(pre)
            case BlockType.QUOTE:
                blockquote = create_blockquote_node(block)
                html_blocks.append(blockquote)
            case BlockType.UNORDERED_LIST:
                ul = create_ul_node(block)
                html_blocks.append(ul)
            case BlockType.ORDERED_LIST:
                ol = create_ol_node(block)
                html_blocks.append(ol)
    body = ParentNode("body", html_blocks, None)
    html = ParentNode(
        "html",
        [
            body,
        ],
        None,
    )
    return html


def create_ul_node(block: str):
    lines = block.split("\n")
    children = []
    for line in lines:
        grand_children_text_nodes = text_to_textnodes(line[2:])
        for text_node in grand_children_text_nodes:
            html_node = text_node_to_html_node(text_node)
            children.append(ParentNode("li", html_node))
    return ParentNode("ul", children)


def create_ol_node(block: str):
    lines = block.split("\n")
    children = []
    for line in lines:
        grand_children_text_nodes = text_to_textnodes(line.split(". ", 1)[1])
        for text_node in grand_children_text_nodes:
            html_node = text_node_to_html_node(text_node)
            children.append(ParentNode("li", html_node))
    return ParentNode("ol", children)


def create_p_node(block: str):
    text_nodes = text_to_textnodes(block)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return ParentNode("p", html_nodes)


def create_blockquote_node(block: str):
    lines = block.split("\n")
    clean_lines = []
    for line in lines:
        clean_lines.append(line.strip("> ").strip())
    clean_block = "\n".join(clean_lines)
    text_nodes = text_to_textnodes(clean_block)
    html_nodes = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return ParentNode("blockquote", html_nodes)


def create_heading_node(block: str):
    headings: dict[str, str] = {
        "h6": "###### ",
        "h5": "##### ",
        "h4": "#### ",
        "h3": "### ",
        "h2": "## ",
        "h1": "# ",
    }
    heading_tag: str = ""
    for key, value in headings.items():
        if value in block:
            block = block.strip(value)
            heading_tag = key
            break
    text_nodes: list[TextNode] = text_to_textnodes(block)
    html_nodes: list[HTMLNode] = []
    for text_node in text_nodes:
        html_nodes.append(text_node_to_html_node(text_node))
    return ParentNode(heading_tag, html_nodes)


def create_code_node(block: str):
    block = block.strip("```").strip("\n")
    code = LeafNode("code", block, None)
    pre = ParentNode(
        "pre",
        [
            code,
        ],
        None,
    )
    return pre
