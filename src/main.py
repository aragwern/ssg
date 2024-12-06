import os
import shutil
from html_generator import generate_page


def main():
    if os.path.exists("public"):
        shutil.rmtree("public")
    os.mkdir("public", mode=0o777)
    copy_src_to_dst("static", "public")
    generate_page("content/index.md", "template.html", "public/index.html")


def copy_src_to_dst(src: str, dst: str):
    dir = os.listdir(src)
    for item in dir:
        if os.path.isdir(os.path.join(src, item)):
            os.mkdir(os.path.join(dst, item))
            copy_src_to_dst(os.path.join(src, item), os.path.join(dst, item))
        else:
            shutil.copy(os.path.join(src, item), dst)


if __name__ == "__main__":
    main()
