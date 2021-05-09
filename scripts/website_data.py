
import os
from pathlib import Path


def get_item_toml(*item):
    return """[[items]]\ntitle = "{}"\nimage = "{}"\nthumb = "{}"\nalt= "{}"\ndescription = "{}"\nurl = "{}"\n\n""".format(*item)


class GenerateWebsiteData:

    def __init__(self, src_dir, out_dir, rep_url, img_url) -> None:
        self._src_dir = src_dir
        self._out_dir = out_dir
        self._rep_url = rep_url
        self._img_url = img_url

    @property
    def src_dir(self):
        return self._src_dir

    @property
    def out_dir(self):
        return self._out_dir

    @property
    def rep_url(self):
        return self._rep_url

    @property
    def img_url(self):
        return self._img_url

    def format_item(self, file):
        return file.name, self.img_url + file.name, self.img_url + file.name, file.name, self.rep_url, self.rep_url + "blob/main/src/" + file.with_suffix(".tex").name

    def get_all_items(self, *suffix, output_file):

        suffix = (".png", ".jpg") if not(suffix) else suffix

        all_items = []
        for root, dirs, files in os.walk(self.out_dir):
            for f in files:
                if Path(f).suffix in suffix:
                    item = self.format_item(Path(f))
                    all_items.append(get_item_toml(*item))

        with open(output_file, 'w') as f:
            for item in all_items:
                f.write(item)
