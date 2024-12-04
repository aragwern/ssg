import re
from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter: str, text_type: TextType):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        fragments = node.text.split(delimiter)
        if len(fragments) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for index, fragment in enumerate(fragments):
            if fragment == "":
                continue
            if index % 2 == 1:  # odd index means to format
                new_nodes.append(TextNode(fragment, text_type))
            else:
                new_nodes.append(TextNode(fragment, TextType.TEXT))

    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        images = extract_markdown_images(node.text)
        if not images and node.text != "":
            new_nodes.append(node)
            continue
        text_to_split = node.text
        for image in images:
            text_split = text_to_split.split(f"![{image[0]}]({image[1]})", 1)
            if len(text_split) != 2:
                raise ValueError("Invalid markdown, image section not closed")
            if text_split[0] != "":
                new_nodes.append(TextNode(text_split[0], TextType.TEXT))
            new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))
            text_to_split = text_split[1]
        if text_to_split != "":
            new_nodes.append(TextNode(text_to_split, TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        links = extract_markdown_links(node.text)
        if not links and node.text != "":
            new_nodes.append(node)
            continue
        text_to_split = node.text
        for link in links:
            text_split = text_to_split.split(f"[{link[0]}]({link[1]})", 1)
            if len(text_split) != 2:
                raise ValueError("Invalid markdown, link section not closed")
            if text_split[0] != "":
                new_nodes.append(TextNode(text_split[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text_to_split = text_split[1]
        if text_to_split != "":
            new_nodes.append(TextNode(text_to_split, TextType.TEXT))

    return new_nodes


def text_to_textnodes(text):
    nodes = []
    nodes.append(TextNode(text, TextType.TEXT))
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "*", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)

    return nodes
