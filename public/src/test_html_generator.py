import unittest
from html_generator import (
    create_code_node,
    create_ul_node,
    create_ol_node,
    create_p_node,
    create_blockquote_node,
    create_heading_node,
    markdown_to_html_node,
)
from htmlnode import ParentNode, LeafNode


class TestHTMLGenerator(unittest.TestCase):
    def test_markdown_to_html(self):
        text_md = """# Fedora Linux Flatpak cool apps to try for December

This article introduces projects available in Flathub with installation instructions.

[Flathub](https://flathub.org/) is the place to get and distribute apps for all of Linux. It is powered \
by Flatpak, allowing Flathub apps to run on almost any Linux distribution.

> Please read “[Getting started with Flatpak](https://fedoramagazine.org/getting-started-flatpak/)“. \
In order to enable flathub as your flatpak provider, use the instructions on the \
[flatpak site](https://flatpak.org/setup/Fedora).

These apps are classified into four categories:

- Productivity
- Games
- Creativity
- Miscellaneous

## Ghostwriter

![alt text](https://fedoramagazine.org/wp-content/uploads/2024/11/image-2-1024x505.png)

```
flatpak install flathub org.kde.ghostwriter
```

*Ghostwriter is also available as an rpm in the Fedora Linux repositories*
"""
        text_node = markdown_to_html_node(text_md)
        expected_html_node = ParentNode(
            "html",
            [
                ParentNode(
                    "body",
                    [
                        ParentNode(
                            "h1",
                            [
                                LeafNode(
                                    None,
                                    "Fedora Linux Flatpak cool apps to try for December",
                                ),
                            ],
                        ),
                        ParentNode(
                            "p",
                            [
                                LeafNode(
                                    None,
                                    "This article introduces projects available in Flathub with installation instructions.",
                                ),
                            ],
                        ),
                        ParentNode(
                            "p",
                            [
                                LeafNode(
                                    "a", "Flathub", {"href": "https://flathub.org/"}
                                ),
                                LeafNode(
                                    None,
                                    " is the place to get and distribute apps for all of Linux. It is powered by Flatpak, allowing Flathub apps to run on almost any Linux distribution.",
                                ),
                            ],
                        ),
                        ParentNode(
                            "blockquote",
                            [
                                LeafNode(
                                    None,
                                    "Please read “",
                                ),
                                LeafNode(
                                    "a",
                                    "Getting started with Flatpak",
                                    {
                                        "href": "https://fedoramagazine.org/getting-started-flatpak/"
                                    },
                                ),
                                LeafNode(
                                    None,
                                    "“. In order to enable flathub as your flatpak provider, use the instructions on the ",
                                ),
                                LeafNode(
                                    "a",
                                    "flatpak site",
                                    {"href": "https://flatpak.org/setup/Fedora"},
                                ),
                                LeafNode(
                                    None,
                                    ".",
                                ),
                            ],
                        ),
                        ParentNode(
                            "p",
                            [
                                LeafNode(
                                    None,
                                    "These apps are classified into four categories:",
                                ),
                            ],
                        ),
                        ParentNode(
                            "ul",
                            [
                                ParentNode(
                                    "li",
                                    LeafNode(
                                        None,
                                        "Productivity",
                                    ),
                                ),
                                ParentNode(
                                    "li",
                                    LeafNode(
                                        None,
                                        "Games",
                                    ),
                                ),
                                ParentNode(
                                    "li",
                                    LeafNode(
                                        None,
                                        "Creativity",
                                    ),
                                ),
                                ParentNode(
                                    "li",
                                    LeafNode(
                                        None,
                                        "Miscellaneous",
                                    ),
                                ),
                            ],
                        ),
                        ParentNode(
                            "h2",
                            [
                                LeafNode(
                                    None,
                                    "Ghostwriter",
                                ),
                            ],
                        ),
                        ParentNode(
                            "p",
                            [
                                LeafNode(
                                    "img",
                                    "",
                                    {
                                        "src": "https://fedoramagazine.org/wp-content/uploads/2024/11/image-2-1024x505.png",
                                        "alt": "alt text",
                                    },
                                ),
                            ],
                        ),
                        ParentNode(
                            "pre",
                            [
                                LeafNode(
                                    "code",
                                    "flatpak install flathub org.kde.ghostwriter",
                                ),
                            ],
                        ),
                        ParentNode(
                            "p",
                            [
                                LeafNode(
                                    "i",
                                    "Ghostwriter is also available as an rpm in the Fedora Linux repositories",
                                ),
                            ],
                        ),
                    ],
                    None,
                ),
            ],
            None,
        )
        self.assertEqual(expected_html_node, text_node)

    def test_create_ul_node(self):
        list_md = "* first item\n* second item\n* third item"
        list_node = create_ul_node(list_md)
        expected_html_node = ParentNode(
            "ul",
            [
                ParentNode(
                    "li",
                    LeafNode(None, "first item", None),
                    None,
                ),
                ParentNode(
                    "li",
                    LeafNode(None, "second item", None),
                    None,
                ),
                ParentNode(
                    "li",
                    LeafNode(None, "third item", None),
                    None,
                ),
            ],
            None,
        )

        self.assertEqual(expected_html_node, list_node)

    def test_create_ol_node(self):
        list_md = "1. first item\n2. second item\n3. third item"
        list_node = create_ol_node(list_md)
        expected_html_node = ParentNode(
            "ol",
            [
                ParentNode(
                    "li",
                    LeafNode(None, "first item", None),
                    None,
                ),
                ParentNode(
                    "li",
                    LeafNode(None, "second item", None),
                    None,
                ),
                ParentNode(
                    "li",
                    LeafNode(None, "third item", None),
                    None,
                ),
            ],
            None,
        )
        self.assertEqual(expected_html_node, list_node)

    def test_create_p_node(self):
        paragraph_md = "In the Productivity section we have \
[Ghostwriter](https://flathub.org/apps/org.kde.ghostwriter). \
Ghostwriter is a distraction-free text editor for Markdown \
featuring a live HTML preview as you type, theme creation, \
focus mode, fullscreen mode, live word count, and document \
navigation."
        paragraph_node = create_p_node(paragraph_md)
        expected_html_node = ParentNode(
            "p",
            [
                LeafNode(None, "In the Productivity section we have ", None),
                LeafNode(
                    "a",
                    "Ghostwriter",
                    {"href": "https://flathub.org/apps/org.kde.ghostwriter"},
                ),
                LeafNode(
                    None,
                    ". Ghostwriter is a distraction-free text editor for Markdown \
featuring a live HTML preview as you type, theme creation, \
focus mode, fullscreen mode, live word count, and document \
navigation.",
                    None,
                ),
            ],
            None,
        )
        self.assertEqual(expected_html_node, paragraph_node)

    def test_create_blockquote_node(self):
        blockqoute_md = "> In the Productivity section we have \
[Ghostwriter](https://flathub.org/apps/org.kde.ghostwriter).\n\
> Ghostwriter is a distraction-free text editor for Markdown \
featuring a live HTML preview as you type, theme creation, \
focus mode, fullscreen mode, live word count, and document \
navigation."
        blockquote_node = create_blockquote_node(blockqoute_md)
        expected_html_node = ParentNode(
            "blockquote",
            [
                LeafNode(None, "In the Productivity section we have ", None),
                LeafNode(
                    "a",
                    "Ghostwriter",
                    {"href": "https://flathub.org/apps/org.kde.ghostwriter"},
                ),
                LeafNode(
                    None,
                    ".\nGhostwriter is a distraction-free text editor for Markdown \
featuring a live HTML preview as you type, theme creation, \
focus mode, fullscreen mode, live word count, and document \
navigation.",
                    None,
                ),
            ],
            None,
        )
        self.assertEqual(expected_html_node, blockquote_node)

    def test_create_heading_node(self):
        heading_md = "## Heading two"
        heading_node = create_heading_node(heading_md)
        expected_html_node = ParentNode(
            "h2",
            [LeafNode(None, "Heading two", None)],
            None,
        )
        self.assertEqual(expected_html_node, heading_node)

    def test_create_code_node(self):
        code_md = "```\nflatpak install flathub org.kde.ghostwriter\n```"
        code_node = create_code_node(code_md)
        expected_html_node = ParentNode(
            "pre",
            [
                LeafNode(
                    "code",
                    "flatpak install flathub org.kde.ghostwriter",
                    None,
                )
            ],
            None,
        )
        print(expected_html_node)
        print(code_node)
        self.assertEqual(expected_html_node, code_node)


if __name__ == "__main__":
    unittest.main()
