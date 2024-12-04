import os
import shutil


def main():
    copy_src_to_dst("static", "public", False)


def copy_src_to_dst(src: str, dst: str, clean: bool):
    if not os.path.exists(dst):
        os.mkdir(dst, mode=0o777)
    elif not clean:
        shutil.rmtree(dst)
        os.mkdir(dst, mode=0o777)

    dir = os.listdir(src)
    for item in dir:
        if os.path.isdir(os.path.join(src, item)):
            os.mkdir(os.path.join(dst, item))
            copy_src_to_dst(os.path.join(src, item), os.path.join(dst, item), True)
        else:
            shutil.copy(os.path.join(src, item), dst)


if __name__ == "__main__":
    main()
