from enum import Enum
from htmlnode import LeafNode
import re


class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = None if url == "link" else url

    def __eq__(self, other):
        return (
            self.text == other.text
            and self.text_type == other.text_type
            and self.url == other.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise ValueError(f"Invalid text type: {text_node.text_type}")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        if delimiter not in node.text:
            raise ValueError(f"There is no '{delimiter}' inside text: {node.text}")
        fragments = node.text.split(delimiter)
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
        images = extract_markdown_images(node.text)
        if not images and node.text != "":
            new_nodes.append(node)
            continue
        text_to_split = node.text
        for image in images:
            text_split = text_to_split.split(f"![{image[0]}]({image[1]})", 1)
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
        links = extract_markdown_links(node.text)
        if not links and node.text != "":
            new_nodes.append(node)
            continue
        text_to_split = node.text
        for link in links:
            text_split = text_to_split.split(f"[{link[0]}]({link[1]})", 1)
            if text_split[0] != "":
                new_nodes.append(TextNode(text_split[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text_to_split = text_split[1]
        if text_to_split != "":
            new_nodes.append(TextNode(text_to_split, TextType.TEXT))

    return new_nodes
